import pyfirmata
import time
import sounddevice as sd
import numpy as np


def create_sinusoid(freq, tim):
    samplingFreq = 66100  # Hz
    nData = tim * samplingFreq
    time = np.arange(0, nData).T / samplingFreq

    amp = 0.3;
    initPhase = np.pi / 2  # rad
    sinusoid = amp * np.sin(2 * np.pi * freq * time + initPhase)

    return sinusoid


isPlaying = False

board = pyfirmata.Arduino('COM3')

it = pyfirmata.util.Iterator(board)
it.start()

board.digital[10].mode = pyfirmata.INPUT

middleC = np.array(create_sinusoid(261.63, 10))
print("done2")

while True:
    sw = board.digital[10].read()
    if sw is True:
        board.digital[13].write(1)
        print(sw)
        if isPlaying is False:
            sd.play(middleC)
            isPlaying = True

    else:
        board.digital[13].write(0)
        sd.stop()
        isPlaying = False
    time.sleep(0.1)
