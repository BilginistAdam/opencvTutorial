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

    kernel = np.ones((15,15), np.float32)/255

    smoothed = cv2.filter2D(res, -1, kernel)
    blur = cv2.GaussianBlur(res, (15,15), 0)
    median =  cv2.medianBlur(res, 15)
    bilateral = cv2.bilateralFilter(res, 15, 75, 75)

    
    cv2.imshow('frame', frame)
    #cv2.imshow('mask', mask)
    cv2.imshow('smoothed', smoothed)
    cv2.imshow('blur', blur)
    cv2.imshow('res', res)
    cv2.imshow('median', median)
    cv2.imshow('bilateral', bilateral)
    
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()


if __name__ == '__main__':
    print('Complete!')