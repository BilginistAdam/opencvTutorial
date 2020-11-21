import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./img/watch.jpg', cv2.IMREAD_COLOR)


#####################################################
#
#   READ AND WRITE A PIXEL/PIXELS ON A IMAGE
#
#####################################################
#This variable holds color information where this location on image
#and we can change it.
px = img[55,55]
print('(55,55) color info :', px)

img[55,55] = [255,255,255]

px = img[55,55]
print('(55,55) color info (after changed) : ', px)

#This variable is an array that hold color information where these locations
#and we can change it 
roi = img[100:150, 100:150]
print('(100,100) - (150,150) : ',roi)

img[100:150, 100:150] = [255,255,255]

#####################################################
#
#   COPY AND PASTE A PIXEL/PIXELS ON A IMAGE
#
#####################################################
#Copy these pixsels
watchFace = img[37:111, 107:194]

#Paste these pixsels
img[0:74, 0:87] = watchFace

#Show changes
cv2.imshow('changed img',img)
cv2.waitKey()
cv2.destroyAllWindows()

if __name__ == '__main__':
    print('Complete!')