import random
import numpy as np
class Synthesizer:
    samplerate = 44100
    def makeSomeNoise(self, amplitude, duration):
        return [(random.uniform(-amplitude, amplitude)) for _ in range(int(self.samplerate * duration))]

    def genKarplusStrong(self, NoiseBurst, freq, decay):
        print("Applying Karplus Strong")
        delay = int(self.samplerate / freq)
        decay = float(np.clip(0, 1, float(decay)))
        output = NoiseBurst
        #idx = delay
        #while idx < len(output):
            #output[idx] = decay * 0.5 * (output[idx - delay] + output[idx - delay - 1])
            #idx += 1
        for idx in range(delay, len(output)):
            output[idx] = decay * 0.5 * (output[idx - delay] + output[idx - delay - 1])

        
        return output
    def makeGString(self, duration, amplitude, freq, decay):
            return self.genKarplusStrong(self.makeSomeNoise(amplitude, duration), freq, decay)



