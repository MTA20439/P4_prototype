import numpy as np
import random
import sounddevice as sd
from itertools import zip_longest

class additiveStream:
    def __init__(self):
        self.buffer = [0]
        self.stream = sd.OutputStream(channels = 1, callback = callback)
        self.start()

    def start(self):
        self.stream.start()

    def stop(self):
        self.stream.stop()

    def __callback(outdata, frames, time, status):
        outdata[:,0] = self.__getNext(frames)

    def __getNext(frames):
        if frames > len(self.buffer):
            print("end of buffer; extending")
            self.buffer.extend([0] * (frames - len(self.buffer)))
        out = self.buffer[:frames]
        self.buffer = self.buffer[frames:]
        return out

    def Play(self, sample):
        self.buffer = [x + y for x,y in zip_longest(sample, self.buffer, fillvalue=0)]

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

def makeSomeNoise(amplitude, samplerate, duration):
    return [(random.uniform(-amplitude, amplitude)) for _ in range(int(samplerate * duration))]
