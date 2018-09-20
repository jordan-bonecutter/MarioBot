#Intro.py
import os
import PIL as P
from PIL import Image as I
import time


os.system("screencapture -R 851,482,170,240 screencap4.png")
im = I.open("/Users/jordanbonecutter/Desktop/Python Projects" + "/screencap4.png")

print(im.getpixel((20, 57)))
