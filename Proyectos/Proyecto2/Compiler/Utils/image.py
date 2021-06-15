#!/usr/bin/env python3
from PIL import Image
from constants import FORMAT


def decToHex(result):
    newHexArray = [int(result[i:i+3]) for i in range(0, len(result), 3)]
    x = ""
    for n in newHexArray:
        h = hex(int(n))
    
        sliced = h[2:]
        output = hex3Digits(sliced)
        x += output
    return x


def hex3Digits(hexa):
    if(len(hexa) == 1):
        return '0'+str(hexa)
    else:
        return str(hexa)
        

def imageToFile(filename, out):
    photo = Image.open(filename)  # your image
    photo = photo.convert('RGB')

    width = photo.size[0]  # define W and H
    height = photo.size[1]

    imageFile = open(out, 'w')
    imageFile.truncate()

    for y in range(0, height):  # each pixel has coordinates
        row = ''
        for x in range(0, width):

            RGB = photo.getpixel((x, y))
            R, G, B = RGB  # now you can use the RGB value
            temp = f'{R:03}{G:03}{B:03}'
            result = decToHex(temp)
            imageFile.write(result + FORMAT)

    imageFile.close()
    print('Image File Success')


def getSizeImage(filename):
    photo = Image.open(filename)
    # 0:Width 1:Heigth
    return photo.size
