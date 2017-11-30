'''
Created on 20 October 2017

@author: Lai Hok Him
'''

class LLLAlgorithm(object):
    
    def Swap(self, basis, i, j):
        basis[i], basis[j] = basis[j], basis[i]
        return basis