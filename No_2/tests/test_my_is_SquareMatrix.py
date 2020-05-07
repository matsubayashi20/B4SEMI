from unittest import TestCase
from ch_2and3_ver4 import my_is_SquareMatrix
import math

class TestMyIsSquareMatrix(TestCase):
    def setUp(self):
        print("begin")

    def tearDown(self):
        print("end")

    # 課題5 正方行列かどうか判定する関数
    def test_my_is_SquareMatrix(self):
        self.assertTrue(my_is_SquareMatrix([[11, 12, 13], [21, 22, 23], [31, 32, 33]]))
        self.assertFalse(my_is_SquareMatrix([[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]]))

if __name__ == "__main__":
    unittest.main()
