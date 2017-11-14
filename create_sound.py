#!/usr/bin/env python
import wave
import struct
import numpy as np
from pylab import *

def createSinWave (A, f0, fs, length):
    """振幅A,基本周波数f0, サンプリング周波数fs,長さlength秒の正弦波を作成して返す"""
    data = []
    for n in np.arange(length * fs):
        s = A * np.sin(2 * np.pi * f0 * n / fs)

        if s >  1.0: s = 1.0
        if s < -1.0: s = -1.0

        data.append(s)

    data = [int(x * 32767.0) for x in data]
    data = struct.pack("h" * len(data), *data)

    # list に * をつけると引数展開? されるらしい
    return data


def play(data, fs, bit):
    import pyaudio

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
            channels=1,
            rate=int(fs),
            output=True)
    chunk = 1024
    sp = 0

    buffer = data[sp:sp+chunk]
    while buffer != b'':
        stream.write(buffer)
        sp = sp + chunk
        buffer = data[sp:sp+chunk]

    stream.close()
    p.terminate()


if __name__ == "__main__" :
    freqList = [262, 294, 330, 349, 392, 440, 494, 523]
    for f in freqList:
        data = createSinWave(1.0, f, 8000.0, 2.0)
        play(data, 8000, 16)
