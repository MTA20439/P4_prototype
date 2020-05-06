import threading
import pyfirmata
import time
import sounddevice as sd

from Synthesizer import StringSynthesizer
from additiveStream import AdditiveStream
from SongDatabase import SongDatabase


class ReadButtonThread(threading.Thread):
    def __init__(self, pin, sound, audio_player):
        threading.Thread.__init__(self)
        self.pin = pin
        self.audio_player = audio_player
        self.sound = sound
        self.init_setup_pin()
        self.isPlaying = False

    def run(self):
        while True:

            # analog_value = analog_input.read() # for reading the analog pin
            isPressed = board.digital[self.pin].read()

            if isPressed is True:
                if self.isPlaying is False:
                    self.isPlaying = True
                # board.digital[13].write(1)
            else:
                if self.isPlaying is True:
                    self.audio_player.play(sample=self.sound)
                    self.isPlaying = False
                # board.digital[13].write(0)

            time.sleep(0.1)

    def init_setup_pin(self):
        board.digital[self.pin].mode = pyfirmata.INPUT
        # self.analog_input = board.get_pin('a:0:i') # for setting up the analog pin


"""setting up which usb port is the arduino connected to"""
board = pyfirmata.Arduino('COM3')  # might want to change this based on your pc

"""Initialize communication with the arduino board"""
it = pyfirmata.util.Iterator(board)
it.start()

"""Initialize the player"""
player = AdditiveStream()

"""Arrays for storing some initial data"""
notes = [261.63, 293.66, 329.63]
pins = [10, 8, 7]  # array of pins
sounds = []  # array for storing sounds we want the threads to play

samplerate = 44100

"""A for loop for making sounds"""
for i in notes:
    string = StringSynthesizer(samplerate, 1, 2, i, 1)
    sounds.append(string)

"""A for loop for making threads and assigning them sounds"""
for i in range(len(sounds)):
    t = ReadButtonThread(pins[i], sounds[i].getString(), player)
    t.start()

print("setup done")
