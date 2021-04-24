# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 11:22:58 2021

@author: Ema
"""

#Imports
import threading
import numpy as np
import random
from Mem import *
import time


# Clase principal/ cacheL1
# Preparada para un core 
class L1cache:
    mem1=[[0,'I',0,0],
          [1,'I',0,0]]
    
    core = "Px"

    #Inicialozador
    def __init__(self,core): 
        self.mem1=[[0,'I',0,0],
                   [1,'I',0,0]]
                  #line, state, address date
        self.core = core
    
    #Escritura
    def write(self, address, data, mem3,L2cache,state):

        time.sleep(0.2)
        a,b = self.check(address)
       
        if state ==0:
            if a == 1: 
                if self.mem1[b][1] == "M":
                    pass
                elif  self.mem1[b][1] == "I" or self.mem1[b][1] == "S":
                    print("Actualizo dato L1", self.core)                  
                    
                self.mem1[b][3] = data
                self.mem1[b][1] = "M"
                mem3.setVal(address, data)
                self.wL2(address, data, L2cache,mem3,0)
            else:
                tmp = random.randrange(2)
                if self.mem1[tmp][1] == "M":
                    pass
                elif  self.mem1[tmp][1] == "I" or self.mem1[tmp][1] == "S":
                    self.wM(address, data, mem3, L2cache)                    
                    
                self.mem1[tmp][2] = address
                self.mem1[tmp][3] = data
                self.mem1[tmp][1] = "M"
                mem3.setVal(address, data)
                self.wL2(address, data, L2cache,mem3,0)
        else:
            if a == 1:                
                    
                self.mem1[b][3] = data
                self.mem1[b][1] = "S"
                
                #mem3.setVal(address, data)
                self.wL2(address, data, L2cache,mem3,1)
            else:
                tmp = random.randrange(2)             
                self.mem1[tmp][2] = address
                self.mem1[tmp][3] = data
                self.mem1[tmp][1] = "S"
                
                #mem3.setVal(address, data)
                self.wL2(address, data, L2cache,mem3,1)

    #Lectura     
    def read(self, address, mem3, L2cache):

        self.verFm( address, L2cache,mem3)

        time.sleep(0.2)
        a,b = self.check(address)
        
        if a == 1:
            if self.mem1[b][1] == "S":
                pass
            else:


                val = mem3.getVal(address)
                self.wL2(address, val, L2cache,mem3,0)
                self.write(address, val, mem3, L2cache,1)
                

                
        else:
            tmp = self.bL2(address, mem3, L2cache)
            
            if tmp == 0:
                val = mem3.getVal(address)
                #print("valor es:  ", val)
                self.wL2(address, val, L2cache,mem3,0)
                self.write(address, val, mem3, L2cache,1)
                
            else:
                val = L2cache.getVal(address, self.core)
                #print("valor es:  ", val)
                self.write(address, val, mem3, L2cache,1)

            
    #Check de los datos en L1    
    def check(self, address):

        if int(self.mem1[0][2]) == address:
            return 1,0
        elif int(self.mem1[1][2]) == address:
            return 1,1
        else:
            return 0,0

    #Busca valores en L2
    def bL2(self, address, mem3, L2cache):
        var,s = L2cache.search(address, mem3)
        return var

    #Avisa de WM    
    def wM(self, address, data, mem3, L2cache):
        print("writeMiss")
    
    #Escribe en L2
    def wL2(self, address,data, L2cache,mem3,state):
        L2cache.write(address, data, mem3, self.core,state)
        
    #Verifica la integridad de los datos    
    def verFm(self, address, L2cache,mem3):
        var,s = L2cache.search(address, mem3)
        if var == 1:
            state = L2cache.mem2[s][1]
            _,ind = self.check(address)
            if state == "DM":
                self.mem1[ind][1] = "I"
            
        else: 
            return 0
        