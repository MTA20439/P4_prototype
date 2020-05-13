import random
from numba import njit
import numpy as np


class StringSynthesizer:
    def __init__(self, samplerate, amplitude, duration, decay):
        self.samplerate = samplerate
        self.amplitude = amplitude
        self.duration = duration
        self.decay = decay
        self.init_makeSomeNoise()
        self.octave = 1

    def init_makeSomeNoise(self):
        self.waveform = np.array(
            [(np.random.uniform(-self.amplitude, self.amplitude)) for _ in range(int(self.samplerate * self.duration))])

    def genKarplusStrong(self, note_freq):
        note = note_freq * self.octave
        delay = int(self.samplerate / note)
        decay = float(np.clip(0, 1, float(self.decay)))
        output = self.waveform
        # idx = delay
        # while idx < len(output):
        # output[idx] = decay * 0.5 * (output[idx - delay] + output[idx - delay - 1])
        # idx += 1

        for idx in range(delay, len(output)):
            output[idx] = decay * 0.5 * (output[idx - delay] + output[idx - delay - 1])
        string = output

        return string
