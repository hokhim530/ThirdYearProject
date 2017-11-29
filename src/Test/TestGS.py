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
        v1 = np.array([5, 8, 7])
        v2 = np.array([6, 4, 9])
        result = gs.GSCoef(v1,v2)
        self.assertEqual(result, 125/ 138, "Coef Fail")
        
    def testMulti(self):
        gs = GramSchmidt()
        v1 = np.array([5, 8, 7])
        result = gs.Multi(v1, 5)
        npt.assert_array_equal(result, np.array([25, 40, 35]))
        
    def testGSproj(self):
        gs = GramSchmidt()
        v1 = np.array([5, 8, 7])
        v2 = np.array([6, 4, 9])
        result = gs.GSproj(v1, v2)
        npt.assert_array_equal(result, np.array([625/ 138, 1000/138, 875/138]))