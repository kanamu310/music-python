import sys,os
sys.path.append(os.pardir)
import unittest
import test


class Test_test(unittest.TestCase):
    # createSinWave はバイナリデータを返す
    def test_createSinWave(self):
        self.assertIsInstance(test.createSinWave(1.0, 256, 8000.0, 2.0), bytes)
        self.assertIsInstance(test.createSinWave(1.0, 0, 8000.0, 2.0), bytes)
        self.assertIsInstance(test.createSinWave(1.0, 999999999999, 8000.0, 2.0), bytes)

if __name__ == "__main__":
    unittest.main()
