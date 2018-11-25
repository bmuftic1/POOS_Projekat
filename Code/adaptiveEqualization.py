import cv2
import matplotlib.pyplot as plt
import spasavanjeSlika as ss

def equalizeHistogram (image, factor):
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    lab_planes = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=1.0, tileGridSize=(factor, factor))
    lab_planes[0] = clahe.apply(lab_planes[0])
    lab = cv2.merge(lab_planes)
    return cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

def proba():
	image = cv2.imread('image.jpeg')
	enhancedImage = equalizeHistogram(image, 10)
	plt.subplot(221), plt.imshow(image), plt.title('Originalna slika')
	plt.xticks([]), plt.yticks([])
	plt.subplot(222), plt.imshow(enhancedImage), plt.title('Ujednacena slika')
	plt.xticks([]), plt.yticks([])
	histogram1 = cv2.calcHist([image],[0],None,[256],[0,256])
	plt.subplot(223), plt.plot(histogram1), plt.title('Histogram originalne slike')
	plt.xlim([0,256])
	histogram2 = cv2.calcHist([enhancedImage],[0],None,[256],[0,256])
	plt.subplot(224), plt.plot(histogram2), plt.title('Histogram ujednacene slike')
	plt.xlim([0,256])
	plt.show()
	ss.spasiSliku("EqualizedImages", "image", 2, enhancedImage)

for i in range(0, 90):
    slika = cv2.imread('./ROI/{}_ROI.jpg'.format(i+1))
    nova = equalizeHistogram(slika, 30)
    ss.spasiSliku("Histogram", "AdaptiveEqualization", i+1, nova)