import cv2
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage

import spasavanjeSlika as ss


def sharpenimage (image):
    image = cv2.imread('image.jpg')

    kernel_sharpening = np.array([[0, -2, 0],
                                  [-2, 9, -2],
                                  [0, -2, 0]])

    sharpened = cv2.filter2D(image, -1, kernel_sharpening)

    plt.subplot(121), plt.imshow(image), plt.title('Originalna slika')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(sharpened), plt.title('Izoštrena slika')
    plt.xticks([]), plt.yticks([])
    plt.show()
    ss.spasiSliku("SharpenedImages", "image", "1", sharpened)


sharpenimage("")
