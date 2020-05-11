import threading

import numpy as np
import pyfirmata
import time

from Synthesizer import StringSynthesizer
from additiveStream import AdditiveStream
from GUI import PrototypeGUI


class ReadPiezoThread(threading.Thread):
    def __init__(self, pin, sound, audio_player, name):
        threading.Thread.__init__(self)
        self.pin = pin
        self.name = name
        self.audio_player = audio_player
        self.sound = sound
        self.init_setup_pin()
        self.isPlaying = False

    def run(self):
        while True:

            value = self.analog_input.read()  # for reading the analog pin
            # isPressed = board.digital[self.pin].read()
            if value is not None:
                # print("Thread" + " " + str(self.name) + ": " + str(value))
                # print("\n")

                if value > 0.7:
                    if self.isPlaying is False:
                        self.audio_player.play(sample=self.sound)
                        print("poop")
                        self.isPlaying = True
                    # board.digital[13].write(1)
                else:
                    if self.isPlaying is True:
                        self.isPlaying = False
                    # board.digital[13].write(0)

            time.sleep(0.1)

    def init_setup_pin(self):
        self.analog_input = board.get_pin(self.pin)
        # board.digital[self.pin].mode = pyfirmata.INPUT


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
board = pyfirmata.Arduino('COM3')  # might want to change this based on your pc

"""Initialize communication with the arduino board"""
it = pyfirmata.util.Iterator(board)
it.start()

"""Initialize the player"""
player = AdditiveStream()

"""Arrays for storing some initial data"""
notes = [65.41, 73.42, 82.41, 92.50, 103.83, 116.54]
pins = ['a:0:i', 'a:1:i', 'a:2:i', 'a:3:i', 'a:4:i', 'a:5:i']  # array of pins
sounds = []  # array for storing sounds we want the threads to play

samplerate = 44100
board.digital[5].mode = pyfirmata.INPUT

"""A for loop for making sounds"""
for i in notes:
    string = StringSynthesizer(samplerate, 1, 2, i, 1)
    sounds.append(string)

"""A for loop for making threads and assigning them sounds"""
for i in range(len(sounds) - 4):
    t = ReadPiezoThread(pins[i], sounds[i].getString(), player, i)
    t.start()

"""Booleans for checking if GUI is running"""
isPressed = False
windowExists = False

"""Making a GUI object"""
interface = gui(board)

print("setup done")

while True:
    value = board.digital[5].read()

    """Checks if button has been pressed"""
    if value is True:

        if isPressed is False:
            print("-------------------")
            print("Learning mode is on")
            if windowExists is False:
                board.digital[6].write(1)  # Lights up the learning mode led
                interface.start()  # Starts the GUI
                windowExists = True  # Says that the gui has been started

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

            board.digital[6].write(0)  # Turns of the learning mode led off
            windowExists = False

            print("-------------------")
            print("Learning mode is off")

    time.sleep(0.2)
