'''
Created on 20 October 2017

@author: Lai Hok Him
'''
import numpy as np
from src.gs import GramSchmidt

class LLLAlgorithm(object):
    
    def Swap(self, basis, i, j):
        basis[i], basis[j] = basis[j], basis[i]
        return basis
    
    def LovaszCondition(self, basis, i):
        gs= GramSchmidt()
        oBasis = gs.GS(basis, i + 1)
        v1 = np.dot(oBasis[i], oBasis[i])
        v2 = ((3/4) - np.square(gs.GSCoef(oBasis[i - 1], basis[i]))) * np.dot(oBasis[i - 1], oBasis[i - 1])
        if v1 < v2:
            basis = self.Swap(basis, i, i -1)
        return basis
    
    def Reduce(self, basis, i):
        gs= GramSchmidt()
        for j in range(i):
            v1 = np.asarray(basis[i])
            coef = gs.GSCoef(np.asarray(basis[j]), v1)
            if coef <= 0.5:
                break
            v2 = np.around(gs.GSCoef(np.asarray(basis[j]), v1))
            result = v1 - gs.Multi(np.asarray(basis[j]), v2)
            basis[i] = result.tolist()
        return basis

    def LLL(self, matrix):
        vList = matrix.tolist().copy()
        temp1 =vList.copy()
        temp2 =vList.copy()
        count = 1
        while True:
            for i in range(1, len(vList)):
                self.Reduce(vList, i)
                self.LovaszCondition(vList, i)
            if (count%2) == 0:
                temp2 = vList.copy()
                count = count + 1
            else:
                temp1 = vList.copy()
                count = count + 1
            if temp1 == temp2:
                break
        return np.asmatrix(vList)