#!/usr/bin/env python
# coding: utf-8


import numpy as np
import math
from itertools import product


def euclidean_inner_product(vector1, vector2):
    # numpy配列変換
    vecx = np.array(vector1)
    vecy = np.array(vector2)

    # エラー処理
    if not vecx.shape == vecy.shape:
        raise ValueError("ベクトルのサイズが違います")

    vecx = np.array(vector1).reshape(-1, 1)
    vecy = np.array(vector2).reshape(-1, 1)

    # 共役をとる
    conj_y = vecy.conj()

    # 成分ごとに加算
    tmp = [vx[0] * cy[0] for (vx, cy) in zip(vecx, conj_y)]
    res = sum(tmp)

    # 直交性の判断
    is_orthogonal = round(res, 7) == 0

    return res, is_orthogonal


def n_norm(vector, n=2):
    # 強制的に縦ベクトルに変換
    vec = np.array(vector).reshape(-1, 1)

    # 計算
    tmp = [abs(v[0]) ** n for v in vec]

    # 全部加算してn乗根
    res = sum(tmp)**(1 / n)

    return res


def cosine_similarity(vector1, vector2):
    # 内積計算
    ip_xy, __ = euclidean_inner_product(vector1, vector2)

    # ノルム計算
    norm_x = n_norm(vector1)
    norm_y = n_norm(vector2)

    if norm_x == 0 or norm_y == 0:
        raise ZeroDivisionError("ノルムが0です")

    # コサイン類似度計算
    res = ip_xy.real / (norm_x * norm_y)

    return res


def unitary_matrix(matrix):

    uni = np.array(matrix)

    her_mat = np.conjugate(uni.T)
    ide_mat = np.dot(uni, her_mat)
    ide_mat2 = np.identity(len(uni))

    is_unitary = True
    for i, j in product(range(len(uni)), repeat=2):
        is_unitary &= round(ide_mat[i][j] - ide_mat2[i][j], 7) == 0

    return is_unitary


def Gram_Schmidt_orthonormalization(matrix):
    # numpy基底行列matrix_u
    matrix_u = np.matrix(matrix)
    u_len = len(matrix_u)
    u_N = matrix_u.shape[0]

    for i in range(u_len):
        is_norm_zero = n_norm(matrix_u[:, i])
        if is_norm_zero == 0:
            raise ZeroDivisionError("ノルムが0です")
        else:
            pass

    # 第一手順
    u0 = matrix_u[:, 0]  # 一つ目の基底を縦ベクトルで取得
    print("u0", u0)
    v0 = u0/(n_norm(u0))
    matrix_v = np.matrix(v0)
    print("v0", matrix_v[:, 0])

    # 第一手順 i = 2 , 3 , ... N
    for i in range(1, u_len):
        ui = matrix_u[:, i]
        ui_var = np.zeros((u_N, 1))
        for j in range(i):
            ui_var += matrix_v[:, j] * euclidean_inner_product(ui, matrix_v[:, j])[0]
        vi = (ui-ui_var)/(n_norm(ui-ui_var))
        matrix_v = np.hstack((matrix_v, vi))
    return matrix_v


def orthogonal_projection(matrix, vector):
    x = np.array(vector).reshape(-1, 1)
    matrix_u = Gram_Schmidt_orthonormalization(matrix)
    u_len = len(matrix_u)
    pwx = np.zeros((u_len, 1))

    for i in range(u_len):
        ui = np.array(matrix_u[:, i]).reshape(-1, 1)
        pwx += euclidean_inner_product(x, ui)[0] * ui
    return pwx


if __name__ == "__main__":
    pass
