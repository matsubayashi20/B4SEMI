from unittest import TestCase
from ch_2and3_ver4 import my_vector_multiply

class TestMyVetorMultiply(TestCase):
    def setUp(self):
        print("begin")

    def tearDown(self):
        print("end")
    # 課題2-2 ベクトルの積を求める関数
    def test_my_vector_multiply(self):
        #整数2つ
        self.assertEqual([[-2, 10]], my_vector_multiply(2, [[-1, 5]])) #横ベクトル
        self.assertEqual([[3], [-15]], my_vector_multiply(-3, [[-1], [5]])) # 縦ベクトル

        #整数3つ
        self.assertEqual([[-52, 0, -60]], my_vector_multiply(4, [[-13, 0, -15]])) #横ベクトル
        self.assertEqual([[-52], [0], [-60]], my_vector_multiply(4, [[-13], [0], [-15]])) # 縦ベクトル

        #整数4つ
        self.assertEqual([[1, -5, -6, 6]], my_vector_multiply(-1, [[-1, 5, 6, -6]])) #横ベクトル
        self.assertEqual([[1], [-5], [-6], [6]], my_vector_multiply(-1, [[-1], [5], [6], [-6]])) # 縦ベクトル

        #整数5つ
        self.assertEqual([[20, -24, 32, 10, -34]], my_vector_multiply(2, [[10, -12, 16, 5, -17]])) #横ベクトル
        self.assertEqual([[20], [-24], [32], [10], [-34]], my_vector_multiply(2, [[10], [-12], [16], [5], [-17]])) # 縦ベクトル

        #少数
        self.assertEqual([[-7.4789, 25.2967]], my_vector_multiply(1.43, [[-5.23, 17.69]])) #横ベクトル
        self.assertEqual([[-7.4789], [25.2967]], my_vector_multiply(1.43, [[-5.23], [17.69]])) # 縦ベクトル
        # expected = [[-7.4789, 25.2967]]
        # actual = my_vector_multiply(1.43, [[-5.23, 17.69]])
        # self.assertAlmostEqual(expected[0][0], actual[0][0])
        # self.assertAlmostEqual(expected[0][1], actual[0][1]) # 横ベクトル
        # expected = [[-7.4789], [25.2967]]
        # actual = my_vector_multiply(1.43, [[-5.23], [17.69]])
        # self.assertAlmostEqual(expected[0][0], actual[0][0])
        # self.assertAlmostEqual(expected[1][0], actual[1][0]) # 縦ベクトル

        #複素数
        self.assertEqual([[10-6j, 12-6j]], my_vector_multiply(1+1j, [[2-8j, 3-9j]])) #横ベクトル
        self.assertEqual([[10-6j], [12-6j]], my_vector_multiply(1+1j, [[2-8j], [3-9j]])) # 縦ベクトル

        # 異なる型同士
        self.assertEqual([[-4.9, 2.45+7.35j]], my_vector_multiply(2.45, [[-2, 1+3j]])) #横ベクトル
        self.assertEqual([[-15.69], [-9+6j]], my_vector_multiply(3, [[-5.23], [-3+2j]])) # 縦ベクトル
        # expected = [[-4.9, 2.45+7.35j]]
        # actual = my_vector_multiply(2.45, [[-2, 1+3j]])
        # self.assertAlmostEqual(expected[0][0], actual[0][0])
        # self.assertAlmostEqual(expected[0][1], actual[0][1]) # 横ベクトル
        # expected = [[-15.69], [-9+6j]]
        # actual = my_vector_multiply(3, [[-5.23], [-3+2j]])
        # self.assertAlmostEqual(expected[0][0], actual[0][0])
        # self.assertAlmostEqual(expected[1][0], actual[1][0]) # 縦ベクトル

if __name__ == "__main__":
    unittest.main()
