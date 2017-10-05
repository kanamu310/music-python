#import wave
#import pyaudio
import struct
import numpy as np
from pylab import *

#オリジナルモジュール
import File_open
import test

if __name__ == "__main__" :
    freqList = File_open.conversion(File_open.openfile(sys.argv[1]))
    datas=b""
    count = len(freqList)
    del freqList[count-1]

    freqList = [int(i) for i in freqList]

    for f in freqList:
        data = test.createSinWave(1.0, f, 8000.0, 2.0)
        #test.play(data, 8000, 16)
        datas += data

    File_open.save_wave(datas)
