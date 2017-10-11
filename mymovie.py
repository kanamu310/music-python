import subprocess
import wave


def MovieMake(wavefile, fname, times):
    subprocess.run(["sh", "scr_mov.sh", "pic.jpg", "{0}".format(wavefile),
                   "{0}".format(fname), "{0}".format(times)])


def LengthMusic(wavefile):
    wf = wave.open("{0}".format(wavefile), "r")
    times = int(wf.getnframes()) / wf.getframerate()
    return times


def upload(fname):
    subprocess.run(["sh", "youtube-upload.sh",
                   "{0}.mp4".format(fname), "{0}".format(fname)])


def main(wavefile, fname):
    times = LengthMusic(wavefile)
    MovieMake(wavefile, fname, times)
    return times
