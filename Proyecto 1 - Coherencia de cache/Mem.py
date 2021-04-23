# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 11:23:15 2021

@author: Ema
"""
#Imports
import numpy as np
import time
import threading



class Mem:

    
    def __init__(self):
        
        self.mem3=[[0," "],
                   [1," "],
                   [2," "],
                   [3," "],
                   [4," "],
                   [5," "],
                   [6," "],
                   [7," "]]
            #address, date
    #Obtiene dato    
    def getVal(self,address):
        return self.mem3[address][1]

    #Actualiza memoria
    def setVal(self,address,data):
        self.mem3[address][1] = data
        