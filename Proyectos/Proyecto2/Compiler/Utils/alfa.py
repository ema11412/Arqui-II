import re
import random
import numpy as np

from PIL import Image
from constants import FORMAT
from Utils.image import decToHex
        




def createAlfaImage(alfaFileName, gradientFileName, imageFileName, ain):
    linesGradientFile = []
    linesImageFile = []

    with open(gradientFileName, encoding='utf8') as gradientFile:
        for line in gradientFile:
            linesGradientFile.append(line)

    with open(imageFileName, encoding='utf8') as imageFile:
        for line in imageFile:
            linesImageFile.append(line)

    alfaFile = open(alfaFileName, 'w')
    alfaFile.truncate()

    count = 0
    for lineImage in linesImageFile:
        #print(lineImage, "##############################\n")
        R_Gradient, G_Gradient, B_Gradient = re.findall(
            '..', linesGradientFile[count])
        
        R_Image, G_Image, B_Image = re.findall('..', lineImage)

        count += 1

        R_out = __newPixelValue(R_Gradient, R_Image, ain)
        G_out = __newPixelValue(G_Gradient, G_Image, ain)
        B_out = __newPixelValue(B_Gradient, B_Image, ain)

        result = f'{R_out:03}{G_out:03}{B_out:03}'
        result =  decToHex(result)
        alfaFile.write(result + FORMAT)

    alfaFile.close()
    print('Alfa File Success')


def __newPixelValue(Pin1, Pin2, ain):
    return (int(Pin1,16) * (100 - ain) + int(Pin2,16) * ain ) // 100


def loadImage(alfaPath, alfaFileName, width, height):
    rowCount = 0
    columnCount = 0
    data = np.zeros((height, width, 3), dtype=np.uint8)

    with open(alfaFileName, encoding='utf8') as alfaFile:
        for line in alfaFile:
            if(columnCount >= width):
                rowCount += 1
                columnCount = 0

            #print(line, "****\n")

            R_Alfa, G_Alfa, B_Alfa = re.findall('..', line)

            newPixel = [int(R_Alfa,16), int(G_Alfa,16), int(B_Alfa,16)]

            data[rowCount, columnCount] = newPixel  # red patch in upper left
            columnCount += 1

    img = Image.fromarray(data, 'RGB')
    img.save(alfaPath)
    # img.show()
