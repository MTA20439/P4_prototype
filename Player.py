import numpy as np
import random
import sounddevice as sd
from itertools import zip_longest

samplerate = 44100


class AudioBuffer:
    def __init__(self):
        self.buffer = [0]

    def getNext(self, frames):
        if frames > len(self.buffer):
            print("end of buffer; extending")
            self.buffer.extend([0] * (frames - len(self.buffer)))
        out = self.buffer[:frames]
        self.buffer = self.buffer[frames:]
        return out

    def addToBuffer(self, sample):
        self.buffer = [x + y for x, y in zip_longest(sample, self.buffer, fillvalue=0)]


def makeSomeNoise(amplitude, samplerate, duration):
    return [(random.uniform(-amplitude, amplitude)) for _ in range(int(samplerate * duration))]


def genKarplusStrong(NoiseBurst, samplerate, freq, decay):
    print("Applying Karplus Strong")
    delay = int(samplerate / freq)
    decay = float(np.clip(0, 1, float(decay)))
    output = NoiseBurst
    idx = delay
    while idx < len(output):
        output[idx] = decay * 0.5 * (output[idx - delay] + output[idx - delay - 1])
        idx += 1

    return output


audioBuffer = AudioBuffer()


def callback(outdata, frames, time, status):
    audioBuffer = AudioBuffer()
    outdata[:, 0] = audioBuffer.getNext(frames)

"""
noise = makeSomeNoise(1, samplerate, 0.01)
noise.extend([0] * samplerate * 5)
string1 = genKarplusStrong(noise, samplerate, 329.63, 0.995)

noise = makeSomeNoise(1, samplerate, 0.01)
noise.extend([0] * samplerate * 5)
string2 = genKarplusStrong(noise, samplerate, 261.63, 0.995)

noise = makeSomeNoise(1, samplerate, 0.01)
noise.extend([0] * samplerate * 5)
string3 = genKarplusStrong(noise, samplerate, 196.00, 0.995)

noise = makeSomeNoise(1, samplerate, 0.01)
noise.extend([0] * samplerate * 5)
string4 = genKarplusStrong(noise, samplerate, 164.81, 0.995)

noise = makeSomeNoise(1, samplerate, 0.01)
noise.extend([0] * samplerate * 5)
string5 = genKarplusStrong(noise, samplerate, 130.81, 0.995)

all = [x + y for x, y in zip_longest([x + y for x, y in zip_longest([x + y for x, y in zip_longest(
    [x + y for x, y in zip_longest(string1, string2, fillvalue=0)], string3, fillvalue=0)], string4, fillvalue=0)],
                                     string5, fillvalue=0)]
"""
# with sd.OutputStream(channels=1, callback=callback):
#     audioBuffer.addToBuffer(string1)
#     sd.sleep(25)
#     audioBuffer.addToBuffer(string2)
#     sd.sleep(25)
#     audioBuffer.addToBuffer(string3)
#     sd.sleep(25)
#     audioBuffer.addToBuffer(string4)
#     sd.sleep(25)
#     audioBuffer.addToBuffer(string5)
#     sd.sleep(2500)
#     audioBuffer.addToBuffer(all)
#
#     sd.sleep(5000)
