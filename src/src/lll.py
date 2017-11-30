'''
Created on 20 October 2017

@author: Lai Hok Him
'''
from src.gs import GramSchmidt

class LLL(object):
    
    def GSOB(self, basis):
        gs = GramSchmidt()
        return gs.GS(basis)