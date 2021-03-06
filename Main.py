import threading
import keyboard
import pyfirmata
import time

from Synthesizer import StringSynthesizer
from additiveStream import AdditiveStream
from GUI import PrototypeGUI


class ReadOctavesThread(threading.Thread):
    def __init__(self, synthesizer, breadBoard, XPin, YPin, leds):
        threading.Thread.__init__(self)
        self.synthesizer = synthesizer
        self.breadBoard = breadBoard
        self.currentPosition = 1
        self.XPin = XPin
        self.YPin = YPin
        self.init_pin(self.XPin, self.YPin)
        self.leds = leds
        self.changePosition(1)

    def run(self):
        while True:
            valueX = self.analog_inputX.read() # for reading values of x
            valueY = self.analog_inputY.read() # for reading values of Y
            if valueX is not None and valueY is not None:
                valueX = (valueX - 0.5) * 2
                valueY = (valueY - 0.5) * 2
                if valueX >= 0.9 and abs(valueY) < 1:
                    self.changePosition(1)
            
                elif abs(valueX) < 1 and valueY >= 0.9:
                    self.changePosition(2)
            
                elif valueX <= -0.9 and abs(valueY) < 1:
                    self.changePosition(3)
            
                elif abs(valueX) < 1 and valueY <= -0.9:
                    self.changePosition(4)

            #if keyboard.is_pressed('w'):
            #    self.synthesizer.octave = 1
            #    print("octave 1")

            #elif keyboard.is_pressed('a'):
            #    self.synthesizer.octave = 2
            #    print("octave 2")

            #elif keyboard.is_pressed('d'):
            #    self.synthesizer.octave = 3
            #    print("octave 3")

            #elif keyboard.is_pressed('s'):
            #    self.synthesizer.octave = 4
            #    print("octave 4")

            time.sleep(0.1)

    def changePosition(self, position):
        if self.currentPosition != position:
            self.synthesizer.octave = position
            self.currentPosition = position
            for idx in range(len(self.leds)):
                self.breadBoard.digital[self.leds[idx]].write(1 if idx == position - 1 else 0)
            print("octave " + str(position))

    def init_pin(self, pin1, pin2):
        self.analog_inputX = board.get_pin(pin1)
        self.analog_inputY = board.get_pin(pin2)
        



class ReadPiezoThread(threading.Thread):
    def __init__(self, pin, synthesizer, audio_player, led, note):
        threading.Thread.__init__(self)
        self.pin = pin
        self.audio_player = audio_player
        self.synthesizer = synthesizer
        self.led = led
        self.note = note
        self.init_setup_pin()
        self.avgVal = 0
        self.preAvgVal = 0

    def run(self):
        while True:

            value = self.analog_input.read() 
            if value != None:
                self.avgVal = ((value + (self.avgVal*24))/25) if value != 0 else self.avgVal
                if (self.avgVal - self.preAvgVal) > 0.0001:
                    self.avgVal = value
                    #print(str(self.note) + " : " + str(self.avgVal - self.preAvgVal))
                    delta = time.time()
                    self.audio_player.play(self.synthesizer.generateGuitarString(self.note))
                    delta = time.time()-delta
                    print(str(self.note) + " : " + str(delta))
                    board.digital[self.led].write(1)
                    time.sleep(0.1)
                else:
                    board.digital[self.led].write(0)
            

                self.preAvgVal = self.avgVal
            
            time.sleep(0.01)

    def init_setup_pin(self):
        self.analog_input = board.get_pin(self.pin)


class gui:
    def __init__(self, breadBoard):
        self.breadBoard = breadBoard
        self.GUI = PrototypeGUI(breadBoard)
        self.myColor3 = '#101C59'

    def start(self):
        self.GUI.resvar = '960x720'
        self.GUI.config(bg=self.myColor3)
        self.GUI.geometry(self.GUI.resvar)
        self.GUI.resizable(0, 0)
        self.GUI.mainloop()

    def getThread(self):
        existingThreads = self.GUI.threadList
        return existingThreads

    def checkIfAlive(self):
        fram = self.GUI.frame
        try:
            val = fram.winfo_exists()
        except:
            val = False
        return val


"""setting up which usb port is the arduino connected to"""
board = pyfirmata.ArduinoMega('COM3')  # might want to change this based on your pc
"""Initialize communication with the arduino board"""
it = pyfirmata.util.Iterator(board)
it.start()
time.sleep(0.01)

"""Initialize the player"""
player = AdditiveStream()

"""Arrays for storing some initial data"""
notes = [65.41, 73.42, 82.41, 92.50, 103.83, 116.54]
pins = ['a:0:i', 'a:1:i', 'a:2:i', 'a:3:i', 'a:4:i', 'a:5:i']  # array of pins
leds = [2, 3, 4, 5, 6, 7]
piezoThreads = []

samplerate = 44100
board.digital[12].mode = pyfirmata.INPUT

synth = StringSynthesizer(samplerate, 1, 2, 4)


"""A for loop for making threads and assigning them sounds"""
for i in range(len(pins)):
    t = ReadPiezoThread(pins[i], synth, player, leds[i], notes[i])
    piezoThreads.append(t)
    t.start()

octaveThread = ReadOctavesThread(synth, board, 'a:8:i', 'a:9:i', [47,51,45,49])
octaveThread.start()

"""Booleans for checking if GUI is running"""
isPressed = False
windowExists = False

"""Making a GUI object"""
interface = gui(board)

print("setup done")

while True:
    value = board.digital[12].read()

    """Checks if button has been pressed"""
    if value is True:

        if isPressed is False:
            print("-------------------")
            print("Learning mode is on")
            if windowExists is False:
                board.digital[13].write(1)  # Lights up the learning mode led

                for i in piezoThreads:
                    i.ledAvailable = False

                interface.start()  # Starts the GUI

                windowExists = True  # Says that the gui has been started

            isPressed = True


    else:
        if isPressed is True:
            isPressed = False

    """Checks if window is still alive"""
    if interface.checkIfAlive() is False:
        if windowExists is True:

            """Stopping the tread that GUI had started before being closed"""
            threads = interface.getThread()
            if len(threads) is not 0:
                threads[-1].stop()
                threads[-1].join()

            del threads

            """Deleting an old interface object and creating a new one under the same name"""
            old_object = interface
            interface = gui(board)
            del old_object

            board.digital[13].write(0)  # Turns of the learning mode led off
            windowExists = False1

            for i in piezoThreads:
                i.ledAvailable = True

            print("-------------------")
            print("Learning mode is off")

    time.sleep(0.2)
