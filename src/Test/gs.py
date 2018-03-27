'''
Created on 5 October 2017

@author: Lai Hok Him
'''
from __future__ import division
import numpy as np

class GramSchmidt(object):
    
    '''
    Calculate the Gram-Schmidt Coefficient
    '''
    def GSCoef(self, v1, v2):
            return np.dot(v1, v2) / np.dot(v1, v1)

    '''
    Multiple function
    '''
    def Multi(self, v1, coef):
        return v1.dot(coef)

    '''
    Calculate the Gram-Schmidt projection
    '''
    def GSproj(self, v1, v2):
        return self.Multi(v1, self.GSCoef(v1, v2))

    '''
    Main body of the Gram-Schmidt process
    '''
    def GS(self, basis, v):
        oBasis = []
        for i in range(v):
            if i != 0:
                v2 = np.asarray(basis[i])
                result = v2
                for j in range(i):
                    v1 = np.asarray(oBasis[i - j - 1])
                    result = np.subtract(result, self.GSproj(v1, v2))
            else:
                result = np.asarray(basis[0])
            oBasis.append(result.tolist())
        return oBasis
