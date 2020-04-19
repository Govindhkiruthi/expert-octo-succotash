# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 18:49:33 2020

@author: 780020
"""

import cv2
import numpy as np
import pyautogui

screen_size=(1920, 1080)

# create Encoder code of video format XVID or MPEG
fourcc=cv2.VideoWriter_fourcc(*"XVID")

# Create output file with encoder, films per sec and Screen size 
out=cv2.VideoWriter("output.avi",fourcc,5.0,(screen_size))

# screen will be recording untill press ESC key
while True:
    #Take the screenshot
    img=pyautogui.screenshot()
    
    #convert it an array
    img_np=np.array(img)
    
    #Convert the color asif in original
    frame=cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
    
    #Show the screen
    cv2.imshow("Screen",frame)
    
    #output will be recorded
    out.write(frame)
    
    #cv2.imshow("show",frame)
    
    #To stop the recording press ESC
    if cv2.waitKey(1)==27:
       break

#Output will be generated
out.release()
#Screen recoder will be closed
cv2.destroyAllWindows()
