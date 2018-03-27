'''
Created on 5 October 2017

@author: Lai Hok Him
'''
from __future__ import division
import unittest
import numpy as np
import numpy.testing as npt
import sys
sys.path.append('../')
from src import gs as gsp

class Test(unittest.TestCase):

    def testGSCoefficients(self):
        gs = gsp.GramSchmidt()
        v1 = np.array([1, 1, 1])
        v2 = np.array([-1, 0, 2])
        result = gs.GSCoef(v1, v2)
        self.assertEqual(result, 1 / 3, "Coef Fail")

    def testMulti(self):
        gs = gsp.GramSchmidt()
        v1 = np.array([1, 1, 1])
        result = gs.Multi(v1, 1 / 3)
        npt.assert_array_equal(result, np.array([1 / 3, 1 / 3, 1 / 3]))

    def testGSproj(self):
        gs = gsp.GramSchmidt()
        v1 = np.array([1, 1, 1])
        v2 = np.array([-1, 0, 2])
        result = gs.GSproj(v1, v2)
        npt.assert_array_equal(result, np.array([1 / 3, 1 / 3, 1 / 3]))

    def testGS(self):
        gs = gsp.GramSchmidt()
        basis = [[1, 1, 1], [-1, 0, 2], [3, 5, 6]]
        result = gs.GS(basis, 3)
        pResult = [[1, 1, 1], [-4 / 3, -1 / 3, 5 / 3],
                   [-6 / 14, 9 / 14, -3 / 14]]
        np.testing.assert_array_almost_equal(result, pResult, 7)

if __name__ == "__main__":
    unittest.main()