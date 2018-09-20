#Intro.py
import PIL as P
from PIL import ImageGrab as IGRAB
from PIL import Image as I
import time

start_time = time.time()
'''
im = P.ImageGrab.grab(bbox=(100,400,2000,640))
im = im.getchannel(1);
im.save("/Users/jordanbonecutter/Desktop/newImage.bmp")
'''

desktopPath = "/Users/jordanbonecutter/Desktop/TestImages"

im = IGRAB.grab((1700,966,2050,1440))
imG = im.getchannel(1)
imR = im.getchannel(0)
im.save(desktopPath + "/NewImage.bmp")
imR.save(desktopPath + "/ImageR.bmp")
imG.save(desktopPath + "/ImageG.bmp")

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
    totalTestPixels = 0
    lowPosition = (0,0)
    for x in range(0, int(width/10)):
        for y in range(0, int(height/10)):
            temp = image.getpixel((x*10, y*10))
            if temp < lowVal:
                lowVal = temp
                lowPosition = (x*10, y*10)

            totalTestPixels = totalTestPixels + 1
            sumVal = sumVal + temp
    xLeft = lowPosition[0]
    xRight = lowPosition[0]
    xCurr = lowPosition[0]
    yCurr = lowPosition[1]
    yTop = lowPosition[1]
    yBottom = lowPosition[1]
    averageVal = sumVal/totalTestPixels

    while (image.getpixel((xLeft, yCurr)) < averageVal):
        xLeft = (xLeft - 5) if (xLeft - 5 > 0) else 0

    while (image.getpixel((xRight, yCurr)) < averageVal):
        xRight = (xRight + 5) if (xRight + 5 < width) else width - 1

    while (image.getpixel((xCurr, yTop)) < averageVal):
        yTop = (yTop - 5) if (yTop - 5 > 0) else 0

    while (image.getpixel((xCurr, yBottom)) < averageVal):
        yBottom = (yBottom + 5) if (yBottom + 5 < height) else height - 1

    return (xLeft, yTop, xRight, yBottom)

print("My program took ", time.time() - start_time, " to run")

imR = im.crop(findMinBBox(imR))
imG = im.crop(findMinBBox(imG))
imR.save(desktopPath + "/RedHat.bmp")
imG.save(desktopPath + "/GreenBal.bmp")










