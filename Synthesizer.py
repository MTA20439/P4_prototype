import random
from numba import njit
import numpy as np


class StringSynthesizer:
    def __init__(self, samplerate, amplitude, duration, decay):
        self.samplerate = samplerate
        self.amplitude = amplitude
        self.duration = duration
        self.decay = decay
        self.octave = 1

    def makeSomeNoise(self):
        wave = np.array(
            [(np.random.uniform(-self.amplitude, self.amplitude)) for _ in range(int(self.samplerate * self.duration))])
        return wave

    def genKarplusStrong(self, note_freq):
        waveform = self.makeSomeNoise()
        note = note_freq * self.octave
        delay = int(self.samplerate / note)
        decay = float(np.clip(0, 1, float(self.decay)))
        output = waveform

        for idx in range(delay, len(output)):
            output[idx] = decay * 0.5 * (output[idx - delay] + output[idx - delay - 1])
        return output
