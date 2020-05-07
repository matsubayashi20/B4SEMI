# import pprint # 縦行列を見やすく表示するため
import math # sqrt()使用
# from decimal import *


# 課題1 ベクトルの転置を求める関数
def my_transpose_vector(vector):
    transposed_vector = list(map(list, zip(*vector)))

    # 引数vectorのlistをzip()で成分ごとに分解して結合させることで行列が入れ替わった
    # tupleを受け取る．map()のfunctionとしてlist()を設定し，戻ってきたmapオブジェクトを
    # listに変換してtransplsed_vectorに代入している．

    # transpose_vector = [list(x) for x in zip(*vector)] # ←↑どちらでも動作可
    return transposed_vector

# matrix = [
#     [11, 12, 13, 14],
#     [21, 22, 23, 24],
#     [31, 32, 33, 34]
# ]

# vector = [[11, 12, 13, 14]] # 横ベクトル
# vector = [
#     [11],
#     [21],
#     [31],
#     [41]] # 縦ベクトル

# transpose_vector = my_transpose_vector(vector)

# print(vector)
# #pprint.pprint(vector, width=20)
# print(transpose_vector)






# 課題2-1 ベクトルの和を求める関数
def my_vector_add(vector_x, vector_y):
    rnd_vector_sum_1d = []
    if len(vector_x[0]) == 1: # 縦ベクトルの場合
        trs_vector_x = list(map(list, zip(*vector_x))) # 転置（縦 → 横）
        trs_vector_y = list(map(list, zip(*vector_y)))
        vector_sum_tmp = [x + y for (x, y) in zip(*trs_vector_x, *trs_vector_y)] # リストの要素同士を足し算
        for i in range(len(vector_sum_tmp)):
            if isinstance(vector_sum_tmp[i], complex): # 複素数の場合
                rnd_vector_sum_1d.append(complex(round(vector_sum_tmp[i].real, 13), round(vector_sum_tmp[i].imag, 13)))
            else: # 実数の場合
                rnd_vector_sum_1d.append(round(vector_sum_tmp[i], 13)) # 小数点以下15桁に丸める
        tmp_2d = [rnd_vector_sum_1d] # リストを横ベクトルに変換
        vector_sum = list(map(list, zip(*tmp_2d))) # 転置（横 → 縦）
    else: # if len(vector_x[0]) != 1:に相当，横ベクトルの場合
        vector_sum_1d = [x + y for (x, y) in zip(vector_x[0], vector_y[0])] # リストの要素同士を足し算
        for i in range(len(vector_sum_1d)):
            if isinstance(vector_sum_1d[i], complex): # 複素数の場合
                rnd_vector_sum_1d.append(complex(round(vector_sum_1d[i].real, 13), round(vector_sum_1d[i].imag, 13)))
            else: # 実数の場合
                rnd_vector_sum_1d.append(round(vector_sum_1d[i], 13)) # 小数点以下15桁に丸める
        vector_sum = [rnd_vector_sum_1d] # リストを横ベクトルに変換
    return vector_sum

# vector_x = [[7+5j, -6+1j]]
# vector_y = [[2-8j, 3-9j]]


# vector_x = [[1, -3]]
# vector_y = [[-1, 5]]

# vector_x = [
#     [1],
#     [-3]]
# vector_y = [
#     [-1],
#     [5]]

# vector_sum = my_vector_add(vector_x, vector_y)
# print(vector_sum)



# 課題2-2 ベクトルのスカラ積を求める関数
def my_vector_multiply(coef, vector):
    rnd_vector_pro_1d = []
    if len(vector[0]) == 1: # 縦ベクトルの場合
        trs_vector = list(map(list, zip(*vector))) # 転置（縦 → 横）
        vector_pro_tmp = list(map(lambda mul: coef * mul, trs_vector[0])) # リストの各要素にスカラを乗ずる
        for i in range(len(vector_pro_tmp)):
            if isinstance(vector_pro_tmp[i], complex): # 複素数の場合
                rnd_vector_pro_1d.append(complex(round(vector_pro_tmp[i].real, 13), round(vector_pro_tmp[i].imag, 13)))
            else: # 実数の場合
                rnd_vector_pro_1d.append(round(vector_pro_tmp[i], 13)) # 小数点以下15桁に丸める
        tmp_2d = [rnd_vector_pro_1d] # リストを横ベクトルに変換
        vector_pro = list(map(list, zip(*tmp_2d))) # 転置（横 → 縦）
    else: # if len(vector[0]) != 1:に相当，横ベクトルの場合
        vector_pro_1d = list(map(lambda mul: coef * mul, vector[0])) # リストの各要素にスカラを乗ずる
        for i in range(len(vector_pro_1d)):
            if isinstance(vector_pro_1d[i], complex): # 複素数の場合
                rnd_vector_pro_1d.append(complex(round(vector_pro_1d[i].real, 13), round(vector_pro_1d[i].imag, 13)))
            else: # 実数の場合
                rnd_vector_pro_1d.append(round(vector_pro_1d[i], 13)) # 小数点以下15桁に丸める
        vector_pro = [rnd_vector_pro_1d] # リストを横ベクトルに変換
    return vector_pro

