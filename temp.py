# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cv2
import numpy as np

r, c = (2, 3)
x = np.zeros((r,c,8), dtype=np.uint8)
print('x= ', x)
print('x.shape', x.shape)

'''
img = cv2.imread('ashu.jpg')

img_resize = cv2.resize(img, (512,512))
cv2.imshow('img', img_resize)
cv2.imwrite('ashu-color.jpg', img_resize)
print('img_resize.shape', img_resize.shape)

cv2.waitKey()
cv2.destroyAllWindows()
'''

'''
img = cv2.imread('hallie3.jpg')
img_small = cv2.resize(img, (512,512))
cv2.imshow('2', img)
cv2.imshow('1', img_small)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite('hallie.jpg', img_small)
print('save')
'''


#x = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]])
#print(x[4,:])

'''x = np.zeros((200,200,3), dtype=np.uint8)
x[0:50,0:50,2]=255
cv2.imshow('x', x)
cv2.waitKey()
cv2.destroyAllWindows()
'''

'''
img = np.random.randint(0,255,size=[512,512],dtype=np.uint8)
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
'''