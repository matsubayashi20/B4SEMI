import sympy
import numpy as np
import math
from scipy.linalg import null_space



# 行ベクトルを列ベクトルに変換する関数(何度か使用する部分があるため関数化)
def is_colvec(vec):
    if type(vec[0]) == list:
        col_vec = vec
    else: # 行ベクトルを列ベクトルに変換
        col_vec = list(map(list, zip(vec)))
    return col_vec



# 課題1
# N個の観測値が格納されたベクトルを入力とし標本平均を求める関数を実装
def sample_mean(vec):
    col_vec = is_colvec(vec)

    sample_sum = sum(map(sum, col_vec))
    sample_mean = sample_sum / len(col_vec)

    return sample_mean


# 課題2
# N個の観測値が格納されたベクトルを入力とし標本分散を求める関数を実装
def sample_variance(vec_x, vec_y=None):
    col_vec_x = is_colvec(vec_x)

    # ベクトルが1つだけ渡されたら標本分散を計算
    if vec_y == None:
        mean = sample_mean(col_vec_x)
        square_sum = 0
        for i in range(len(col_vec_x)):
            square_sum += (col_vec_x[i][0] - mean) ** 2
        sample_variance = square_sum / len(col_vec_x)
        return sample_variance
    # ベクトルが2つ渡されたら標本共分散を計算
    elif vec_y != None:
        col_vec_y = is_colvec(vec_y)
        x_mean = sample_mean(col_vec_x)
        y_mean = sample_mean(col_vec_y)
        mul_sum = 0
        for i in range(len(col_vec_x)):
            mul_sum += (col_vec_x[i][0] - x_mean) * (col_vec_y[i][0] - y_mean)
        sample_covariance = mul_sum / len(col_vec_x)
        return sample_covariance


# 課題3
# i行目にXiが格納された行列を入力とし標本共分散行列を求める関数を実装
def sample_covariance_matrix(mat):
    cov_mat = []

    for i in range(len(mat)):
        cov_mat_tmp = [] # 標本共分散行列の行方向の成分をまとめておくtmpリスト
        for j in range(len(mat)):
            vec_x = mat[i]
            vec_y = mat[j]
            cov_mat_tmp.append(sample_variance(vec_x, vec_y))
        cov_mat.append(cov_mat_tmp)

    return cov_mat


# 課題4
# 行列を転置する関数
def transpose_matrix(mat):
    transposed_mat = list(map(list, zip(*mat)))
    return transposed_mat

# i行目にXiが格納された行列を白色化する行列Λ^(-1/2)U^(T)を求める関数を実装
def whitening_matrix(mat):
    cov_mat = sample_covariance_matrix(mat)

    eValues, eVectors = np.linalg.eig(cov_mat)
    indx = eValues.argsort()[::-1]
    eValues = eValues[indx]
    eVectors = eVectors[:,indx]

    eValues_sqrtInv = [] # 固有値の平方根と逆数をとった値を入れる配列
    for i in range(len(eValues)):
        eValues_sqrtInv.append(1 / math.sqrt(eValues[i]))
    eValues_sqrtInv_mat = np.diag(eValues_sqrtInv)

    eVectors_trans = transpose_matrix(eVectors)

    whitening_mat = np.dot(eValues_sqrtInv_mat, eVectors_trans)

    return whitening_mat


# mat = [[50,50,40,60],[70,80,80,90]]
# # print(sample_covariance_matrix(mat))
# matlen = len(mat[0])
# whi_mat = whitening_matrix(mat)

# print(whi_mat)
# # print(np.linalg.eig(mat))
# print('----------------')
# z = np.dot(whi_mat,mat)
# print(z)
# print('----------------')
# z_tmp = z[0]
# z_1_mean = sample_mean(z_tmp)
# print(z_1_mean)
