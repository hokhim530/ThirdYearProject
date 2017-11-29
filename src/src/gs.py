'''
Created on 2017¦~10¤ë5¤é

@author: Lai Hok Him
'''

import numpy as np

class GramSchmidt(object):
    
    def GSCoef(self, v1, v2):
        return np.dot(v1, v2) / np.dot(v1, v1)