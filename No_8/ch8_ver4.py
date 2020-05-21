# 列ベクトルを行ベクトルに変換する関数(何度か使用する部分があるため関数化)
def is_rowvec(vec):
    if len(vec[0]) == 1: # 列ベクトルを行ベクトルに変換
        row_vec = list(map(list, zip(*vec)))
    else:
        row_vec = vec
    return row_vec


# 課題1
# N個の観測値が格納されたベクトルを入力とし標本平均を求める関数を実装
def sample_mean(vec):
    row_vec = is_rowvec(vec)

    sample_sum = sum(row_vec[0])
    sample_mean = sample_sum / len(row_vec[0])

    return sample_mean

# # vec = [[10],[20],[30],[40]]
# vec = [[10,20,30,40]]
# mean = sample_mean(vec)
# print(mean)

import numpy as np

# 課題2
# N個の観測値が格納されたベクトルを入力とし標本分散を求める関数を実装
def sample_variance(vec_x, vec_y=None):
    row_vec_x = is_rowvec(vec_x)

    # ベクトルが1つだけ渡されたら標本分散を計算
    # if vec_y == None:
    #     mean = sample_mean(row_vec_x)
    #     square_sum = 0
    #     for i in range(len(row_vec_x[0])):
    #         square_sum += (row_vec_x[0][i] - mean) ** 2

    #     sample_variance = square_sum / len(row_vec_x[0])
    #     return sample_variance
    if vec_y == None:
        mean_square = sample_mean(row_vec_x) ** 2
        square_sum = 0
        for i in range(len(row_vec_x[0])):
            square_sum += row_vec_x[0][i] ** 2
        square_mean = square_sum / len(row_vec_x[0])
        sample_variance = square_mean - mean_square
        return sample_variance
    # ベクトルが2つ渡されたら標本共分散を計算
    elif vec_y != None:
        row_vec_y = is_rowvec(vec_y)
        x_mean = sample_mean(row_vec_x)
        y_mean = sample_mean(row_vec_y)
        mul_sum = 0
        for i in range(len(row_vec_x[0])):
            mul_sum += (row_vec_x[0][i] - x_mean) * (row_vec_y[0][i] - y_mean)
        sample_covariance = mul_sum / len(row_vec_x[0])
        return sample_covariance

# vec = [[10],[20],[30],[40]]
# vec = [[10,20,30,40]]
# vec = [[0.001,1.111,2.222,3.333,4.444,5.555,6.666,7.777,8.888,9.999]]
# # vec = [[1.234,2.345,3.456,4.567,5.678,6.789,7.891,8.912,9.123,12.345]]
# vec = [[-37.76, -54.688, 21.018, -48.118, -37.029, 87.627, 18.147, -59.58, 23.107, -62.761]]
# variance = sample_variance(vec)
# print(variance)
# print(np.var(vec))

# vec1 = [[1],[2],[3],[4]]
# vec2 = [[10],[20],[30],[40]]
# # vec1 = [[1,2,3,4]]
# # vec2 = [[10,20,30,40]]
# variance = sample_variance(vec1, vec2)
# print(variance)




# 課題3
# i行目にXiが格納された行列を入力とし標本共分散行列を求める関数を実装
def sample_covariance_matrix(mat):
    cov_mat = []

    for i in range(len(mat)):
        cov_mat_tmp = [] # 標本共分散行列の行方向の成分をまとめておくtmpリスト
        for j in range(len(mat)):
            vec_x = mat[i]
            vec_y = mat[j]
            cov_mat_tmp.append(sample_variance([vec_x], [vec_y]))
            # cov_mat_tmp.append(round(sample_variance([vec_x], [vec_y]), 7))
        cov_mat.append(cov_mat_tmp)

    return cov_mat

# mat = [[80,20,50],[100,30,80],[50,50,50]]
# cov_mat = sample_covariance_matrix(mat)
# print(cov_mat)



import numpy as np
import math
from scipy.linalg import eig, eigh, inv

# 課題4
# 行列を転置する関数
def transpose_matrix(mat):
    transposed_mat = list(map(list, zip(*mat)))
    return transposed_mat

def matrix_transition(A):
    # 結果を入れる変数を用意
    result = []

    # 入力された行列のサイズを確認
    A_column = len(A)
    A_row = len(A[0])

    # 転置を行う（エルミート転置）
    for i in range(A_row):
        tmp = []
        for j in range(A_column):
            tmp.append(A[j][i].conjugate())
        result.append(tmp)
    return result


# i行目にXiが格納された行列を白色化する行列Λ^(-1/2)U^(T)を求める関数を実装
def whitening_matrix(mat):
    cov_mat = sample_covariance_matrix(mat)

    if cov_mat == matrix_transition(cov_mat):
        eValues, eVectors = eigh(cov_mat)
        indx = eValues.argsort()[::-1]
        eValues = eValues[indx]
        eVectors = eVectors[:,indx]
    else:
        eValues, eVectors = eig(cov_mat)
        indx = eValues.argsort()[::-1]
        eValues = eValues[indx]
        eVectors = eVectors[:,indx]

    # eValues, eVectors = eig(cov_mat)
    # indx = eValues.argsort()[::-1]
    # eValues = eValues[indx]
    # eVectors = eVectors[:,indx]

    # eValues_sqrtInv = [] # 固有値の平方根と逆数をとった値を入れる配列
    # for i in range(len(eValues)):
    #     eValues_sqrtInv.append(1 / math.sqrt(eValues.real[i]))
    # eValues_sqrtInv_mat = np.diag(eValues_sqrtInv)
    # # print(eValues_sqrtInv_mat)

    eValues_sqrt = [] # 固有値の平方根をとった値を入れる配列
    for i in range(len(eValues)):
        eValues_sqrt.append(math.sqrt(eValues.real[i]))
    eValues_sqrt_mat = np.diag(eValues_sqrt)
    eValues_sqrtInv = inv(eValues_sqrt_mat)
    # print(eValues_sqrtInv)

    eVectors_trans = transpose_matrix(eVectors)

    # whitening_mat = np.dot(eValues_sqrtInv_mat, eVectors_trans)
    whitening_mat = np.dot(eValues_sqrtInv, eVectors_trans)

    return whitening_mat


# # mat = [[50,50,40,60],[70,80,80,90]]
# # mat = [[1,1,2,3,4],[3,4,3,5,5],[4,2,3,2,5]]
# mat = [[11,1,4],[1,14,6],[4,6,67]]


# # # print(sample_covariance_matrix(mat))
# # matlen = len(mat[0])
# whi_mat = whitening_matrix(mat)

# print(whi_mat)
# # print(eig(mat))
# print('----------------')
# z = np.dot(whi_mat,mat)
# print(z)
# print('----------------')

# print(sample_covariance_matrix(z.tolist()))
