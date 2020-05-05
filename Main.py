import threading
import pyfirmata
import time
import sounddevice as sd
import numpy as np


class ReadButtonThread(threading.Thread):
    def __init__(self, pin, sound):
        threading.Thread.__init__(self)
        self.pin = pin
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
                    #sd.stop()
                    sd.play(self.sound)
                    self.isPlaying = False
                # board.digital[13].write(0)"""

            time.sleep(0.1)

    def init_setup_pin(self):
        board.digital[self.pin].mode = pyfirmata.INPUT
        # self.analog_input = board.get_pin('a:0:i') # for setting up the analog pin


def create_sinusoid(freq, tim):
    samplingFreq = 66100  # Hz
    nData = tim * samplingFreq
    time = np.arange(0, nData).T / samplingFreq

    amp = 0.3;
    initPhase = np.pi / 2  # rad
    sinusoid = amp * np.sin(2 * np.pi * freq * time + initPhase)

    return sinusoid


board = pyfirmata.Arduino('COM3')

it = pyfirmata.util.Iterator(board)
it.start()

notes = [261.63, 293.66, 329.63]
pins = [10, 8, 7]
sounds = []

for i in notes:
    note = np.array(create_sinusoid(i, 4))
    sounds.append(note)


for i in range(len(sounds)):
    t = ReadButtonThread(pins[i], sounds[i])
    t.start()

print("setup done")
