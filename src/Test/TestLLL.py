'''
Created on 20 October 2017

@author: Lai Hok Him
'''
from __future__ import division
import unittest
import numpy as np
import sys
sys.path.append('../')
from src import lll as llla

class Test(unittest.TestCase):

    def testSwap(self):
        lll = llla.LLLAlgorithm()
        basis = [[15, 23, 11], [31, -8, -8], [-14, -14, -2]]
        result = lll.Swap(basis, 1, 2)
        pResult = [[15, 23, 11], [-14, -14, -2], [31, -8, -8]]
        self.assertListEqual(result, pResult)

    def testLovaszCondition(self):
        lll = llla.LLLAlgorithm()
        basis = [[15, 23, 11], [1, 9, 9], [31, -8, -8]]
        result = lll.LovaszCondition(basis, 1)
        pResult = [[1, 9, 9], [15, 23, 11], [31, -8, -8]]
        self.assertListEqual(result, pResult)

    def testReduce(self):
        lll = llla.LLLAlgorithm()
        basis = [[1, 9, 9], [13, 5, -7], [31, -8, -8]]
        result = lll.Reduce(basis, 2)
        pResult = [[1, 9, 9], [13, 5, -7], [6, -9, 15]]
        self.assertListEqual(result, pResult)

    def testLLL(self):
        lll = llla.LLLAlgorithm()
        matrix = np.matrix([[15, 23, 11], [46, 15, 3], [32, 1, 1]])
        result = lll.LLL(matrix)
        pResult = np.matrix([[1, 9, 9], [13, 5, -7], [6, -9, 15]])
        np.testing.assert_array_equal(result, pResult)

if __name__ == "__main__":
    unittest.main()