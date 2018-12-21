import csv
import numpy as np
import pandas as pd
import math
import os as os
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
import pickle
import cv2
import copy
import math as m

os.chdir('..')
here = os.path.dirname(os.path.abspath(__file__))
exportGaussianNB = os.path.join(here, '../Model/modelExportGaussianNB.sav')

lowerR = (170, 0, 0)
upperR = (255, 130, 160)

model = pickle.load(open(exportGaussianNB, 'rb'))

for i in range(0,90):
	try:
		Slika = cv2.imread('./Validacija/CroppedROI{}.jpg'.format(i+1))
		kopija = Slika.copy()


		B = cv2.inRange(Slika, lowerR, upperR)

		shape = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
		nm = cv2.morphologyEx(B,cv2.MORPH_OPEN, shape)
		shape2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,5))
		NewMask= cv2.dilate(nm,shape2)
		B=NewMask
		huMoments = cv2.HuMoments(cv2.moments(B)).flatten()

		for i in range(0,7):
			huMoments[i] = -1* m.copysign(1.0, huMoments[i]) * m.log10(abs(huMoments[i]))

		huMoments = huMoments.reshape(1,7)
		rez = model.predict(huMoments)

		h,w,_ = kopija.shape

		B, contours,_ = cv2.findContours(B, mode = cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)

		contours = sorted(contours, key = cv2.contourArea, reverse=True)

		(x,y,w,h) = cv2.boundingRect(contours[0])
		cv2.rectangle(kopija, (x,y), (x+w,y+h), (0,255,0), 2)

		cv2.putText(kopija, str(int(rez[0])), (15, 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255))

		cv2.imshow('Rezultat', kopija)
		cv2.waitKey()
		
	except:
		print('DW, ALL GOOD, CONTINUING...')