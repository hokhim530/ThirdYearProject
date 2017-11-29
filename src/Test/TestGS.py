'''
Created on 5 October 2017

@author: Lai Hok Him
'''

import unittest
import numpy as np
from src.gs import GramSchmidt

class Test(unittest.TestCase):

    def testGSCoefficients(self):
        gs = GramSchmidt()
        v1 = np.array([5, 8, 7])
        v2 = np.array([6, 4, 9])
        result = gs.GSCoef(v1,v2)
        self.assertEqual(result, 125/ 138, "Coef Fail")