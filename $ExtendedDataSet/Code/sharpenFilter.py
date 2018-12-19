import cv2
import matplotlib.pyplot as plt
import numpy as np
import spasavanjeSlika as ss
import os


def proba ():
    image = cv2.imread('image.jpeg')

    kernel_sharpening = np.array([[0, -2, 0],
                                  [-2, 9, -2],
                                  [0, -2, 0]])

    sharpened = cv2.filter2D(image, -1, kernel_sharpening)

    plt.subplot(121), plt.imshow(image), plt.title('Originalna slika')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(sharpened), plt.title('Izostrena slika')
    plt.xticks([]), plt.yticks([])
    plt.show()
    ss.spasiSliku("SharpenedImages", "image", "1", sharpened)

def sharpenImage(image):
    kernel_sharpening = np.array([[0, -2, 0],
                                  [-2, 9, -2],
                                  [0, -2, 0]])

    sharpened = cv2.filter2D(image, -1, kernel_sharpening)
    return sharpened



for i in range(0, 90):
    slika = cv2.imread('./ROI/{}_ROI.jpg'.format(i+1))
    nova = sharpenImage(slika)
    ss.spasiSliku("SharpenFilter", "SharpenFilter", i+1, nova)

for i in range(0, 90):
    slika = cv2.imread('./DenoiseFilter/{}_DenoiseFilter.jpg'.format(i+1))
    nova = sharpenImage(slika)
    ss.spasiSliku("CombinedDenoiseSharpen", "CombinedDenoiseSharpen", i+1, nova)