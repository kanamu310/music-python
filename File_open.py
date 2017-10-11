import sys
import wave
import struct
import numpy as np
import datetime
from pylab import *


def openfile(argv):
    a_file = open(argv, encoding="utf-8")
    befor_music = a_file.read()
    a_file.close()

    return befor_music


def conversion(befor_music):
    befor_list = befor_music.split(',')

    return befor_list


def save_wave(binwaves):
    now = datetime.datetime.now()
    fname = "{0}-{1}-{2}-{3}-{4}".format(now.year, now.month, now.day, now.hour, now.minute)
    w = wave.Wave_write("{0}.wav".format(fname))
    p = (1, 2, 8000, len(binwaves), 'NONE', 'not compressed')
    w.setparams(p)
    w.writeframes(binwaves)
    w.close()

    return fname
