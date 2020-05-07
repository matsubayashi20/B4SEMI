#!/usr/bin/env python
# coding: utf-8

# In[32]:


def cnt(a):
    try:
        if a < 0:
            raise ZeroDivisionError("0以下ですわ")
        elif a == 100:
            raise ValueError("ちょうど100ですわ")
        elif a > 100:
            raise TypeError("100以上ですわ")
        else:
            return a * 10
    except ZeroDivisionError as u0:  # 0より小さいなら関数を抜けてNoneを返す（コードは止まらない）
        return
    except ValueError as i100:  # ちょうど100なら関数を抜けエラーオブジェクトをかえす（コードは止まらない）
        return i100
    except TypeError as e100:  # 100より大きいならエラーを吐いてプロセスが止まる（コード自体が止まる）
        raise e100

    print("関数の最後よ")


if __name__ == "__main__":
    a = cnt(1)
    print(a, type(a))  # 正常に動作
    b = cnt(-1)
    print(b, type(b))  # エラーをはくけどキャッチして関数を抜け，Noneを返すから止まらない
    c = cnt(100)
    print(c, type(c))  # エラーをはくけどキャッチしてエラーオブジェクトをかえすから止まらない
    d = cnt(101)
    print(d, type(d))  # エラーをはいてプロセスを止める
    e = cnt(2)
    print(e, type(e))  # dでエラーをはいてプロセスがとまったからeは実行されない
