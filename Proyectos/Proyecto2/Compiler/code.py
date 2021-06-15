import re
from constants_code import *

file_ = open("data.txt", "r")
i = 1
ii = 0

def appendToMif():
    HEADER = ['DEPTH = 32;', 'WIDTH = 8;', 'ADDRESS_RADIX = DEC;', 'DATA_RADIX = HEX;', 'CONTENT', 'BEGIN']

    for i in HEADER:
        writeFile(i + '\n')

def checkLength_32(data):
    if (len(data) != 32):
        print('-------ERROR------', len(data))
    else:
        newLine = hex(int(data, 2))[2:].zfill(8)
        print(newLine)
        global ii
        mif_line = str(ii) + ' : ' + newLine + ';\n'
        writeFile(mif_line)
        ii += 1


def getConstast(data, fill = 16):
    try:
        return variables[data]
    except Exception as e:
        # print(e)
        return bin(int(data))[2:].zfill(fill)

def writeFile(data):
    vFile = open(f'mif.txt', 'a')

    vFile.write(data)

    vFile.close()

def addEnd():
    vFile = open(f'mif.txt', 'a')
    vFile.write('END;')
    vFile.close()

vFile = open(f'mif.txt', 'w')
vFile.truncate()
vFile.close()
appendToMif()

