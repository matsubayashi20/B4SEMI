from unittest import TestCase
from ch_2and3_ver4 import my_vector_map
import math

class TestMyVetorMap(TestCase):
    def setUp(self):
        print("begin")

    def tearDown(self):
        print("end")

    # 課題4 ベクトルの写像を求める関数
    def test_my_vector_map(self):
        # 整数
        self.assertEqual([[3], [3]], my_vector_map([[1, 0, 2], [0, 1, 1]], [[1],[2],[1]]))

        # 小数
        self.assertEqual([[23.99], [26.17], [1.39]], my_vector_map([
        [1.1, 1.2, -1.3, 1.4],
        [-2.1, 2.2, -2.3, 2.4],
        [3.1, -3.2, 3.3, 3.4]], [[4.1], [9.8], [0.2], [5.7]]))
        # expected = [[23.03], [24.41], [3.95]]
        # actual = my_vector_map([
        # [1.1, 1.2, -1.3, 1.4],
        # [-2.1, 2.2, -2.3, 2.4],
        # [3.1, -3.2, 3.3, 3.4]], [[4.1], [9], [0.2], [5.7]])
        # for i in range(len(actual)):
        #     self.assertAlmostEqual(expected[i][0], actual[i][0])

        #複素数
        self.assertEqual([[-13+8j], [5-1j]], my_vector_map([[1+3j, 3-2j, -2], [2+1j, -3j, 1-2j]], [[3+2j],[-1j],[4]]))

        # 異なる数値型の場合
        self.assertEqual([[16.51-2j], [13.9+13.4j], [-16.5+10.1j]], my_vector_map([
        [1.1, 2, -1+3j],
        [-1, 2+2j, -2.3],
        [3+1j, -3.2, 3]], [[4.1], [9], [2j]]))
        # expected = [[16.51-2j], [13.9+13.4j], [-16.5+10.1j]]
        # actual = my_vector_map([
        # [1.1, 2, -1+3j],
        # [-1, 2+2j, -2.3],
        # [3+1j, -3.2, 3]], [[4.1], [9], [2j]])
        # for i in range(len(actual)):
        #     self.assertAlmostEqual(expected[i][0], actual[i][0])

    def test_raise_Exception(self):
        with self.assertRaises(Exception):
            my_vector_map([[1+3j, 3-2j, -2], [2+1j, -3j, 1-2j]], [[3+2j],[-1j]])    

if __name__ == "__main__":
    unittest.main()
