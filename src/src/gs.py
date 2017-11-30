'''
Created on 5 October 2017

@author: Lai Hok Him
'''

import numpy as np


class GramSchmidt(object):
    
    def GSCoef(self, v1, v2):
            return np.dot(v1, v2) / np.dot(v1, v1)
    
    def Multi(self, v1, coef):
        return v1.dot(coef)
    
    def GSproj(self, v1, v2):
        return self.Multi(v1, self.GSCoef(v1, v2))
    
    def GS(self, basis):
        oBasis = []
        for i in range(len(basis)):
            if i != 0:
                v2 = np.asarray(basis[i])
                result = v2
                for j in range(i):
                    v1 = np.asarray(oBasis[i - j - 1])
                    result = np.subtract(result, self.GSproj(v1, v2))
                    print(result)
            else:
                result = np.asarray(basis[0])
            oBasis.append(result.tolist())
        return oBasis