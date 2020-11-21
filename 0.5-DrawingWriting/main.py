import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./img/watch.jpg', cv2.IMREAD_COLOR)

#Draw a line on image
#BGR
cv2.line(img, (0,0), (150,150), (255, 255, 255), 15)
cv2.line(img, (50,50), (100,200), (255, 0, 0), 5)

#Draw a rectangle on image
cv2.rectangle(img, (15,25), (200,150), (0,255,0),3)

#Draw a circle on image
cv2.circle(img, (75,125), 25, (0,0,255), 8)
cv2.circle(img, (125, 75), 10, (150,150,150), -1)

#Draw your shape on image
pts = np.array([[10,5], [20,30], [70,20], [50,10]], np.int32)
#pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (255,0,255), 3)

#Write a text on image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV Tuts!', (85,25), font, 1, (0,0,0), 5, cv2.LINE_AA)

if __name__ == '__main__':

    cv2.imshow('watch with line', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print('Complete!')