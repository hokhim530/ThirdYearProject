'''
Created on 2017�~10��5��

@author: Lai Hok Him
'''

import numpy as np

class GramSchmidt(object):
    
    def GSCoef(self, v1, v2):
        return np.dot(v1, v2) / np.dot(v1, v1)