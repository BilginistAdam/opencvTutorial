import cv2
import numpy as np
from matplotlib import pyplot as plt

#loading image
img = cv2.imread('img/bookpage.jpg')

#Threshold for original iamge
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

#grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Threshold for grayscaled image
retval2, thresholdGray = cv2.threshold(imgGray, 12, 255, cv2.THRESH_BINARY)

#Adaptive Threshold
gaus = cv2.adaptiveThreshold(imgGray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

#otsu
retval2, otsu = cv2.threshold(imgGray, 125, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

#Show image
cv2.imshow('img', img)
cv2.imshow('imgGray', imgGray)
cv2.imshow('threshold', threshold)
cv2.imshow('thresholdGray', thresholdGray)
cv2.imshow('gaus', gaus) 
cv2.imshow('otsu', otsu)

#Close Windows
cv2.waitKey()
cv2.destroyAllWindows()

if __name__ == '__main__':
    print('Complete!')