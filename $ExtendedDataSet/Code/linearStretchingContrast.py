import numpy
import os
import cv2
import matplotlib.pyplot as plt
import spasavanjeSlika as ss

from PIL import Image

def normalizeRed(intensity):
    iI = intensity
    minI = 60
    maxI = 215
    minO = 0
    maxO = 255
    iO = (iI - minI) * (((maxO - minO) / (maxI - minI)) + minO)
    return iO


def normalizeGreen(intensity):
    iI = intensity
    minI = 50
    maxI = 215
    minO = 0
    maxO = 255
    iO = (iI - minI) * (((maxO - minO) / (maxI - minI)) + minO)
    return iO


def normalizeBlue(intensity):
    iI = intensity
    minI = 50
    maxI = 215
    minO = 0
    maxO = 255
    iO = (iI - minI) * (((maxO - minO) / (maxI - minI)) + minO)
    return iO

def increaseContrast (image, factor):
    pil_im = Image.fromarray(image)
    multiBands = pil_im.split()

    normalizedRedBand = multiBands[2].point(normalizeRed)
    normalizedGreenBand = multiBands[1].point(normalizeGreen)
    normalizedBlueBand = multiBands[0].point(normalizeBlue)

    new_pil_im = Image.merge("RGB", (normalizedRedBand, normalizedGreenBand, normalizedBlueBand))
    im2 = cv2.cvtColor(numpy.array(new_pil_im), cv2.COLOR_RGB2BGR)

    return im2

def proba():
    image = cv2.imread('image.jpeg')
    enhancedImage = increaseContrast(image, 30)
    plt.subplot(121), plt.imshow(image), plt.title('Originalna slika')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(enhancedImage), plt.title('Poboljsana slika')
    plt.xticks([]), plt.yticks([])
    plt.show()
    ss.spasiSliku("ContrastImages", "image", 2, enhancedImage)


for i in range(0, 90):
    slika = cv2.imread('./ROI/{}_ROI.jpg'.format(i+1))
    nova = increaseContrast(slika, 30)
    ss.spasiSliku("Contrast", "LinearStretchingContrast", i+1, nova)