# coef = 3
# vector = [[1, -3]]
# vector = [[-1, 5]]

# vector = [
#     [1],
#     [-3]]

# vector = [
#     [-1],
#     [5]]

# coef = 1+1j
# vector = [[2-8j, 3-9j]]

# vector_pro = my_vector_multiply(coef, vector)
# print(vector_pro)


# # 2x-3y
# vec_x = [[1], [-3]]
# tmp_y = [[-1], [5]]
# vec_y = vector_multiply(3,tmp_y)
# SumMul = my_vector_add(my_vector_multiply(2,vec_x), my_vector_multiply(-3,vec_y))
# print(SumMul)






# 課題3 ベクトルの長さを求める関数
def my_vector_length(vector):
    tmp = [] # 各成分の2乗を入れておくリスト
    if len(vector[0]) == 1: # 縦ベクトルの場合
        trs_vector = list(map(list, zip(*vector))) # 転置（縦 → 横）
        vct_list = trs_vector[0] # 横ベクトルをリストに変換
    else: # len(vector[0]) != 1:に相当，横ベクトルの場合
        vct_list = vector[0] # 横ベクトルをリストに変換
    for i in range(len(vct_list)): # リストの長さだけ処理をする
        if isinstance(vct_list[i], complex): # 複素数の場合
            tmp.append(vct_list[i].real ** 2 + vct_list[i].imag ** 2) # 2乗を計算
        else: # 実数の場合
            tmp.append(vct_list[i] ** 2) # 2乗を計算
    vct_length = math.sqrt(sum(tmp)) # 2乗した値の合計値の平方根をとる
    return round(vct_length, 13) # 小数点以下15桁に丸める

# vector = [[1,4,3,5,6]]
# vector = [[1+4j,3,5+6j]]
# vector = [[8.18, -9.51, 19.7, -17.75, 0.9]]

# vector = [[1],[4],[3],[5],[6]]
# vector = [[1+4j],[3],[5+6j]]

# vector_length = my_vector_length(vector)
# print(vector_length)






# 課題4 ベクトルの写像を求める関数
def my_vector_map(matrix, vector):
    if len(matrix[0]) == len(vector): # 行列の行とベクトルの成分数が揃っている場合
        trs_vector = list(map(list, zip(*vector))) # 転置（縦 → 横）
        tmp = [] # 行列の行とベクトルの，同じインデックス同士の積を入れておくリスト
        tmp_1d = [] # tmpの和を入れておくリスト
        rnd_tmp_1d = []
        for i in range(len(matrix)):
            tmp.append([x * y for (x, y) in zip(matrix[i], trs_vector[0])]) # 行列の行とベクトルの，同じインデックス同士の積
            tmp_1d.append(sum(tmp[i])) # 同じインデックス同士の積の和
        for i in range(len(tmp_1d)):
            if isinstance(tmp_1d[i], complex): # 複素数の場合
                rnd_tmp_1d.append(complex(round(tmp_1d[i].real, 13), round(tmp_1d[i].imag, 13)))
            else: # 実数の場合
                rnd_tmp_1d.append(round(tmp_1d[i], 13)) # 小数点以下15桁に丸める
        tmp_2d = [rnd_tmp_1d] # リストを横ベクトルに変換
        vector_mapping = list(map(list, zip(*tmp_2d))) # 転置（横 → 縦）
    else: # 行列の行とベクトルの成分数が揃っていない場合
        raise Exception("cannot calculate")
        # vector_mapping = None
        # print("cannot calculate")
    return vector_mapping

# matrix = [
#     [1,0,2],
#     [0,1,1],
# ]

# vector = [[1],[2],[1]]

# matrix = [
#     [2,1],
#     [1,3],
# ]

# vector = [[2],[-1]]

# matrix = [[1+3j, 3-2j, -2], [2+1j, -3j, 1-2j]]
# vector = [[3+2j],[-1j],[4]]

# matrix = [[1.1, 1.2, -1.3, 1.4],
#         [-2.1, 2.2, -2.3, 2.4],
#         [3.1, -3.2, 3.3, 3.4]]
# vector = [[4.1], [9.8], [0.2], [5.7]]

# vector_mapping = my_vector_map(matrix, vector)
# print(vector_mapping)





# 課題5 正方行列かどうか判定する関数
def my_is_SquareMatrix(matrix):
    if len(matrix) == len(matrix[0]): # 行列の行数と列数が一致しているかどうか判定
        print("square matrix")
        return True
    else:
        print("rectangular matrix")
        return False

# matrix = [
#     [11, 12, 13],
#     [21, 22, 23],
#     [31, 32, 33]
# ]

# matrix = [
#     [11, 12, 13, 14],
#     [21, 22, 23, 24],
#     [31, 32, 33, 34]
# ]

# square_or_rect = my_is_SquareMatrix(matrix)
# print(square_or_rect)
