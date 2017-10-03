import sys
import wave
import struct
import numpy as np
from pylab import *

def openfile(argv):
    a_file = open (argv,encoding="utf-8")
    befor_music = a_file.read()
    a_file.close()

    return befor_music

def conversion(befor_music):
    befor_list = befor_music.split(',')

    return befor_list

def save_wave(binwaves):
    w = wave.Wave_write("output.wav")
    p = (1, 2, 8000, len(binwaves), 'NONE', 'not compressed')
    w.setparams(p)
    w.writeframes(binwaves)
    w.close()


    """wf = wave.open(filename, "w")
    wf.setnchannels(1)
    wf.setsampwidth(bit / 8)
    wf.setframerate(fs)
    wf.writeframes(data)
    wf.close()"""
