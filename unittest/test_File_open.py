import sys,os
sys.path.append(os.pardir)
import File_open
import unittest
import datetime
import struct

class Test_File_open(unittest.TestCase):
    def setUp(self):
        print("setUp is called.")
        mlist = ["3","200","400","600","500"]


    def tearDown(self):
        print("tearDown is called.")


    def test_conversion(self):
        mlist = ["3","200","400","600","500"]
        self.assertEqual(File_open.conversion("{0}".format(mlist[1])),["200"])
        self.assertNotEqual(File_open.conversion("{0}".format(mlist[1])),",")

    def test_save_wave(self):
        now = datetime.datetime.now()
        fname = "{0}-{1}-{2}-{3}-{4}".format(now.year, now.month, now.day, now.hour, now.minute)
        data = b'd\x00\xb0\x04'
        kind, value = struct.unpack("BxH", data)

        self.assertEqual(File_open.save_wave(data),"{0}".format(fname))

if __name__ == "__main__":
    unittest.main()
