#!/usr/bin/env python
# coding: utf-8


import numpy as np
import math


class InnerProduct:  # 内積値と直交性かどうかのステートを持つクラス

    def __init__(self, result, orthogonal):
        self.__ip = result
        self.__orth = orthogonal

    @property
    def ip(self):
        return self.__ip

    @property
    def orth(self):
        return self.__orth


class Ch5:
    def __init__(self):
        pass

    # def euclidean_inner_product(self, vector1, vector2, show_orth=False):
    def euclidean_inner_product(self, vector1, vector2):
        # numpy配列変換
        x = np.array(vector1)
        y = np.array(vector2)

        # エラー処理
        if not x.shape == y.shape:
            raise ValueError("ベクトルのサイズが違います")
        else:
            pass

        # # エラー処理
        # try:
        #     if not x.shape == y.shape:
        #         raise ValueError("ベクトルのサイズが違います")
        #     else:
        #         pass
        # except ValueError as ve:
        #     # return ve #エラーオブジェクトを返す
        #     print(ve)
        #     return  # 関数を抜けてNoneを返す

        # 共役をとる
        conj_y = y.conj()

        # 成分ごとの積をとって加算
        tmp = []
        for i in range(x.size):
            tmp.append(x[i][0] * conj_y[i][0])
        res = sum(tmp)

        # 直交性の判断
        if round(res, 7) == 0:
            is_orthogonal = True
        else:
            is_orthogonal = False

        # # 直交性の判別を返すかどうか
        # if show_orth == True:
        #     return res, is_orthogonal
        # else:
        #     return res

        return InnerProduct(res, is_orthogonal)

    def n_norm(self, vector, n=2):
        # 強制的に縦ベクトルに変換
        vec = np.array(vector).reshape(-1, 1)

        # 計算
        tmp = []
        for i in range(vec.size):
            # print(abs(vec[i][0]))
            tmp.append(abs(vec[i][0]) ** n)  # 絶対値のn乗(たぶん複素数もOK)

        # 全部加算してn乗根
        res = sum(tmp)**(1 / n)

        return res

    def cosine_similarity(self, vector1, vector2):
        # 内積計算
        ip_xy = self.euclidean_inner_product(vector1, vector2).ip

        # ノルム計算
        norm_x = self.n_norm(vector1)
        norm_y = self.n_norm(vector2)

        if norm_x == 0 or norm_y == 0:
            raise ZeroDivisionError("ノルムが0です")
        else:
            pass

        # コサイン類似度計算
        res = ip_xy / (norm_x * norm_y)

        return res

    def unitary_matrix(self, matrix):
        """
        1. 逆行列とエルミート転置が一致　
        2. 行列自身とエルミート転置の積が単位行列  ←こっち採用中

        第三回の荒井のコードを流用→うまくいかないからnumpyでとりあえず代用
        """
        uni = np.array(matrix)

        # inv_mat = np.linalg.inv(uni)
        # print(inv_mat)
        # her_mat = np.conjugate(uni.T)
        # print(her_mat)
        # diff = np.round(inv_mat - her_mat)

        # if np.array_equiv(diff, 0) == True:
        #     return True
        # else:
        #     return False

        her_mat = np.conjugate(uni.T)
        # ide_mat = uni @ her_mat
        ide_mat = np.dot(uni, her_mat)
        ide_mat2 = np.identity(len(uni))

        for i in range(len(uni)):
            for j in range(len(uni)):
                if not round(ide_mat[i][j] - ide_mat2[i][j], 7) == 0:
                    unitary = False
                else:
                    unitary = True
        return unitary

    def Gram_Schmidt_orthonormalization(self, matrix):
        # numpy基底行列matrix_u
        matrix_u = np.array(matrix)
        u_len = len(matrix_u)

        for i in range(u_len):
            is_norm_zero = self.n_norm(matrix_u[:, i])
            if is_norm_zero == 0:
                raise ZeroDivisionError("ノルムが0です")
            else:
                pass

        # 第一手順
        u0 = np.array(matrix_u[:, 0]).reshape(-1, 1)  # 一つ目の基底を縦ベクトルで取得
        v0 = u0/(self.n_norm(u0))
        matrix_v = np.array(v0).reshape(-1, 1)

        # 第二手順
        for i in range(1, u_len):
            ui = np.array(matrix_u[:, i]).reshape(-1, 1)
            u_ = np.zeros((u_len, 1))
            for j in range(i):
                vj = np.array(matrix_v[:, j]).reshape(-1, 1)
                u_ = u_ + self.euclidean_inner_product(ui, vj).ip * vj
            vi = (ui - u_) / (self.n_norm((ui - u_)))
            matrix_v = np.hstack((matrix_v, vi))
        return matrix_v

    def orthogonal_projection(self, matrix, vector):
        x = np.array(vector).reshape(-1, 1)
        matrix_u = np.array(matrix)
        u_len = len(matrix_u)
        pwx = np.zeros((u_len, 1))

        for i in range(u_len):
            ui = np.array(matrix_u[:, i]).reshape(-1, 1)
            pwx = pwx + self.euclidean_inner_product(x, ui).ip * ui
        return pwx


if __name__ == "__main__":
    pass
