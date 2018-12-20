import os as os
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image
import easygui
import os
import math as m
import spasavanjeSlika as ss

os.chdir('..')

lowerR = (170, 0, 0)
upperR = (255, 130, 160)

f = open("./DeskriptorTest3.csv", "a")
f.write("Hu1,Hu2,Hu3,Hu4,Hu5,Hu6,Hu7\n")

for i in range(0,150):
	try:
		Slika = cv2.imread('./Test3/CroppedROI{}.jpg'.format(i+1))

		B = cv2.inRange(Slika, lowerR, upperR)

		shape = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
		nm = cv2.morphologyEx(B,cv2.MORPH_OPEN, shape)
		shape2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,5))
		NewMask= cv2.dilate(nm,shape2)
		B=NewMask
		huMoments = cv2.HuMoments(cv2.moments(B)).flatten()

		for i in range(0,7):
			huMoments[i] = -1* m.copysign(1.0, huMoments[i]) * m.log10(abs(huMoments[i]))
		f = open("./DeskriptorTest3.csv", "a")
		f.write("{},{},{},{},{},{},{}\n".format(huMoments[0],huMoments[1],huMoments[2],huMoments[3],huMoments[4],huMoments[5],huMoments[6]))
	except:
		print('DW, ALL GOOD, CONTINUING...')


f = open("./DeskriptorTrain3.csv", "a")
f.write("Hu1,Hu2,Hu3,Hu4,Hu5,Hu6,Hu7,Klasa\n")
klasa=1

for i in range(0,150):
	try:
		Slika = cv2.imread('./Train3/CroppedROI{}.jpg'.format(i+1))

		B = cv2.inRange(Slika, lowerR, upperR)

		if (i>49):
			klasa=2
		if (i>99):
			klasa=3
		print("{}, {}\n".format(i,klasa))

		shape = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
		nm = cv2.morphologyEx(B,cv2.MORPH_OPEN, shape)
		shape2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,5))
		NewMask= cv2.dilate(nm,shape2)
		B=NewMask
		huMoments = cv2.HuMoments(cv2.moments(B)).flatten()

		for i in range(0,7):
			huMoments[i] = -1* m.copysign(1.0, huMoments[i]) * m.log10(abs(huMoments[i]))
		f = open("./DeskriptorTrain3.csv", "a")
		f.write("{},{},{},{},{},{},{},{}\n".format(huMoments[0],huMoments[1],huMoments[2],huMoments[3],huMoments[4],huMoments[5],huMoments[6],klasa))
	except:
		print('DW, ALL GOOD, CONTINUING...')

	#print(huMoments)

	#f = open("./DeskriptorTrain.txt", "a")
	#f.write("{}{} {},{},{},{}\n".format(naziv,broj, x1,y1,x2,y2))


	# B, contours,_ = cv2.findContours(B, mode = cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)

	# contours = sorted(contours, key = cv2.contourArea, reverse=True)
	# #print(contours)

	# Slika = cv2.drawContours(Slika,contours, contourIdx=-1, color=(0,0,255), thickness=1)

	# cv2.imshow('b', B)
	# cv2.imshow('gr', Slika)
	# cv2.waitKey()