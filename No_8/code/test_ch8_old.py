#!/usr/bin/env python
# coding: utf-8

import numpy as np
from numpy.testing import assert_array_equal
import unittest
from ch8_ver7 import sample_mean, sample_variance, sample_covariance_matrix, whitening_matrix

#課題1 N個の観測値が格納されたベクトルを入力とし標本平均を求める関数を実装
class TestSampleMean(unittest.TestCase):
    def test_sample_mean(self):
        exp = 72
        act = sample_mean([[90, 80, 40, 60, 90]])
        self.assertAlmostEqual(exp, act)

        exp = -15.0037
        act = sample_mean([[-37.76, -54.688, 21.018, -48.118, -37.029, 87.627, 18.147, -59.58, 23.107, -62.761]])
        self.assertAlmostEqual(exp, act)

        exp = -5.9776
        act = sample_mean([[-25.348, -54, -26.429, 87, -70.035, 90.534, -65.264, 90.276, -29, -22.427, 84, -63.724, -73, -90.247, 78]])
        self.assertAlmostEqual(exp, act)


#課題2 N個の観測値が格納されたベクトルを入力とし標本分散を求める関数を実装
class TestSampleVariance(unittest.TestCase):
    def test_sample_variance(self):
        exp = 376
        act = sample_variance([[90, 80, 40, 60, 90]])
        self.assertAlmostEqual(exp, act)

        exp = 24.278
        act = sample_variance([[0.5,3.6,-0.6,-9.8,-4.4,6.1,5.1,7.4,0.3,2.8]])
        self.assertAlmostEqual(exp, act)

        exp = 32.99705956
        act = sample_variance([[4.95,-5,7.75,5.48,-7,-0.98,-8.4,1.95,-0.86,-9,-4.43,6.46,4.82,8,1.62]])
        self.assertAlmostEqual(exp, act)


#課題3 i行目にXiが格納された行列を入力とし標本共分散行列を求める関数を実装
class TestSampleCovarianceMatrix(unittest.TestCase):
    def test_sample_covariance_matrix(self):
        exp = [[1400/3, 500/3], [500/3, 200/3]]
        act = sample_covariance_matrix([[40, 80, 90], [80, 90, 100]])
        for i in range(2):
            for j in range(2):
                self.assertAlmostEqual(exp[i][j], act[i][j])

        exp = [[1073.639325,-623.61545,531.78615], [-623.61545,621.700925,-567.472375], [531.78615,-567.472375,931.01145]]
        act = sample_covariance_matrix([[-45.82,-25.35,-32.05,39.32], [28.12,-14.17,33.94,-22.47], [-43.96,37.21,2.99,21.92]])
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(exp[i][j], act[i][j])

        exp = [[4.428,-4.912,-3.756,-2.472],[-4.912,14.944,-3.176,10.196],[-3.756,-3.176,14.5504,-7.6968],[-2.472,10.196,-7.6968,10.1976]]
        act = sample_covariance_matrix([[-1,4.3,-1.1,-0.7,-1],[-5.6,-8,-3.2,3.4,-1.6],[7,-3.6,-2,-2.6,0.4],[-3.1,-1.1,4,5.6,1.7]])
        for i in range(4):
            for j in range(4):
                self.assertAlmostEqual(exp[i][j], act[i][j])

#課題4 i行目にXiが格納された行列を白色化する行列Λ^(-1/2)U^(T)を求める関数を実装
class TestWhiteningMatrix(unittest.TestCase):
    def test_whitening_matrix(self):
        exp = np.array([[ 0.04095854983226044 , 0.0148290403118912], [0.1353602496881495 , -0.37387176887728213]])
        act = whitening_matrix([[40, 80, 90], [80, 90, 100]])

        for i in range(exp.shape[0]):
            for j in range(exp.shape[1]):
                self.assertAlmostEqual(exp[i][j], act[i][j])

        exp = np.array([[0.014245668189244708, -0.011313215676737294, 0.01262021673696023], [0.03135494731512368, 0.0015038591483654345, -0.03404527050563938], [0.03259724693983638, 0.07839949834966449, 0.033484438405276276]])
        act = whitening_matrix([[-45.82,-25.35,-32.05,39.32], [28.12,-14.17,33.94,-22.47], [-43.96,37.21,2.99,21.92]])
        for i in range(exp.shape[0]):
            for j in range(exp.shape[1]):
                self.assertAlmostEqual(exp[i][j], act[i][j])

        exp = np.array([[0.023342910587869133, -0.12165384962747014, 0.08899363123730368, -0.1132771806067438], [0.12387241888532186, -0.11709565785890363, -0.1941336043291668, -0.0012356773195523584], [0.5338130178481921, 0.5127973559490143, 0.03394566591585277, -0.41404698243612936], [2.7978562593515828, -0.6532117590551376, 2.1603112740043433, 2.975266304140435]])
        act = whitening_matrix([[-1,4.3,-1.1,-0.7,-1],[-5.6,-8,-3.2,3.4,-1.6],[7,-3.6,-2,-2.6,0.4],[-3.1,-1.1,4,5.6,1.7]])
        for i in range(exp.shape[0]):
            for j in range(exp.shape[1]):
                self.assertAlmostEqual(exp[i][j], act[i][j])

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored', '-v'], exit=False)
