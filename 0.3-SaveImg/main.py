import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./img/watch.jpg', cv2.IMREAD_GRAYSCALE)

if __name__ == '__main__':
    cv2.imwrite('./img/watchgray.png', img) 
    print('Complete!')