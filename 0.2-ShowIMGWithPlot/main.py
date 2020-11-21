import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./img/watch.jpg', cv2.IMREAD_GRAYSCALE)

if __name__ == '__main__':
    plt.imshow(img, cmap='gray', interpolation='bicubic')
    plt.plot([50,100], [80,100], 'c', linewidth=5)
    plt.show()

    print('Complete!')