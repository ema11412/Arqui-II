# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 11:59:29 2021

@author: Ema
"""

import numpy as np



class InstructGen:
    def __init__(self):
        self.generator = np.random.default_rng()

    def generateInstructionForProcessor(self):

        
        instructionType = round(self.generator.uniform(0, 2))

        if (instructionType == 0):
            instruction = self.generateCalc()
        address = round(self.generator.uniform(0, 7))
        if (instructionType == 1):
            instruction = self.generateRead( address)
        if (instructionType == 2):
            data = round(self.generator.uniform(0, 65535))
            instruction = self.generateWrite( address, data)
        return instruction


    def generateCalc(self):
            return "CALC"

    def generateRead(self, address):
        address = self.decimalToBinary(address)

        return "READ " + address

    def generateWrite(self, address, data):
        address = self.decimalToBinary(address)
        data = self.decimalToHexadecimal(data)

        return "WRITE " + address + "-" + data

    def decimalToBinary(self, decimalNumber):
        result = bin(decimalNumber).replace("0b", "")
        rLen = len(result)
        while (rLen != 3):
            result = "0" + result
            rLen += 1

        return result

    def decimalToHexadecimal(self, hexadecimalNumber):
        result = hex(hexadecimalNumber).replace("0x", "")
        rLen = len(result)
        while (rLen != 4):
            result = "0" + result
            rLen += 1

        return result
    
    

