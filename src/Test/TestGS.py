'''
Created on 5 October 2017

@author: Lai Hok Him
'''

import unittest
import numpy as np
import numpy.testing as npt
from src.gs import GramSchmidt

class Test(unittest.TestCase):

    def testGSCoefficients(self):
        gs = GramSchmidt()
        v1 = np.array([1, 1, 1])
        v2 = np.array([-1, 0, 2])
        result = gs.GSCoef(v1,v2)
        self.assertEqual(result, 1/ 3, "Coef Fail")
        
    def testMulti(self):
        gs = GramSchmidt()
        v1 = np.array([1, 1, 1])
        result = gs.Multi(v1, 1/ 3)
        npt.assert_array_equal(result, np.array([1/ 3, 1/ 3, 1/ 3]))
        
    def testGSproj(self):
        gs = GramSchmidt()
        v1 = np.array([1, 1, 1])
        v2 = np.array([-1, 0, 2])
        result = gs.GSproj(v1, v2)
        npt.assert_array_equal(result, np.array([1/ 3, 1/ 3, 1/ 3]))
        
    def testGS(self):
        gs = GramSchmidt()
        v1 = [[1, 1, 1], [-1, 0, 2], [3, 5, 6]]
        result = gs.GS(v1)
        pResult = [[1, 1, 1], [-4/ 3, -1/ 3, 5/ 3], [-6/ 14, 9/ 14, -3/ 14]]
        self.assertListEqual(result, pResult)
        print(result)