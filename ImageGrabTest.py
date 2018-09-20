#Intro.py
import os
import PIL as P
from PIL import Image as I
import time
from Mario import *
import serial

counter = 0

#ser = serial.Serial("/dev/cu.SLAB_USBtoUART") 

desktopPath = "/Users/jordanbonecutter/Desktop/TestImages"
videoBox = (847,478,1016,703)

loop_time = time.time()

ballPos = (0,0)
hit_time = time.time()
hitCounter = 0

while (time.time() - loop_time < 1):
    start_time = time.time()
    counter = counter + 1
    prevBall = ballPos
    #im = FastScreen(videoBox, "/Users/jordanbonecutter/Desktop/Python Projects/", "currentScreen")
    im = I.open("/Users/jordanbonecutter/Desktop/Test_Image.png")
    hatBox = findHat(im)
    hatPos = BBoxPos(hatBox)
    print(hatPos)
    print(ballPos)
    ballBox = findBall(im)
    ballPos = BBoxPos(ballBox)
    if(hatPos[0] < ballPos[0] + 10 and hatPos[0] > ballPos[0] - 10):
         ballPos = (10, 125)
    vector = navec(hatPos, ballPos)
#    joyVec = vec2Joystick(vector)
#    ser.write(str(chr(int(joyVec[0]))).encode('utf-8'))
    
    print("Loop took ", time.time() - start_time)
    

print(counter)

#ser.close()
