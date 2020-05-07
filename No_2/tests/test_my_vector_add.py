
from unittest import TestCase
from ch_2and3_ver4 import my_vector_add

class TestMyVectorAdd(TestCase):
    def setUp(self):
        print("begin")

    def tearDown(self):
        print("end")

    # 課題2-1 ベクトルの和を求める関数
    def test_my_vector_add(self):

        #整数2つ
        self.assertEqual([[0, 2]], my_vector_add([[1, -3]], [[-1, 5]])) #横ベクトル
        self.assertEqual([[0], [2]], my_vector_add([[1], [-3]], [[-1], [5]])) # 縦ベクトル

        #整数3つ
        self.assertEqual([[-24, 18, -23]], my_vector_add([[-11, 18, -8]], [[-13, 0, -15]])) #横ベクトル
        self.assertEqual([[-24], [18], [-23]], my_vector_add([[-11], [18], [-8]], [[-13], [0], [-15]])) # 縦ベクトル

        #整数4つ
        self.assertEqual([[0, 2, 5, -1]], my_vector_add([[1, -3, -1, 5]], [[-1, 5, 6, -6]])) #横ベクトル
        self.assertEqual([[0], [2], [5], [-1]], my_vector_add([[1], [-3], [-1], [5]], [[-1], [5], [6], [-6]])) # 縦ベクトル

        #整数5つ
        self.assertEqual([[25, -3, 18, 3, -13]], my_vector_add([[15, 9, 2, -2, 4]], [[10, -12, 16, 5, -17]])) #横ベクトル
        self.assertEqual([[25], [-3], [18], [3], [-13]], my_vector_add([[15], [9], [2], [-2], [4]], [[10], [-12], [16], [5], [-17]])) # 縦ベクトル

        #少数
        self.assertEqual([[-2.32, 32.57]], my_vector_add([[2.91, 14.88]], [[-5.23, 17.69]])) #横ベクトル
        self.assertEqual([[-2.32], [32.57]], my_vector_add([[2.91], [14.88]], [[-5.23], [17.69]])) # 縦ベクトル
        # expected = [[-2.32, 32.57]]
        # actual = my_vector_add([[2.91, 14.88]], [[-5.23, 17.69]])
        # self.assertAlmostEqual(expected[0][0], actual[0][0])
        # self.assertAlmostEqual(expected[0][1], actual[0][1]) # 横ベクトル
        # expected = [[-2.32], [32.57]]
        # actual = my_vector_add([[2.91], [14.88]], [[-5.23], [17.69]])
        # self.assertAlmostEqual(expected[0][0], actual[0][0])
        # self.assertAlmostEqual(expected[1][0], actual[1][0]) # 縦ベクトル

        #複素数
        self.assertEqual([[9-3j, -3-8j]], my_vector_add([[7+5j, -6+1j]], [[2-8j, 3-9j]])) #横ベクトル
        self.assertEqual([[9-3j], [-3-8j]], my_vector_add([[7+5j], [-6+1j]], [[2-8j], [3-9j]])) # 縦ベクトル

        # 異なる型同士
        self.assertEqual([[0.91, 15+3j]], my_vector_add([[2.91, 14]], [[-2, 1+3j]])) #横ベクトル
        self.assertEqual([[-2.32], [32.57]], my_vector_add([[2.91], [14.88]], [[-5.23], [17.69]])) # 縦ベクトル
        # expected = [[0.91, 15+3j]]
        # actual = my_vector_add([[2.91, 14]], [[-2, 1+3j]])
        # self.assertAlmostEqual(expected[0][0], actual[0][0])
        # self.assertAlmostEqual(expected[0][1], actual[0][1]) # 横ベクトル
        # expected = [[-2.32], [32.57]]
        # actual = my_vector_add([[2.91], [14.88]], [[-5.23], [17.69]])
        # self.assertAlmostEqual(expected[0][0], actual[0][0])
        # self.assertAlmostEqual(expected[1][0], actual[1][0]) # 縦ベクトル

if __name__ == "__main__":
    unittest.main()
