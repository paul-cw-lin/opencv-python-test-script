# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 15:41:26 2021

@author: d19fd
"""

import cv2
import numpy as np

img = np.random.randint(0,256,size=[4,5],dtype=np.uint8)

t, rst = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

print('img\n', img)
print('t=', t)
print('rst\n', rst)

