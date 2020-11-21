import cv2
import numpy as np
from matplotlib import pyplot as plt

#Load images
img1 = cv2.imread('./img/3D-Matplotlib.png')
img2 = cv2.imread('./img/mainlogo.png')

#Some Method Add two image 
#add = img1 + img2
#add = cv2.add(img1, img2)
#weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)

#hold img size and channels info
#shape --> hold size info about image
row, col, channel = img1.shape
print('img1\nrows : ',row, type(row))
print('cols : ', col, type(col))
print('channels : ', channel, type(channel))
rows,cols,channels = img2.shape
print('img2\nrows : ',rows, type(rows))
print('cols : ', cols, type(cols))
print('channels : ', channels, type(channels))

#Select img1 0 to rows, 0 to cols pixel
roi = img1[0:rows, 0:cols]

#Create a mask for logo transparent sectors
#Convert to image gray filter
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
#create a mask with threshold funct.
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)

#inverse to mask
mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('res', img1)
cv2.imshow('masl_inv', mask_inv)
cv2.imshow('mask', mask)
cv2.imshow('dst', dst)
cv2.imshow('img2_fg', img2_fg)
cv2.imshow('img1_bg', img1_bg)
cv2.waitKey(0)
cv2.destroyAllWindows()

if __name__ == '__main__':
    print('Complete!')