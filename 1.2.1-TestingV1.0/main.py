import cv2
import numpy as np
from matplotlib import pyplot as plt

#Debug
debugStatues = True
#Some Parameters
border = 1
pading = 5

#load image
img0 = cv2.imread('./img/3D-Matplotlib.png')
img1 = cv2.imread('./img/mainsvmimage.png')
img2 = cv2.imread('./img/mainlogo.png')

#get size info about images
row0, col0, channel0 = img0.shape
row1, col1, channel1 = img1.shape
row2, col2, channel2 = img2.shape

#calculate new image size 
if row0 > row1:
    totalRow = row0 + (border * 2) + (pading * 2)
else:
    totalRow = row1 + (border * 2) + (pading * 2)

totalCol = col0 + col1 + (border * 4) + (pading * 4)

#create new image
newImage = np.zeros((totalRow, totalCol, 3), np.uint8)

#add img0 and img1 as linear
for x in range(totalRow - 1):
    for y in range(totalCol -1):
        if x > (pading + border):
            pass


#show images
cv2.imshow('img0', img0)
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('newImage', newImage)

cv2.waitKey(0)
cv2.destroyAllWindows()

if __name__ == '__main__':
    if debugStatues:
        print('img0 => Row : {}, Col : {}'.format(row0, col0))
        print('img1 => Row : {}, Col : {}'.format(row1, col1))
        print('img2 => Row : {}, Col : {}'.format(row2, col2))
        print('Pading : {}, Border : {}'.format(pading, border))
        print('newImage => Row : {}, Col : {}'.format(totalRow, totalCol))


    print('Complete!')