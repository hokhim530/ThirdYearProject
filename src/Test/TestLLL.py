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