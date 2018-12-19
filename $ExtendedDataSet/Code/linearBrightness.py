import cv2
import matplotlib.pyplot as plt
import spasavanjeSlika as ss

def increaseBrightness (image, factor):
    factorscaled = (factor / 100) + 1
    return cv2.convertScaleAbs(image, 1, factorscaled)

def proba():
	image = cv2.imread('image.jpeg')
	brighterImage = increaseBrightness(image, 20)
	plt.subplot(121), plt.imshow(image), plt.title('Originalna slika')
	plt.xticks([]), plt.yticks([])
	plt.subplot(122), plt.imshow(brighterImage), plt.title('Posvijetljena slika')
	plt.xticks([]), plt.yticks([])
	plt.show()
	ss.spasiSliku("BrighterImages", "image", 2, brighterImage)

for i in range(0, 90):
    slika = cv2.imread('./ROI/{}_ROI.jpg'.format(i+1))
    nova = increaseBrightness(slika, 20)
    ss.spasiSliku("Brightness", "LinearBrightness", i+1, nova)