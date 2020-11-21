import cv2
import numpy as np
from scipy.ndimage.interpolation import shift
from matplotlib import pyplot as plt


debugStatus = False

#Load Image
img1 = cv2.imread('./img/3D-Matplotlib.png')
img2 = cv2.imread('./img/mainsvmimage.png')
img3 = cv2.imread('./img/mainlogo.png')

#get size and channel info 
rows1, cols1, channels1 = img1.shape  
rows2, cols2, channels2 = img2.shape
rows3, cols3, channels3 = img3.shape

#Create New image
totalRow = rows1 + 10
totalCol = cols1 + cols2 + 30

newImage = np.zeros((totalRow, totalCol, 3), np.uint8)

#Add to image (linear)
for x in range(totalRow-1):
    for y in range(totalCol-1):
        if y > 10 and y<509 and x > 5 and x < 255:
            imgx = x - 5
            imgy = y - 10
            newImage[x,y] = img1[imgx,imgy]

        elif y >= 509 and y<1009 and x > 5 and x < 255:
            imgx = x - 5
            imgy = y - 509

            newImage[x,y] = img2[imgx, imgy]

        else:
            #newImage[x,y] = newImage[x,y]
            newImage[x,y] = [255,255,255]

#Add logo with mask on newImage
#Select logo place on ımage
logoPlace = newImage[0:rows3, 0:cols3]

#convert logo to gray
img3Gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)

#create a mask for logo
ret, img3Mask = cv2.threshold(img3Gray, 220, 255,cv2.THRESH_BINARY)

#create a not mask
img3MaskNot = cv2.bitwise_not(img3Mask) 

#apply mask on images
newImageBG = cv2.bitwise_and(logoPlace, logoPlace, mask=img3Mask)
img3New = cv2.bitwise_and(img3, img3, mask=img3MaskNot)

#add logo on newImage
logo = newImageBG + img3New
newImage[0:rows3, 0:cols3] = logo

#Show img
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.imshow('newImage', newImage)

#Debug Windows:
if debugStatus:
    cv2.imshow('logoPlace', logoPlace)
    cv2.imshow('img3Gray', img3Gray)
    cv2.imshow('img3Mask', img3Mask)
    cv2.imshow('newImageBG', newImageBG)
    cv2.imshow('img3New', img3New)
    cv2.imshow('logo', logo)

cv2.waitKey(0)
cv2.destroyAllWindows()

if __name__ == '__main__':

    if debugStatus == True:
        print('img1\nrows:{}\ncols:{}\nchannels:{}\n'.format(rows1, cols1, channels1), end='')
        print('img2\nrows:{}\ncols:{}\nchannels:{}\n'.format(rows2, cols2, channels2), end='')
        print('img3\nrows:{}\ncols:{}\nchannels:{}\n'.format(rows3, cols3, channels2), end='')
        print('totalCol : {}, totalRow : {}'.format(totalCol, totalRow))
    
    print('Complete!')