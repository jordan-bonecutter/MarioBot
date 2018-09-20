import os
import PIL as P
from PIL import Image as I
import time
from PIL import ImageDraw as IDRAW
import serial

def findMinBBox(image):
    width, height = image.size
    lowVal = 255
    temp = 255
    averageVal = 0
    sumVal = 0
    xLeft = 0
    xRight = 0
    yTop = 0
    yBottom = 0
    xCurr = 0
    yCurr = 0
    stopCounter = 0
    totalTestPixels = 0
    lowPosition = (0,0)
    for x in range(0, int(width/9)):
        for y in range(0, int(height/9)):
            temp = image.load()[(x*9, y*9)]
            if temp < lowVal:
                lowVal = temp
                lowPosition = (x*9, y*9)

            totalTestPixels = totalTestPixels + 1
            sumVal = sumVal + temp
            
    xLeft = lowPosition[0]
    xRight = lowPosition[0]
    xCurr = lowPosition[0]
    yCurr = lowPosition[1]
    yTop = lowPosition[1]
    yBottom = lowPosition[1]
    averageVal = sumVal/totalTestPixels

    while (image.getpixel((xLeft, yCurr)) < averageVal) and stopCounter < 6:
        xLeft = (xLeft - 5) if (xLeft - 5 > 0) else 0
        stopCounter = stopCounter + 1

    stopCounter = 0

    while (image.getpixel((xRight, yCurr)) < averageVal) and stopCounter < 6:
        xRight = (xRight + 5) if (xRight + 5 < width) else width - 1
        stopCounter = stopCounter + 1

    stopCounter = 0
    
    while (image.getpixel((xCurr, yTop)) < averageVal) and stopCounter < 6:
        yTop = (yTop - 5) if (yTop - 5 > 0) else 0
        stopCounter = stopCounter + 1

    stopCounter = 0
    
    while (image.getpixel((xCurr, yBottom)) < averageVal) and stopCounter < 6:
        yBottom = (yBottom + 5) if (yBottom + 5 < height) else height - 1
        stopCounter = stopCounter + 1

    return (xLeft, yTop, xRight, yBottom)

def BBoxPos(Box):
    xCenter = (Box[0] + Box[2])/2
    yCenter = (Box[1] + Box[3])/2
    return (xCenter, yCenter)


def navec(pos1, pos2):
    return (pos2[0] - pos1[0], pos2[1] - pos1[1])


def FastScreen(BBox, fpath, fname):
    x0 = BBox[0]
    y0 = BBox[1]
    x1 = BBox[2]
    y1 = BBox[3]
    os.system("screencapture -R " + str(x0) + "," + str(y0)+ ","+ str(x1 - x0)+ ","+ str(y1 - y0)+ " "+ fname+ ".png")
    return I.open(fpath+ fname+ ".png")

def HighlightBBox(image, BBox, color):
    im = IDRAW.Draw(image)
    im.ellipse(BBox, fill=None, outline=color)

def DrawVec(image, vec):
    im = IDRAW.Draw(image)
    im.line(vec, fill = (0,0,0), width=10) 

def vec2Joystick(vec):
    norm = ((vec[0]*vec[0]) + (vec[1]*vec[1]))**(1/2)
    scale = 1/norm
    newVec = vec
    newVec[0] = newVec[0] * scale
    newVec[1] = newVec[1] * scale
    newVec[0] = newVec[0] + 1
    newVec[1] = newVec[1] + 1
    newVec = newVec/2
    newVec = newVec*255
    return newVec

def findHat(image):
    imageR = image.getchannel(0)
    width, height = image.size
    x = 0
    y = 0
    leave = False
    while (x < (width - 1)/9) and not leave:
        x = x + 9
        while (y < (height - 1)/9) and not leave:
            y = y + 9
            if(imageR.getpixel((x, y)) < 200):
                leave = True
    xLeft = x
    xRight = x
    xCurr = x
    yTop = y
    yBottom = y
    yCurr = y
    stopCounter = 0
    
    while (imageR.getpixel((xLeft, yCurr)) < 200) and stopCounter < 6:
        xLeft = (xLeft - 5) if (xLeft - 5 > 0) else 0
        stopCounter = stopCounter + 1

    stopCounter = 0

    while (imageR.getpixel((xRight, yCurr)) < 200) and stopCounter < 6:
        xRight = (xRight + 5) if (xRight + 5 < width) else width - 1
        stopCounter = stopCounter + 1

    stopCounter = 0
    
    while (imageR.getpixel((xCurr, yTop)) < 200) and stopCounter < 6:
        yTop = (yTop - 5) if (yTop - 5 > 0) else 0
        stopCounter = stopCounter + 1

    stopCounter = 0
    
    while (imageR.getpixel((xCurr, yBottom)) < 200) and stopCounter < 6:
        yBottom = (yBottom + 5) if (yBottom + 5 < height) else height - 1
        stopCounter = stopCounter + 1

    return (xLeft, yTop, xRight, yBottom)

def findBall(image):
    imageG = image.getchannel(1)
    width, height = image.size
    x = 0
    y = 0
    leave = False
    while (x < (width - 1)/9) and not leave:
        x = x + 9
        while (y < (height - 1)/9) and not leave:
            y = y + 9
            if(imageG.getpixel((x, y)) < 120):
                leave = True
    xLeft = x
    xRight = x
    xCurr = x
    yTop = y
    yBottom = y
    yCurr = y
    stopCounter = 0
    
    while (imageG.getpixel((xLeft, yCurr)) < 120) and stopCounter < 6:
        xLeft = (xLeft - 5) if (xLeft - 5 > 0) else 0
        stopCounter = stopCounter + 1

    stopCounter = 0

    while (imageG.getpixel((xRight, yCurr)) < 120) and stopCounter < 6:
        xRight = (xRight + 5) if (xRight + 5 < width) else width - 1
        stopCounter = stopCounter + 1

    stopCounter = 0
    
    while (imageG.getpixel((xCurr, yTop)) < 120) and stopCounter < 6:
        yTop = (yTop - 5) if (yTop - 5 > 0) else 0
        stopCounter = stopCounter + 1

    stopCounter = 0
    
    while (imageG.getpixel((xCurr, yBottom)) < 120) and stopCounter < 6:
        yBottom = (yBottom + 5) if (yBottom + 5 < height) else height - 1
        stopCounter = stopCounter + 1

    return (xLeft, yTop, xRight, yBottom)



























    










