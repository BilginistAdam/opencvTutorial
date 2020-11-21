import cv2
import numpy as np
from matplotlib import pyplot as plt

#capture camera
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    _, frame = cap.read()
    #Convert color format to hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #set hsv color limits
    lowerFilter = np.array([150, 150, 50])
    upperFilter = np.array([180, 255, 200])

    mask = cv2.inRange(hsv, lowerFilter, upperFilter)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    kernel = np.ones((5,5), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations=1)
    dilation = cv2.dilate(mask,kernel, iterations=1)

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    cv2.imshow('frame', frame)
    cv2.imshow('res', res)
    cv2.imshow('erosion', erosion)
    cv2.imshow('dilation', dilation)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)
    
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()


if __name__ == '__main__':
    print('Complete!')