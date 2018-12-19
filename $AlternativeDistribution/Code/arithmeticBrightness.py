import cv2
import matplotlib.pyplot as plt
import spasavanjeSlika as ss
import os

def increaseBrightness (image, factor):
    im2 = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
    height, width, channels = im2.shape
    for x in range(0, height):
        for y in range(0, width):
            if im2[x,y,1] < 255 - factor:
                im2[x,y,1] += factor
    return cv2.cvtColor(im2, cv2.COLOR_HLS2BGR)


def proba():
	image = cv2.imread('image.jpeg')
	brighterImage = increaseBrightness(image, 30)
	plt.subplot(121), plt.imshow(image), plt.title('Originalna slika')
	plt.xticks([]), plt.yticks([])
	plt.subplot(122), plt.imshow(brighterImage), plt.title('Posvijetljena slika')
	plt.xticks([]), plt.yticks([])
	plt.show()
	ss.spasiSliku("BrighterImages", "image", 1, brighterImage)



for i in range(0, 90):
    slika = cv2.imread('./ROI/{}_ROI.jpg'.format(i+1))
    nova = increaseBrightness(slika, 30)
    ss.spasiSliku("Brightness", "ArithmeticBrightness", i+1, nova)