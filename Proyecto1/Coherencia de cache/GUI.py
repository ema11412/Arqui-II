# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 11:31:04 2021

@author: Ema
"""
#Imports
from threading import *
import PySimpleGUI as sg

#Seleccion de tema
sg.theme('DarkBlue4') 

#Pantalla principal
FRAME = [[sg.Text('Procesadores', size=(30,1),pad=(500,0))],
         
         [ sg.Text('---------------------------------------------------------------------', size=(30,1),pad=(0,0),justification='center'),
           sg.Text('---------------------------------------------------------------------', size=(30,1),pad=(0,0),justification='center'),
           sg.Text('---------------------------------------------------------------------', size=(30,1),pad=(0,0),justification='center'),
           sg.Text('---------------------------------------------------------------------', size=(30,1),pad=(0,0),justification='center'),
           sg.Text('---------------------------------------------------------------------', size=(30,1),pad=(0,0),justification='center')],

          [sg.Text('Cache L1_0', size=(30,1),pad=(55,0)),
          sg.Text('CacheL1_1', size=(30,1),pad=(10,0)),
          sg.Text('CacheL1_2', size=(30,1),pad=(10,0)),
          sg.Text('Cachel1_3', size=(30,1),pad=(10,0))],

          [sg.Text('Instruction-0', size=(30,1),pad=(55,0),key='P0'),
          sg.Text('Instruction-1', size=(30,1),pad=(10,0),key='P1'),
          sg.Text('Instruction-2', size=(30,1),pad=(10,0),key='P2'),
          sg.Text('Instruction-3', size=(30,1),pad=(10,0),key='P3')],
          
          
          
          [sg.Text('[0, I, 0, 0]', size=(30,1),pad=(55,0),key='C10'),
          sg.Text('[0, I, 0, 0]', size=(30,1),pad=(14,0),key='C20'),
          sg.Text('[0, I, 0, 0]', size=(30,1),pad=(7,0),key='C30'),
          sg.Text('[0, I, 0, 0]', size=(30,1),pad=(10,0),key='C40')],
          
          [sg.Text('[1, I, 0, 0]', size=(30,1),pad=(55,0),key='C11'),
          sg.Text('[1, I, 0, 0]', size=(30,1),pad=(14,0),key='C21'),
          sg.Text('[1, I, 0, 0]', size=(30,1),pad=(7,0),key='C31'),
          sg.Text('[1, I, 0, 0]', size=(30,1),pad=(10,0),key='C41')],


          [ sg.Text('---------------------------------------------------------------------', size=(30,1),pad=(0,0),justification='center'),
           sg.Text('---------------------------------------------------------------------', size=(30,1),pad=(0,0),justification='center'),
           sg.Text('---------------------------------------------------------------------', size=(30,1),pad=(0,0),justification='center'),
           sg.Text('---------------------------------------------------------------------', size=(30,1),pad=(0,0),justification='center'),
           sg.Text('---------------------------------------------------------------------', size=(30,1),pad=(0,0),justification='center')],
          
          [[sg.Text('Cache L2', size=(30,1),pad=(500,0))]],
          [sg.Text('[0, DI, 0, 0]', size=(30,1),pad=(500,0),key='L20')],
          [sg.Text('[1, DI, 0, 0]', size=(30,1),pad=(500,0),key='L21')],
          [sg.Text('[2, DI, 0, 0]', size=(30,1),pad=(500,0),key='L22')],
          [sg.Text('[3, DI, 0, 0]', size=(30,1),pad=(500,0),key='L23')],


          [ sg.Text('---------------------------------------------------------------------', size=(30,1),pad=(0,0),justification='center'),
           sg.Text('---------------------------------------------------------------------', size=(30,1),pad=(0,0),justification='center'),
           sg.Text('---------------------------------------------------------------------', size=(30,1),pad=(0,0),justification='center'),
           sg.Text('---------------------------------------------------------------------', size=(30,1),pad=(0,0),justification='center'),
           sg.Text('---------------------------------------------------------------------', size=(30,1),pad=(0,0),justification='center')],


          [[sg.Text('Memoria principal', size=(30,1),pad=(480,0))]],
          [sg.Text('[0 , " "]', size=(30,1),pad=(510,0),key='M0')],
          [sg.Text('[1 , " "]', size=(30,1),pad=(510,0),key='M1')],
          [sg.Text('[2 , " "]', size=(30,1),pad=(510,0),key='M2')],
          [sg.Text('[3 , " "]', size=(30,1),pad=(510,0),key='M3')],
          [sg.Text('[4 , " "]', size=(30,1),pad=(510,0),key='M4')],
          [sg.Text('[5 , " "]', size=(30,1),pad=(510,0),key='M5')],
          [sg.Text('[6 , " "]', size=(30,1),pad=(510,0),key='M6')],
          [sg.Text('[7 , " "]', size=(30,1),pad=(510,0),key='M7')]
          ]
        
#Titulo
window = sg.Window('COHERENCIA DE CACHE', FRAME)

#Run de la GUI
def runGUI():
    while True:
        event, values = window.read()
        if event == 'Close' or event == sg.WIN_CLOSED:
            break
        
    window.close()

#Actualizacion de datos.
def updateWindow(val,key):
    window[key].update(val)

