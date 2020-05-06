import sounddevice as sd
from itertools import zip_longest


class AdditiveStream:
    def __callback(self, outdata, frames, time, status):
        outdata[:, 0] = self.__getNext(frames)

    def __init__(self):
        self.buffer = [0]
        self.stream = sd.OutputStream(channels=1, callback=self.__callback)
        self.start()

    def start(self):
        self.stream.start()

    def stop(self):
        self.stream.stop()

    def __getNext(self, frames):
        if frames > len(self.buffer):
            #print("end of buffer; extending")
            self.buffer.extend([0] * (frames - len(self.buffer)))
        out = self.buffer[:frames]
        self.buffer = self.buffer[frames:]
        return out

    def play(self, sample):
        self.buffer = [x + y for x, y in zip_longest(sample, self.buffer, fillvalue=0)]
