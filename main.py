#!/usr/bin/env python

# Author: Shyamal S. Chandra
# Date: October 30, 2018

# Source adapted: https://stackoverflow.com/questions/35097837/capture-video-data-from-screen-in-python/43560140

# TODO:
# 1. tar.gzip the files when done and move to a folder
# 2. convert the folder into a movie 
# 3. provide scripts to convert the movie into images5

# Libraries for the AlphaZeroXOX

import numpy as np
import cv2
import pyscreenshot as ImageGrab
from matplotlib import pyplot as plt
import datetime
from time import sleep

# Hardcoded coordinates 

top = 50
bottom = 295
left = 0
right = 430

counter = 0
num_of_digits = 20

while(True):

    # Get the time and date
    mydate = datetime.datetime.now().strftime("%y-%m-%d-%H-%M")

    # Grab the image
    img = ImageGrab.grab(bbox=(left, top, right, bottom)) #x, y, w, h
    
    # Save the image
    img.save('alphaMegaMan_' + str(counter).zfill(num_of_digits) + "-" + mydate + '.png')

    # Increase the counter
    counter = counter + 1

    # Wait for the key
    key = cv2.waitKey(1)
    if key == 27:
        break  

    # Sleep for 20 milliseconds
    sleep(00.02)