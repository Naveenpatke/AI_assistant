##!/usr/bin/env python
import numpy as np
import sys
import cv2
from playsound import playsound
from gtts import gTTS

print ("Enter the Text :")
str=input()
while str != "exit":
    print(str)
    myobj = gTTS(text=str, lang='en')
    myobj.save(str+".mp3")
    playsound(str+".mp3")
    os.system(str+".mp3")
    str=input()