for line in file_:
    array = line.split(" ")
    Mnemonic = array[0]

    if(Mnemonic[0] == '.'):
        checkLength_32('00000000000000000000000000000000')

    # R type
    elif(Mnemonic == 'ADD'):
        Rd = resisters[array[1].replace("\n", "")]
        Rs1 = resisters[array[2].replace("\n", "")]
        Rs2 = resisters[array[3].replace("\n", "")]

        D = r_type[Mnemonic] 
        opcode = D['opcode']
        aluop = D['aluop']

        newLine = f'{opcode}{Rd}{Rs1}{Rs2}{aluop}000000000'.replace("\n", "")
        
        checkLength_32(newLine)

    elif(Mnemonic == 'SUB'):
        Rd = resisters[array[1].replace("\n", "")]
        Rs1 = resisters[array[2].replace("\n", "")]
        Rs2 = resisters[array[3].replace("\n", "")]
        
        D = r_type[Mnemonic] 
        opcode = D['opcode']
        aluop = D['aluop']

        newLine = f'{opcode}{Rd}{Rs1}{Rs2}{aluop}000000000'.replace("\n", "")

        checkLength_32(newLine)

    elif(Mnemonic == 'MUL'):
        Rd = resisters[array[1].replace("\n", "")]
        Rs1 = resisters[array[2].replace("\n", "")]
        Rs2 = resisters[array[3].replace("\n", "")]
        
        D = r_type[Mnemonic] 
        opcode = D['opcode']
        aluop = D['aluop']

        newLine = f'{opcode}{Rd}{Rs1}{Rs2}{aluop}000000000'.replace("\n", "")

        checkLength_32(newLine)

    elif(Mnemonic == 'MOV'):
        Rd = resisters[array[1].replace("\n", "")]
        Rs1 = resisters[array[2].replace("\n", "")]

        D = r_type[Mnemonic] 
        opcode = D['opcode']

        newLine = f'{opcode}{Rd}{Rs1}00000{aluop}000000000'.replace("\n", "")
        
        checkLength_32(newLine)

    # I type
    elif(Mnemonic == 'ADDI'):
        Rd = resisters[array[1].replace("\n", "")]
        Rs1 = resisters[array[2].replace("\n", "")]
        Imm = getConstast(array[3].replace("\n", ""))

        D = i_type[Mnemonic] 
        opcode = D['opcode']
        
        newLine = f'{opcode}{Rd}{Rs1}{Imm}0'.replace("\n", "")

        checkLength_32(newLine)

    elif(Mnemonic == 'SUBI'):
        Rd = resisters[array[1].replace("\n", "")]
        Rs1 = resisters[array[2].replace("\n", "")]
        Imm = getConstast(array[3].replace("\n", ""))

        D = i_type[Mnemonic] 
        opcode = D['opcode']

        newLine = f'{opcode}{Rd}{Rs1}{Imm}0'.replace("\n", "")

        checkLength_32(newLine)

    elif(Mnemonic == 'BLE'):
        Rs1 = resisters[array[1].replace("\n", "")]
        Rs2 = resisters[array[2].replace("\n", "")]
        label = getConstast(array[3].replace("\n", ""))

        D = i_type[Mnemonic] 
        opcode = D['opcode']

        newLine = f'{opcode}{Rd}{Rs1}{Imm}0'.replace("\n", "")

        checkLength_32(newLine)

    elif(Mnemonic == 'DIVI'):
        Rd = resisters[array[1].replace("\n", "")]
        Rs1 = resisters[array[2].replace("\n", "")]
        Imm = getConstast(array[3].replace("\n", ""))

        D = i_type[Mnemonic] 
        opcode = D['opcode']

        newLine = f'{opcode}{Rd}{Rs1}{Imm}0'.replace("\n", "")

        checkLength_32(newLine)

    elif(Mnemonic == 'MULI'):
        Rd = resisters[array[1].replace("\n", "")]
        Rs = resisters[array[2].replace("\n", "")]
        Imm = getConstast(array[3].replace("\n", ""))

        D = i_type[Mnemonic] 
        opcode = D['opcode']

        newLine = f'{opcode}{Rd}{Rs1}{Imm}0'.replace("\n", "")
        
        checkLength_32(newLine)

    elif(Mnemonic == 'MOVI'):
        Rd = resisters[array[1].replace("\n", "")]
        Imm = getConstast(array[2].replace("\n", ""))

        D = i_type[Mnemonic] 
        opcode = D['opcode']

        tempImn = bin(int(Imm, 10))[2:]

        newLine = f'{opcode}{Rd}00000{Imm}0'.replace("\n", "")
        
        checkLength_32(newLine)

    # J type
    elif(Mnemonic == 'JMP'):
        label = getConstast(array[1].replace("\n", ""), 20)

        D = j_type[Mnemonic] 
        opcode = D['opcode']

        newLine = f'{opcode}0000000{label}'.replace("\n", "")

        checkLength_32(newLine)

    # V type
    elif(Mnemonic == 'VLD'):
        Vd = resisters[array[1].replace("\n", "")]
        Rs1 = resisters[array[2].replace("\n", "")]

        D = v_type[Mnemonic] 
        opcode = D['opcode'].replace("\n", "")

        newLine = f'{opcode}{Vd}{Rs1}00000000000000000'.replace("\n", "")

        checkLength_32(newLine)

    elif(Mnemonic == 'VST'):
        Vd = resisters[array[1].replace("\n", "")]
        VRs = resisters[array[2].replace("\n", "")]

        D = v_type[Mnemonic] 
        opcode = D['opcode'].replace("\n", "")

        newLine = f'{opcode}{Vd}{VRs}00000000000000000'.replace("\n", "")

        checkLength_32(newLine)

    elif(Mnemonic == 'VOPG'):
        VR2 = resisters[array[1]]
        VR1 = resisters[array[2]]
        VR14 = resisters[array[3].replace("\n", "")]

        D = v_type[Mnemonic] 
        opcode = D['opcode']
        aluop = D['aluop']

        newLine = f'{opcode}{Vd}{VR1}{VR2}{aluop}000000000'.replace("\n", "")

        checkLength_32(newLine)

    elif(Mnemonic == 'VOPA'):
        VR3 = resisters[array[1].replace("\n", "")]
        VR1 = resisters[array[2].replace("\n", "")]
        VR2 = resisters[array[3].replace("\n", "")]

        D = v_type[Mnemonic] 
        opcode = D['opcode']
        aluop = D['aluop']

        newLine = f'{opcode}{Vd}{VR1}{VR2}{aluop}000000000'.replace("\n", "")

        checkLength_32(newLine)

    else:
        print('------------------------ERROR------------------------------------')

addEnd()