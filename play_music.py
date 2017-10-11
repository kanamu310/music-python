import struct
import numpy as np
from pylab import *

# オリジナルモジュール
import File_open
import test
import mymovie

if __name__ == "__main__":
    freqList = File_open.conversion(File_open.openfile(sys.argv[1]))
    datas = b""
    count = len(freqList)
    del freqList[count-1]

    freqList = [int(i) for i in freqList]

    for f in freqList:
        data = test.createSinWave(1.0, f, 8000.0, 2.0)
        # test.play(data, 8000, 16)
        datas += data

    fname = File_open.save_wave(datas)
    print("{0}.wavを出力".format(fname))
    times = mymovie.main("{0}.wav".format(fname), "{0}.mp4".format(fname))
    print("{0}.mp4を出力".format(fname))
    mymovie.upload(fname)
    print("{0}.mp4をyoutubeにアップロード".format(fname))
    print("Time[s]:{0}".format(times))
