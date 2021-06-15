
import os
from Utils.utils import *
from constants import COLOR_PERCENTAGE
from constants import OPACITY_PERCENTAGE, ORIENTATION


imagePath = 'Images\\_example.jpg'
alfaPath = 'Images\\_alfa.png'

imageOutputPath = 'Output\\image.txt'
alfaOutputPath = 'Output\\alfa.txt'


def main():
    __initFolder()
    __removeFiles("./Images", ".png")
    __removeFiles("./Output", ".txt")

    useUserInput = False
    createGradientImage = True

    c1 = [1, 0, 255]
    c2 = [255, 0,  150]
    opacity = 25 # 0 || 25 || 75 || 100
    orientation = 'own' # vertical || horizontal || diagonal || own

    if(useUserInput):
        c1, c2, opacity, orientation = __userInputs()

    gradientOutputPath = f'Output\{orientation}.txt'
    gradientPath = f'Images\_{orientation}.png'

    '''
    Create a new file, with the pixels values from an image
    '''
    imageToFile(imagePath, imageOutputPath)

    '''
    Get the image size
    '''
    w, h = getSizeImage(imagePath)

    '''
    Create a new file, with the gradient image
    '''
    if (orientation == 'vertical'):
        verticalGradient(c1, c2, w, h, 'vertical.txt') # POR ARQUI
    elif (orientation == 'horizontal'):
        horizontalGradient(c1, c2, w, h, 'horizontal.txt')
    elif (orientation == 'diagonal'):
        diagonalGradient(c1, c2, w, h, 'diagonal.txt')
    elif (orientation == 'own'):
        ownGradient(c1, c2, w, h, 'own.txt')

    createAlfaImage(alfaOutputPath, imageOutputPath,
                    gradientOutputPath, opacity)

    loadImage(alfaPath, alfaOutputPath, w, h)

    if(createGradientImage):
        loadImage(gradientPath, gradientOutputPath, w, h)

    return 0


def __userInputs():
    r1 = __inputNumber("R1? (0: 0%, 1: 25%, 2: 75%, 3: 100%) : ")
    g1 = __inputNumber("G1? (0: 0%, 1: 25%, 2: 75%, 3: 100%) : ")
    b1 = __inputNumber("B1? (0: 0%, 1: 25%, 2: 75%, 3: 100%) : ")
    print('')
    r2 = __inputNumber("R2? (0: 0%, 1: 25%, 2: 75%, 3: 100%) : ")
    g2 = __inputNumber("G2? (0: 0%, 1: 25%, 2: 75%, 3: 100%) : ")
    b2 = __inputNumber("B2? (0: 0%, 1: 25%, 2: 75%, 3: 100%) : ")
    print('')
    opacity = __inputNumber("Opacity? (0: 0%, 1: 25%, 2: 75%, 3: 100%) : ")
    print('')
    orientation = __inputNumber(
        "Gradient Orientation? (0: Vertical, 1: Horizontal, 2: Diagonal, 3: Vertical Gap) : ")
    print('')

    #            R        G        B
    color1 = [COLOR_PERCENTAGE[r1], COLOR_PERCENTAGE[g1], COLOR_PERCENTAGE[b1]]
    color2 = [COLOR_PERCENTAGE[r2], COLOR_PERCENTAGE[g2], COLOR_PERCENTAGE[b2]]

    return [color1, color2, OPACITY_PERCENTAGE[opacity], ORIENTATION[orientation]]


def __initFolder():
    outputFolder = 'Output'
    if not os.path.exists(outputFolder):
        os.makedirs(outputFolder)


def __removeFiles(directory, extension):
    files_in_directory = os.listdir(directory)
    filtered_files = [
        file for file in files_in_directory if file.endswith(extension)]
    for file in filtered_files:
        path_to_file = os.path.join(directory, file)
        os.remove(path_to_file)


def __inputNumber(message):
    while True:
        try:
            userInput = int(input(message))
            if(userInput < 0 or userInput > 3):
                __outRange()
        except ValueError:
            print("Not an integer or out of range [0-3]! Try again.")
            continue
        else:
            return userInput
            break

if __name__ == '__main__':
    main()
