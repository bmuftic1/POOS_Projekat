import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image
import easygui
import os
import spasavanjeSlika as ss #poziva se sa ss.SpasiSliku(...)

#limfociti su od 1 do 30
#neurolimfi od 31 do 60
#ostatak od 61 do 90


koordinate=[]

def mouse(event,x,y,flags,params):

	if event==cv2.EVENT_LBUTTONDOWN:
		koordinate.append([x,y])

	elif event==cv2.EVENT_LBUTTONUP:
		koordinate.append([x,y])
		cv2.rectangle(Slika, (koordinate[0][0],koordinate[0][1]), (koordinate[1][0],koordinate[1][1]), (0,255,0), 2)
		cv2.imshow("Slika", Slika)


def upisi(naziv, broj,x1,y1,x2,y2):
	f = open("./KoordinateROI.txt", "a")
	f.write("{}{} {},{},{},{}\n".format(naziv,broj, x1,y1,x2,y2))


def nadjiROI(c, I, i):
	c = c*0
	if (len(koordinate)!=2):
		print("Ne moze se croppati")
		return
	x1=koordinate[0][0]
	y1=koordinate[0][1]
	x2=koordinate[1][0]
	y2=koordinate[1][1]
	c[y1:y2,x1:x2] = (255,255,255)
	B = cv2.inRange(c, (250,250,250), (255,255,255))
	finalno = cv2.bitwise_and(I, I, mask=B)


	folder="ROI" 
	naziv="ROI"
	broj=i+1 
	slika=finalno
	ss.spasiSliku(folder, naziv, broj, slika)

	upisi(naziv, broj,x1,y1,x2,y2)


brojSlika=90
os.chdir('..')

for i in range(0, brojSlika):
	while True: 
		Slika = cv2.imread('./DataSet/{}.jpeg'.format(i+1))
		c = Slika.copy()
		cv2.namedWindow("Slika")
		cv2.setMouseCallback("Slika", mouse)
		cv2.imshow("Slika", Slika)
		#pozovi funkciju da odredis granice

		key = cv2.waitKey()

		if (key==ord("r")):
			Slika=c.copy()
			koordinate=[]
		elif(key==ord("c")):
			nadjiROI(Slika, c, i)
			koordinate=[]
			break
