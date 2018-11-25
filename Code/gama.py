import numpy as np
import cv2
import spasavanjeSlika as ss
import os


def gammaContrast(image, gamma):
	g = 1.0 / gamma
	table = np.array([((i / 255.0) ** g) * 255
		for i in np.arange(0, 256)]).astype("uint8")
 
	return cv2.LUT(image, table)

def pozivGama():
	for i in range(0,90):

		I = cv2.imread('./ROI/{}_ROI.jpg'.format(i+1))
		slika = gammaContrast(I,0.7)
		ss.spasiSliku("Contrast", "GammaContrast", i+1, slika)


pozivGama()