import numpy as np
import cv2
import spasavanjeSlika as ss
import os


def pozoviBrightness():
	for i in range(0,90):
		img = cv2.imread('./ROI/{}_ROI.jpg'.format(i+1))
		hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

		value=40
		h, s, v = cv2.split(hsv)
		lim = 255 - value
		v[v > lim] = 255
		v[v <= lim] += value

		final_hsv = cv2.merge((h, s, v))
		img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)

		ss.spasiSliku("Brightness", "BrightnessHSV", i+1, img)


pozoviBrightness()