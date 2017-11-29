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