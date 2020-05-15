import random
import numpy as np


class StringSynthesizer:
    def __init__(self, samplerate, amplitude, duration, decay):
        self.samplerate = samplerate
        self.amplitude = amplitude
        self.duration = duration
        self.decay = float(np.clip(0, 1, float(decay)))
        self.octave = 1

    def makeSomeNoise(self):
        wave = np.array([(np.random.uniform(-self.amplitude, self.amplitude)) for _ in range(int(self.samplerate * self.duration))])
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

    def whiteNoise(self, wavelength):
        return [(random.uniform(-self.amplitude, self.amplitude)) for _ in range(int(wavelength))]

    def karplusStrong(self, NoiseBurst, frequency):
        delay = int(self.samplerate / frequency)
        output = NoiseBurst
        output.extend([0] * int(self.duration * self.samplerate))
        for idx in range(delay, len(output)):
            output[idx] = self.decay * 0.5 * (output[idx - delay] + output[idx - delay - 1])
        return output

    def fadeOut(self, sample, start=0, end=1):
        if start >= end:
            print("fadeOut 'end' must be larger than 'start'")
            return sample
        output = sample
        startIdx = int(len(sample) * start)
        endIdx = int(len(sample) * end)
        for idx in range(startIdx, endIdx):
            output[idx] = output[idx] * (1 - ((idx - startIdx) / endIdx))
        return output

    def generateGuitarString(self, frequency):
        return self.fadeOut(self.karplusStrong(self.whiteNoise(self.samplerate / (frequency * self.octave)), (frequency * self.octave)))