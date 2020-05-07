# -*- coding: utf-8 -*-
#
# test_ch_one.py
#
# Created by Kosuke FUKUMORI on 2020/03/17
#

from unittest import TestCase
from NSIP.ch_one import my_plus

class Test_ch_one(TestCase):   # 名前はなんでもいい
    def test_my_plus(self):   # test**で始まる関数のみテストされる
        self.assertEqual(my_plus(1,2), 3)
        self.assertEqual(my_plus(1,3), 4)
        self.assertEqual(my_plus(2,3), 5)