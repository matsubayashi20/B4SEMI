# 縦ベクトルを横ベクトルに変換する関数（何度か使用する部分があるため関数化）
def is_rowvec(vec):
    if len(vec[0]) == 1:
        row_vec = list(map(list, zip(*vec)))
    else:
        row_vec = vec
    return row_vec


# 課題1
# N 個の観測値が格納されたベクトルを入力とし標本平均を求める関数を実装
def sample_mean(vec):
    # 縦ベクトルを横ベクトルに変換
    row_vec = is_rowvec(vec)

    # 標本平均を計算
    sample_sum = sum(row_vec[0])
    sample_mean = sample_sum / len(row_vec[0])

    return sample_mean


# 課題2
# N 個の観測値が格納されたベクトルを入力とし標本分散を求める関数を実装
def sample_variance(vec_x, vec_y=None):
    # 縦ベクトルを横ベクトルに変換
    row_vec_x = is_rowvec(vec_x)

    if vec_y == None: # ベクトルが 1 つだけ渡されたら標本分散を計算
        mean = sample_mean(row_vec_x)
        square_sum = 0
        for i in range(len(row_vec_x[0])):
            square_sum += (row_vec_x[0][i] - mean) ** 2
        sample_variance = square_sum / len(row_vec_x[0])
        return sample_variance
    elif vec_y != None: # ベクトルが 2 つ渡されたら標本共分散を計算
        row_vec_y = is_rowvec(vec_y)
        x_mean = sample_mean(row_vec_x)
        y_mean = sample_mean(row_vec_y)
        mul_sum = 0
        for i in range(len(row_vec_x[0])):
            mul_sum += (row_vec_x[0][i] - x_mean) * (row_vec_y[0][i] - y_mean)
        sample_covariance = mul_sum / len(row_vec_x[0])
        return sample_covariance


# 課題3
# i行目にXiが格納された行列を入力とし標本共分散行列を求める関数を実装
def sample_covariance_matrix(mat):
    cov_mat = []
    for i in range(len(mat)):
        cov_mat_tmp = []
        for j in range(len(mat)):
            vec_x = mat[i]
            vec_y = mat[j]
            cov_mat_tmp.append(sample_variance([vec_x], [vec_y]))
        cov_mat.append(cov_mat_tmp)

    return cov_mat



import numpy as np # argsort(), diag(), dot() の関数用
import math # 平方根の計算用
from scipy.linalg import eigh, inv

# 行列を転置する関数
def transpose_matrix(mat):
    transposed_mat = list(map(list, zip(*mat)))
    return transposed_mat


# 第 3 回の実装プログラムから引用
# エルミート転置を求める関数
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


# 課題4
# i行目にXiが格納された行列を白色化する行列Λ^(-1/2)U^(T)を求める関数を実装
def whitening_matrix(mat):
    # 標本分散行列を計算
    cov_mat = sample_covariance_matrix(mat)

    # 固有値と固有ベクトルを計算
    eValues, eVectors = eigh(cov_mat)
    
    # 固有ベクトルの 1 行目が負の場合，その固有ベクトル全体に (-1) を掛けて計算
    for row in range(len(eVectors[0])):
        if eVectors[0][row] < 0:
            for col in range(len(eVectors)):
                eVectors[col][row] *= -1
        else:
            pass
    
    # 固有値に0が含まれる場合はエラー処理
    if any([i == 0 for i in np.round(eValues, decimals = 7)]):
        raise ValueError
        
    # 固有値と固有ベクトルを降順に入れ替える
    indx = eValues.argsort()[::-1]
    eValues = eValues[indx]
    eVectors = eVectors[:,indx]

    # 固有値の平方根をとって対角に並べ，逆行列を計算
    eValues_sqrt = []
    for i in range(len(eValues)):
        eValues_sqrt.append(math.sqrt(eValues.real[i]))
    eValues_sqrt_mat = np.diag(eValues_sqrt)
    eValues_sqrtInv = inv(eValues_sqrt_mat)
    
    # 固有ベクトルを並べた行列を転置
    eVectors_trans = transpose_matrix(eVectors)

    # Λ^(-1/2)U^(T)を計算
    whitening_mat = np.dot(eValues_sqrtInv, eVectors_trans)

    return whitening_mat