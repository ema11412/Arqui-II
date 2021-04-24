# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 11:23:07 2021

@author: Ema
"""

import numpy as np
import time
from threading import *
import random

# Clase principal/ cacheL2
# Preparada para todos los cores.   

class L2cache:
    
    def __init__(self):
        
        self.mem2=[[0,'DI',0,0,0],
                   [1,'DI',0,0,0],
                   [2,'DI',0,0,0],
                   [3,'DI',0,0,0]]
        #0line, 1 state, 2 owner, 3 adress, 4 date
        
        
    #Busca valor en L2
    def search(self, address, mem3):
        for i in self.mem2:
           
            if i[3] == address:
                return 1, self.mem2.index(i)
        return 0,0

    #Obtiene dato de L2    
    def getVal(self, address, core):
        for i in self.mem2:
            if i[3] == address: 
                tmp = i[4]
                i[1] = "DS"
                i[2] = core
                return tmp
            else: 
                return 0
    
    #Escribe en L2
    def write(self, address, data, mem3, core,state):
        
        a,b = self.search(address, mem3)
        if state == 0:
            if a == 1:
                if self.mem2[b][1] == "DS":
                    pass
                elif  self.mem2[b][1] == "DI" or self.mem2[b][1] == "DM":
                    self.wM(address, data, mem3)
                    
                self.mem2[b][4] = data
                self.mem2[b][1] = "DM"
                self.mem2[b][2] = core
            else:
                tmp = random.randrange(4)
                if self.mem2[tmp][1] == "DS":
                    pass
                elif  self.mem2[tmp][1] == "DI" or self.mem2[tmp][1] == "DM":
                    self.wM(address, data, mem3)
                    
                self.mem2[tmp][3] = address
                self.mem2[tmp][4] = data
                self.mem2[tmp][1] = "DM"
                self.mem2[tmp][2] = core
        else:
            if a == 1:
                if self.mem2[b][1] == "DS":
                    pass
                elif  self.mem2[b][1] == "DI" or self.mem2[b][1] == "DM":
                    self.wM(address, data, mem3)
                    
                self.mem2[b][4] = data
                self.mem2[b][1] = "DS"
                self.mem2[b][2] = core
            else:
                tmp = random.randrange(4)
                if self.mem2[tmp][1] == "DS":
                    pass
                elif  self.mem2[tmp][1] == "DI" or self.mem2[tmp][1] == "DM":
                    self.wM(address, data, mem3)
                    
                self.mem2[tmp][3] = address
                self.mem2[tmp][4] = data
                self.mem2[tmp][1] = "DS"
                self.mem2[tmp][2] = core
                
    # Aviso de escritura.        
    def wM(self,address, data, mem3):
        print("Escribo en L2")
            
            