##!/usr/bin/env python
import numpy as np
import sys
import cv2
from playsound import playsound
from gtts import gTTS

print ("Enter the Text :")
str=input()
while str != "exit":
    print (str)
    #while True:
        
    #mtext = 'welcome to india welcome to india welcome to india '
    lag = 'en'
    myobj = gTTS(text=str, lang=lag)
    ##, slow =False)
    myobj.save(str+".mp3")
    playsound(str+".mp3")
    os.system(str+".mp3")
    str=input()
