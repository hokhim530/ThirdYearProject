'''
Created on 20 October 2017

@author: Lai Hok Him
'''

import unittest
from src.lll import LLL

class Test(unittest.TestCase):

    def testGSOB(self):
        lll = LLL()
        basis = [[1, 1, 1], [-1, 0, 2], [3, 5, 6]]
        result = lll.GSOB(basis)
        pResult = [[1, 1, 1], [-4/ 3, -1/ 3, 5/ 3], [-6/ 14, 9/ 14, -3/ 14]]
        self.assertListEqual(result, pResult)
        
    def testReduce(self):
        lll = LLL()
        basis = [[15, 23, 11], [46, 15, 3], [32, 1, 1]]
        result = lll.Reduce(basis)
        pResult = [[15, 23, 11], [31, -8, -8], [-14, -14, -2]]
        self.assertListEqual(result, pResult)