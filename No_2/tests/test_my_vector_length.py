from unittest import TestCase
from ch_2and3_ver4 import my_vector_length
import math

class TestMyVetorLength(TestCase):
    def setUp(self):
        print("begin")

    def tearDown(self):
        print("end")

    # 課題3 ベクトルの長さを求める関数
    def test_my_vector_length(self):
        # 整数 2次元
        self.assertEqual(round(math.sqrt(26), 13), my_vector_length([[-1, 5]])) # 横ベクトル
        self.assertEqual(round(math.sqrt(26), 13), my_vector_length([[-1], [5]])) # 縦ベクトル

        # 整数 3次元
        self.assertEqual(round(math.sqrt(42), 13), my_vector_length([[-1, 5, 4]])) # 横ベクトル
        self.assertEqual(round(math.sqrt(42), 13), my_vector_length([[-1], [5], [4]])) # 縦ベクトル

        # 整数 4次元
        self.assertEqual(round(math.sqrt(58), 13), my_vector_length([[-1, 5, 4, -4]])) # 横ベクトル
        self.assertEqual(round(math.sqrt(58), 13), my_vector_length([[-1], [5], [4], [-4]])) # 縦ベクトル

        # 小数
        self.assertEqual(round(math.sqrt(861.315), 13), my_vector_length([[8.18, -9.51, 19.7, -17.75, 0.9]])) # 横ベクトル
        self.assertEqual(round(math.sqrt(861.315), 13), my_vector_length([[8.18], [-9.51], [19.7], [-17.75], [0.9]])) # 縦ベクトル

        # 複素数
        self.assertEqual(round(math.sqrt(87), 13), my_vector_length([[1+4j, 3, 5+6j]])) # 横ベクトル
        self.assertEqual(round(math.sqrt(87), 13), my_vector_length([[1+4j],[3],[5+6j]])) # 縦ベクトル

if __name__ == "__main__":
    unittest.main()
