# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 13:56:00 2020

@author: 780020
"""

import sys
import cv2
import numpy as np
from PIL import ImageGrab
import time

fourcc=cv2.VideoWriter_fourcc(*'XVID')
filename="Output"+str(time.time())+".avi"
out=cv2.VideoWriter(filename,fourcc,15.0,(1366,768))
time.sleep(3)

while True:
    img=ImageGrab.grab()
    img_np=np.array(img)
    frame=cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
    out.write(frame)
    
    if cv2.waitKey(1)==37:
        break
    out.release()
    cv2.destroyAllWindows()