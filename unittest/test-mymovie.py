import sys,os
sys.path.append(os.pardir)
import unittest
import mymovie

class Test_mymovie(unittest.TestCase):

    def test_LengthMusic(self):
        print("LengthMusic test")
        # a > b
        self.assertGreater(mymovie.LengthMusic("testsound.wav"), 0)
        self.assertIsInstance(mymovie.LengthMusic("testsound.wav"),float)

if __name__ == "__main__":
    unittest.main()
