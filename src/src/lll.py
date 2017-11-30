'''
Created on 20 October 2017

@author: Lai Hok Him
'''

import numpy as np
from src.gs import GramSchmidt

class LLL(object):
    
    def GSOB(self, basis):
        gs = GramSchmidt()
        return gs.GS(basis)
    
    def Reduce(self, basis):
        rBasis = []
        for i in range(len(basis)):
            v1 = np.asarray(basis[i])
            if i != 0:
                rv = v1
                for j in range(i):
                    v2 = np.asarray(rBasis[j])
                    rv = np.subtract(rv, v2)
            else:
                rv = v1
            rBasis.append(rv.tolist())
            print(rv)
            print(rBasis)
        return rBasis