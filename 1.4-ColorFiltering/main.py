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

    lowerFilter = np.array([100, 100, 255])
    upperFilter = np.array([225, 225, 225])

    mask = cv2.inRange(hsv, lowerFilter, upperFilter)
    res = cv2.bitwise_and(frame, frame, mask = mask)
    
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()


if __name__ == '__main__':
    print('Complete!')