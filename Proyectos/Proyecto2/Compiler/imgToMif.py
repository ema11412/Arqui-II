def writeFile(data):
    vFile = open(f'imageMif.txt', 'a')

    vFile.write(data)

    vFile.close()

def addEnd():
    vFile = open(f'imageMif.txt', 'a')
    vFile.write('END;')
    vFile.close()

def appendToMif():
    HEADER = ['DEPTH = 32;', 'WIDTH = 8;', 'ADDRESS_RADIX = DEC;', 'DATA_RADIX = HEX;', 'CONTENT', 'BEGIN']

    for i in HEADER:
        writeFile(i + '\n')

vFile = open(f'imageMif.txt', 'w')
vFile.truncate()
vFile.close()
appendToMif()

with open('./Output/image.txt', 'r') as f:

    i=0
    for linea in f:
        writeFile(str(i) + ' : '+ '00' + linea.replace("\n", ";\n"))
        i+=1

addEnd()


