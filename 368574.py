#-------------------------------------------------------------------------------
# INTPROG Python Coursework
# James Taylor
# 368574
# Autumn Teaching Block 2014
#-------------------------------------------------------------------------------

from graphics import *

def main():
    print("Patchwork Drawing Program up368574")
    patchWSize, colourGroup = getInputs()
    win, patchColours, patchTypes = drawPatchwork(patchWSize*100, colourGroup)
    changePatchwork(win, patchWSize*100, patchColours, patchTypes, colourGroup)

def getInputs():
    patchworkSize = getValidPatchworkSize()
    colourGroup = getValidColours()
    return patchworkSize, colourGroup

def getValidPatchworkSize():
    print("Enter desired patchwork dimensions. Valid sizes are 5, 7, and 9.")
    size = 0
    validSizes = [5, 7, 9]
    while size not in validSizes:
        sizeStr = input("Size: ")
        if sizeStr.isdigit():
            size = eval(sizeStr)
        if size not in validSizes:
            print("Invalid input. Valid sizes are 5, 7, and 9,")
    return size

def getValidColours():
    colourGroup = []
    validColours = ["red", "green", "blue", "yellow", "magenta", "cyan"]
    print("Enter colours wanted in patchwork. Valid colours are ", end = "")
    for validColour in validColours:
        if validColour == validColours[-1]:
            print("and " + validColour + ".")
        else:
            print(validColour, end = ", ")
    for i in range(1, 5):
        inputColour = ""
        while inputColour not in validColours:
            inputString = "Colour " + str(i) + ": "
            inputColour = input(inputString).lower()
            if inputColour in validColours:
                colourGroup.append(inputColour)
            else:
                print("Invalid input. Valid inputs are ", end = "")
                for validColour in validColours:
                    if validColour == validColours[-1]:
                        print("and " + validColour + ".")
                    else:
                        print(validColour, end = ", ")
    return colourGroup

def drawPatchwork(winSize, colourGroup):
    win = GraphWin("Patchwork", winSize, winSize)
    win.setBackground("white")
    patchIndex = 0
    patchColourCount = 0
    patchColours = []   #list of numbers, used as indices for colourGroup
    patchTypes = []     #list of booleans, used to determine patch type
    for i in range(0, winSize, 100):
        for j in range(0, winSize, 100):
            patchColours.append(patchColourCount % 4)
            patchColour = colourGroup[patchColours[patchIndex]]
            if i == 0 or j <= 100:
                patchTypes.append(True) #Patch 1
            else:
                patchTypes.append(False) #Patch 2
            patchType = patchTypes[patchIndex]
            drawPatch(win, j, i, patchColour, patchType)
            patchIndex = patchIndex + 1
            patchColourCount = patchColourCount + 1
    return win, patchColours, patchTypes

def changePatchwork(win, winSize, patchColours, patchTypes, colourGroup):
    while win.isOpen():
        try:
            patchNo, pX, pY = calculateClickedPatch(win.getMouse(), winSize)
            if patchColours[patchNo] == 3:
                patchColours[patchNo] = 0
            else:
                patchColours[patchNo] = patchColours[patchNo] + 1
            patchColour = colourGroup[patchColours[patchNo]]
            patchType = patchTypes[patchNo]
            drawPatch(win, pX, pY, patchColour, patchType)
        except GraphicsError:
            print("Window was closed")

def calculateClickedPatch(click, winSize):
    patchNumber = 0
    clickX = click.getX()
    clickY = click.getY()
    for i in range(0, winSize, 100):
        for j in range(0, winSize, 100):
            if clickY >= i and clickY < (i + 100) \
            and clickX >= j and clickX < (j + 100):
                return patchNumber, j, i
            patchNumber = patchNumber + 1

def drawPatch(win, x, y, patchColour, patchType):
    if patchType:   #Patch 1
        drawPatch1(win, x, y, patchColour)
    else:           #Patch 2
        drawPatch2(win, x, y, patchColour)

def drawPatch1(win, x, y, colour):
    difference = y - x
    for i in range(x, x + 99, 10):
        lineLeft = Line(Point(x, difference + i), Point(i + 10, y + 100))
        lineLeft.setFill(colour)
        lineLeft.draw(win)
        lineRight = Line(Point(x + 100, difference + i + 10 ), Point(i , y))
        lineRight.setFill(colour)
        lineRight.draw(win)

def drawPatch2(win, x, y, colour):
    for i in range(y, y + 99, 10):
        p1, p2 = Point(x, i), Point(x + 99, i + 10)
        if i % 20 == 0:
            for j in [x, x+25, x+55, x+85]:
                if j == x or j == x + 85:
                    p1, p2 = Point(j, i), Point(j + 15, i + 10)
                    drawRectangle(win, p1, p2, colour)
                else:
                    p1, p2 = Point(j, i), Point(j + 20, i + 10)
                    drawRectangle(win, p1, p2, colour)
        else:
            for j in range(x + 10, x+ 99, 30):
                p1, p2 = Point(j, i), Point(j + 20, i + 10)
                drawRectangle(win, p1, p2, colour)

def drawRectangle(win, p1, p2, colour):
    rectangle = Rectangle(p1, p2)
    rectangle.setFill(colour)
    rectangle.draw(win)

main()