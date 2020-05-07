

from unittest import TestCase
from ch_2and3_ver4 import my_transpose_vector

class TestTransposeVector(TestCase):
    def setUp(self):
        print("begin")

    def tearDown(self):
        print("end")
    # 課題1 ベクトルの転置を求める関数
    def test_my_transpose_vector(self):

        # # 整数 1次元
        # self.assertEqual([[2]], ch_2and3.my_transpose_vector([[2]])) # タテ を ヨコ に
        # self.assertEqual([[2]], ch_2and3.my_transpose_vector([[2]])) # ヨコ を タテ に

        #整数 2次元
        self.assertEqual([[11, -12]], my_transpose_vector([[11], [-12]])) # タテ を ヨコ に
        self.assertEqual([[11], [-12]], my_transpose_vector([[11, -12]])) # ヨコ を タテ に

        #整数 3次元
        self.assertEqual([[11, -12, 13]], my_transpose_vector([[11], [-12], [13]])) # タテ を ヨコ に
        self.assertEqual([[11], [-12], [13]], my_transpose_vector([[11, -12, 13]])) # ヨコ を タテ に

        #整数 4次元
        self.assertEqual([[11, -12, 13, 14]], my_transpose_vector([[11], [-12], [13], [14]])) # タテ を ヨコ に
        self.assertEqual([[11], [-12], [13], [14]], my_transpose_vector([[11, -12, 13, 14]])) # ヨコ を タテ に

        #少数
        self.assertEqual([[1.23, 2.34, 3.45, 4.56]], my_transpose_vector([[1.23], [2.34], [3.45], [4.56]])) # タテ を ヨコ に
        self.assertEqual([[1.23], [2.34], [3.45], [4.56]], my_transpose_vector([[1.23, 2.34, 3.45, 4.56]])) # ヨコ を タテ に

        #複素数
        self.assertEqual([[5+4j, 4+3j, 3+2j, 2+1j]], my_transpose_vector([[5+4j], [4+3j], [3+2j], [2+1j]])) # タテ を ヨコ に
        self.assertEqual([[5+4j], [4+3j], [3+2j], [2+1j]], my_transpose_vector([[5+4j, 4+3j, 3+2j, 2+1j]])) # ヨコ を タテ に




if __name__ == "__main__":
    unittest.main()
