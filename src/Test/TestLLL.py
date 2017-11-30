'''
Created on 20 October 2017

@author: Lai Hok Him
'''

import unittest
from src.lll import LLLAlgorithm

class Test(unittest.TestCase):
        
    def testSwap(self):
        lll = LLLAlgorithm()
        basis = [[15, 23, 11], [31, -8, -8], [-14, -14, -2]]
        result = lll.Swap(basis, 1, 2)
        pResult = [[15, 23, 11], [-14, -14, -2], [31, -8, -8]]
        self.assertListEqual(result, pResult)
        
    def testLovaszCondition(self):
        lll = LLLAlgorithm()
        basis = [[15, 23, 11], [1, 9, 9], [31, -8, -8]]
        result = lll.LovaszCondition(basis, 1)
        pResult = [[1, 9, 9], [15, 23, 11], [31, -8, -8]]
        self.assertListEqual(result, pResult)
        
    def testReduce(self):
        lll = LLLAlgorithm()
        basis = [[1, 9, 9], [15, 23, 11], [31, -8, -8]]
        result = lll.Reduce(basis, 1)
        pResult = [[1, 9, 9], [13, 5, -7], [31, -8, -8]]
        self.assertListEqual(result, pResult)