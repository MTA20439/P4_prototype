import random
import numpy as np


class StringSynthesizer:
    def __init__(self, samplerate, amplitude, duration, note_freq, decay):
        self.samplerate = samplerate
        self.amplitude = amplitude
        self.duration = duration
        self.note_freq = note_freq
        self.decay = decay
        self.init_makeSomeNoise()
        self.init_genKarplusStrong()
        self.isPlaying = False

    def init_makeSomeNoise(self):
        self.waveform = np.array([(np.random.uniform(-self.amplitude, self.amplitude)) for _ in range(int(self.samplerate * self.duration))])

    def init_genKarplusStrong(self):
        print("Applying Karplus Strong")
        delay = int(self.samplerate / self.note_freq)
        decay = float(np.clip(0, 1, float(self.decay)))
        output = self.waveform
        # idx = delay
        # while idx < len(output):
        # output[idx] = decay * 0.5 * (output[idx - delay] + output[idx - delay - 1])
        # idx += 1
        for idx in range(delay, len(output)):
            output[idx] = decay * 0.5 * (output[idx - delay] + output[idx - delay - 1])

        self.string = output

    def getString(self):
        return self.string
