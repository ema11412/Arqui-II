# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 11:15:29 2021

@author: Ema
"""

#Imports
import threading
from instGen import *
from L1 import *
from L2 import *
from Mem import *
import time

from GUI import *



#Objeto generador de instrucciones.        
ins = InstructGen()


#iNSTANCIA MEMORIA PRINCIPAL
m =  Mem()

    
#Instancia de memorias L1

cacheL1_0 = L1cache("P0")
cacheL1_1 = L1cache("P1")
cacheL1_2 = L1cache("P2")
cacheL1_3 = L1cache("P3")


# Intancia memoria L2
cacheL2 = L2cache()

        

#Loop para cores

#son 4 cores con un generador de instrucciones general para cada 1

def mLoopC0():

    v = ins.generateInstructionForProcessor()
    print(v)
    time.sleep(2)
    updateWindow(v,'P0')
    if v[0] == "R":
        numero = int(v[5:], 2)
        cacheL1_0.read(numero,m,cacheL2)
        

        updateWindow((cacheL1_0.mem1)[0],'C10')
        updateWindow((cacheL1_0.mem1)[1],'C11')
        updateWindow((cacheL2.mem2)[0],'L20')
        updateWindow((cacheL2.mem2)[1],'L21')
        updateWindow((cacheL2.mem2)[2],'L22')
        updateWindow((cacheL2.mem2)[3],'L23') 
        
        updateWindow((m.mem3)[0],'M0')
        updateWindow((m.mem3)[1],'M1')
        updateWindow((m.mem3)[2],'M2')
        updateWindow((m.mem3)[3],'M3')
        updateWindow((m.mem3)[4],'M4')
        updateWindow((m.mem3)[5],'M5')
        updateWindow((m.mem3)[6],'M6')
        updateWindow((m.mem3)[7],'M7')
        
        time.sleep(2)
    
    elif v[0] == "W":
    
        numero = int(v[6:9], 2)
        data = v[10:]
        cacheL1_0.write(numero,data,m,cacheL2,0)
        
        
        updateWindow((cacheL1_0.mem1)[0],'C10')
        updateWindow((cacheL1_0.mem1)[1],'C11')
        updateWindow((cacheL2.mem2)[0],'L20')
        updateWindow((cacheL2.mem2)[1],'L21')
        updateWindow((cacheL2.mem2)[2],'L22')
        updateWindow((cacheL2.mem2)[3],'L23') 
        
        updateWindow((m.mem3)[0],'M0')
        updateWindow((m.mem3)[1],'M1')
        updateWindow((m.mem3)[2],'M2')
        updateWindow((m.mem3)[3],'M3')
        updateWindow((m.mem3)[4],'M4')
        updateWindow((m.mem3)[5],'M5')
        updateWindow((m.mem3)[6],'M6')
        updateWindow((m.mem3)[7],'M7')
        
        time.sleep(3)

        
    elif v[0] =="C":
        
        print(v)
        time.sleep(1)

def mLoopC1():


    v = ins.generateInstructionForProcessor()
    print(v)
    time.sleep(2)
    updateWindow(v,'P1')
    if v[0] == "R":
        numero = int(v[5:], 2)
        cacheL1_1.read(numero,m,cacheL2)
        

        updateWindow((cacheL1_1.mem1)[0],'C20')
        updateWindow((cacheL1_1.mem1)[1],'C21')
        updateWindow((cacheL2.mem2)[0],'L20')
        updateWindow((cacheL2.mem2)[1],'L21')
        updateWindow((cacheL2.mem2)[2],'L22')
        updateWindow((cacheL2.mem2)[3],'L23') 
        
        updateWindow((m.mem3)[0],'M0')
        updateWindow((m.mem3)[1],'M1')
        updateWindow((m.mem3)[2],'M2')
        updateWindow((m.mem3)[3],'M3')
        updateWindow((m.mem3)[4],'M4')
        updateWindow((m.mem3)[5],'M5')
        updateWindow((m.mem3)[6],'M6')
        updateWindow((m.mem3)[7],'M7')
        
        time.sleep(2)
    
    elif v[0] == "W":
    
        numero = int(v[6:9], 2)
        data = v[10:]
        cacheL1_1.write(numero,data,m,cacheL2,0)
        

        updateWindow((cacheL1_1.mem1)[0],'C20')
        updateWindow((cacheL1_1.mem1)[1],'C21')
        updateWindow((cacheL2.mem2)[0],'L20')
        updateWindow((cacheL2.mem2)[1],'L21')
        updateWindow((cacheL2.mem2)[2],'L22')
        updateWindow((cacheL2.mem2)[3],'L23') 
        
        updateWindow((m.mem3)[0],'M0')
        updateWindow((m.mem3)[1],'M1')
        updateWindow((m.mem3)[2],'M2')
        updateWindow((m.mem3)[3],'M3')
        updateWindow((m.mem3)[4],'M4')
        updateWindow((m.mem3)[5],'M5')
        updateWindow((m.mem3)[6],'M6')
        updateWindow((m.mem3)[7],'M7')
        
        time.sleep(3)
    
    elif v[0] =="C":
        
        print(v)
        time.sleep(1)

def mLoopC2():


    v = ins.generateInstructionForProcessor()
    print(v)
    time.sleep(2)
    updateWindow(v,'P2')
    
    if v[0] == "R":
        numero = int(v[5:], 2)
        cacheL1_2.read(numero,m,cacheL2)
        

        updateWindow((cacheL1_2.mem1)[0],'C30')
        updateWindow((cacheL1_2.mem1)[1],'C31')
        updateWindow((cacheL2.mem2)[0],'L20')
        updateWindow((cacheL2.mem2)[1],'L21')
        updateWindow((cacheL2.mem2)[2],'L22')
        updateWindow((cacheL2.mem2)[3],'L23') 
        
        updateWindow((m.mem3)[0],'M0')
        updateWindow((m.mem3)[1],'M1')
        updateWindow((m.mem3)[2],'M2')
        updateWindow((m.mem3)[3],'M3')
        updateWindow((m.mem3)[4],'M4')
        updateWindow((m.mem3)[5],'M5')
        updateWindow((m.mem3)[6],'M6')
        updateWindow((m.mem3)[7],'M7')
        
        time.sleep(2)
    
    elif v[0] == "W":
    
        numero = int(v[6:9], 2)
        data = v[10:]
        cacheL1_2.write(numero,data,m,cacheL2,0)
        
        
        updateWindow((cacheL1_2.mem1)[0],'C30')
        updateWindow((cacheL1_2.mem1)[1],'C31')
        updateWindow((cacheL2.mem2)[0],'L20')
        updateWindow((cacheL2.mem2)[1],'L21')
        updateWindow((cacheL2.mem2)[2],'L22')
        updateWindow((cacheL2.mem2)[3],'L23') 
        
        updateWindow((m.mem3)[0],'M0')
        updateWindow((m.mem3)[1],'M1')
        updateWindow((m.mem3)[2],'M2')
        updateWindow((m.mem3)[3],'M3')
        updateWindow((m.mem3)[4],'M4')
        updateWindow((m.mem3)[5],'M5')
        updateWindow((m.mem3)[6],'M6')
        updateWindow((m.mem3)[7],'M7')
        time.sleep(3)
    
    elif v[0] =="C":
        
        print(v)
        time.sleep(1)
        
def mLoopC3():


    v = ins.generateInstructionForProcessor()
    print(v)
    time.sleep(2)
    updateWindow(v,'P3')
    if v[0] == "R":
        numero = int(v[5:], 2)
        cacheL1_3.read(numero,m,cacheL2)
        
        updateWindow((cacheL1_3.mem1)[0],'C40')
        updateWindow((cacheL1_3.mem1)[1],'C41')
        updateWindow((cacheL2.mem2)[0],'L20')
        updateWindow((cacheL2.mem2)[1],'L21')
        updateWindow((cacheL2.mem2)[2],'L22')
        updateWindow((cacheL2.mem2)[3],'L23') 
        
        updateWindow((m.mem3)[0],'M0')
        updateWindow((m.mem3)[1],'M1')
        updateWindow((m.mem3)[2],'M2')
        updateWindow((m.mem3)[3],'M3')
        updateWindow((m.mem3)[4],'M4')
        updateWindow((m.mem3)[5],'M5')
        updateWindow((m.mem3)[6],'M6')
        updateWindow((m.mem3)[7],'M7')
        
        

        
        
        time.sleep(2)
    
    elif v[0] == "W":
    
        numero = int(v[6:9], 2)
        data = v[10:]
        cacheL1_3.write(numero,data,m,cacheL2,0)

        updateWindow((cacheL1_3.mem1)[0],'C40')
        updateWindow((cacheL1_3.mem1)[1],'C41')
        updateWindow((cacheL2.mem2)[0],'L20')
        updateWindow((cacheL2.mem2)[1],'L21')
        updateWindow((cacheL2.mem2)[2],'L22')
        updateWindow((cacheL2.mem2)[3],'L23') 
        
        updateWindow((m.mem3)[0],'M0')
        updateWindow((m.mem3)[1],'M1')
        updateWindow((m.mem3)[2],'M2')
        updateWindow((m.mem3)[3],'M3')
        updateWindow((m.mem3)[4],'M4')
        updateWindow((m.mem3)[5],'M5')
        updateWindow((m.mem3)[6],'M6')
        updateWindow((m.mem3)[7],'M7')
        
        time.sleep(3)
    
    elif v[0] =="C":
        
        print(v)
        time.sleep(1)       




def finalMain():
   # c0 = threading.Thread(target=mLoopC0, args=())
   # c1 = threading.Thread(target=mLoopC1, args=())
   # c2 = threading.Thread(target=mLoopC2, args=())
   # c3 = threading.Thread(target=mLoopC3, args=())
    print("------------------------------")
    print("1 - Infinito")
    print("2 - Paso a paso")
    print("------------------------------")
    var = input("Eleccion: ")

    if var == "1":
        while True:    
  

            c0 = threading.Thread(target=mLoopC0,name='cpu0')
            c0.start()
            #c0.join()

            c1 = threading.Thread(target=mLoopC1,name='cpu1')
            c1.start()
            #c1.join()

            c2 = threading.Thread(target=mLoopC2,name='cpu2')
            c2.start()
            #c2.join()

            c3 = threading.Thread(target=mLoopC3,name='cpu3')
            c3.start()
            #c3.join()

            c0.join()  
            c1.join()  
            c2.join()  
            c3.join()     

    elif var == "2":
        while True:    
  

            c0 = threading.Thread(target=mLoopC0,name='cpu0')
            c0.start()
            #c0.join() 

            c1 = threading.Thread(target=mLoopC1,name='cpu1')
            c1.start()
            #c1.join()

            c2 = threading.Thread(target=mLoopC2,name='cpu2')
            c2.start()
            #c2.join()

            c3 = threading.Thread(target=mLoopC3,name='cpu3')
            c3.start()
            #c3.join() 

            c0.join()  
            c1.join()  
            c2.join()  
            c3.join()   
             
              
              
                
    

            input("------------------------------ENTER para seguir------------------------------") 
    else:
        
        return 0

#Run de interfaz..
G  = threading.Thread(target=runGUI, args=())
G.start()
time.sleep(2)

#MainLOOP
finalMain()




