import threading

import numpy as np
import pyfirmata
import time
import sounddevice as sd

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


def launch_gui(board):
    myColor3 = '#101C59'
    GUI = PrototypeGUI(board)
    GUI.resvar = '960x720'
    GUI.config(bg=myColor3)
    GUI.geometry(GUI.resvar)
    GUI.resizable(0, 0)
    GUI.mainloop()


"""setting up which usb port is the arduino connected to"""
board = pyfirmata.Arduino('COM3')  # might want to change this based on your pc

"""Initialize communication with the arduino board"""
it = pyfirmata.util.Iterator(board)
it.start()

"""Initialize the player"""
player = AdditiveStream()

"""Arrays for storing some initial data"""
notes = [261.63, 293.66, 329.63]
pins = ['a:0:i', 'a:1:i', 'a:2:i']  # array of pins
sounds = []  # array for storing sounds we want the threads to play

samplerate = 44100
board.digital[10].mode = pyfirmata.INPUT

"""A for loop for making sounds"""
for i in notes:
    string = StringSynthesizer(samplerate, 1, 2, i, 1)
    sounds.append(string)

"""A for loop for making threads and assigning them sounds"""
for i in range(len(sounds) - 1):
    t = ReadPiezoThread(pins[i], sounds[i].getString(), player, i)
    t.start()

print("setup done")
isPressed = False

while True:
    value = board.digital[10].read()

    if value is True:

        if isPressed is False:
            launch_gui(board)
            isPressed = True

    else:
        if isPressed is True:
            isPressed = False
    time.sleep(0.1)


#launch_gui()

