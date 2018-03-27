'''
Created on 20 October 2017

@author: Lai Hok Him
'''
from __future__ import division
import numpy as np
from src.gs import GramSchmidt

class LLLAlgorithm(object):

    '''
    Swap the value between basis in LLL
    '''
    def Swap(self, basis, i, j):
        basis[i], basis[j] = basis[j], basis[i]
        return basis

    '''
    Perform Lovasz Condition in LLL
    '''
    def LovaszCondition(self, basis, i):
        gs = GramSchmidt()
        oBasis = gs.GS(basis, i + 1)
        v1 = np.dot(oBasis[i], oBasis[i])
        v2 = (((3/4) - np.square(gs.GSCoef(oBasis[i - 1], basis[i]))) *
              np.dot(oBasis[i - 1], oBasis[i - 1]))
        if v1 < v2:
            basis = self.Swap(basis, i, i - 1)
        return basis
    
    '''
    Lattice reduction
    '''
    def Reduce(self, basis, i):
        gs = GramSchmidt()
        for j in range(i):
            v1 = np.asarray(basis[i])
            coef = gs.GSCoef(np.asarray(basis[j]), v1)
            if coef <= 0.5:
                break
            v2 = np.around(gs.GSCoef(np.asarray(basis[j]), v1))
            result = v1 - gs.Multi(np.asarray(basis[j]), v2)
            basis[i] = result.tolist()
        return basis
    
    '''
    Main body of LLL algorithm
    '''
    def LLL(self, lattice):
        if type(lattice) == list:
            vList = lattice.copy()
        else:
            vList = lattice.tolist().copy()
        temp1 = vList.copy()
        temp2 = vList.copy()
        count = 1
        '''
        The loop will do the reduction until finished reduction
        '''
        while True:
            for i in range(1, len(vList)):
                self.Reduce(vList, i)
                self.LovaszCondition(vList, i)
            if (count % 2) == 0:
                temp2 = vList.copy()
                count = count + 1
            else:
                temp1 = vList.copy()
                count = count + 1
            if temp1 == temp2:
                break
        return np.asmatrix(vList)

if __name__ == '__main__':
    lll = LLLAlgorithm()
    lattice = input(
        'please input lattice in matrix form:\
        (example:[[15, 23, 11], [46, 15, 3], [32, 1, 1]])\n')
    matrix = eval(lattice)
    print(lll.LLL(lattice))