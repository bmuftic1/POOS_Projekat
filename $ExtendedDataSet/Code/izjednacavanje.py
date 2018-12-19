import cv2
import numpy as np
import spasavanjeSlika as ss

def pozoviIzjednacavanje():
	for i in range(0, 90):
		img = cv2.imread('./ROI/{}_ROI.jpg'.format(i+1))

		for j in range(0, 3):
			img[:,:,j] = cv2.equalizeHist(img[:,:,j])
		ss.spasiSliku("Histogram", "equalizeHist", i+1, img)

pozoviIzjednacavanje()