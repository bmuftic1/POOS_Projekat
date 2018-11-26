import random as random
import os
import cv2

naziv="ROI"
folder="ROI"

if (os.path.isdir("Train")==False):
	#kreiraj folder
	os.mkdir("Train")

if (os.path.isdir("Test")==False):
	#kreiraj folder
	os.mkdir("Test")

if (os.path.isdir("Validacija")==False):
	#kreiraj folder
	os.mkdir("Validacija")

#10% validacija - 3 slike po klasi
#25% test - 7 slika po klasi
#65% train - 19 slika po klasi

odabraniBrojeviValidacija=[]
d=1
g=30

#validacija
while(True):

	if(len(odabraniBrojeviValidacija)==3 or len(odabraniBrojeviValidacija)==6):
		d+=30
		g+=30
	elif(len(odabraniBrojeviValidacija)==9):
		break
	r = random.randint(d,g)
	if(r in odabraniBrojeviValidacija):
		continue
	odabraniBrojeviValidacija.append(r)
	I = cv2.imread("{}/{}{}.jpg".format(folder, naziv, r))
	cv2.imwrite('Validacija/{}{}.jpg'.format(naziv, r), I)
 
odabraniBrojeviTest=[]

d=1
g=30

#Test
while(True):

	if(len(odabraniBrojeviTest)==7 or len(odabraniBrojeviTest)==14):
		d+=30
		g+=30
	elif(len(odabraniBrojeviTest)==21):
		break

	r= random.randint(d,g)
	if(r in odabraniBrojeviTest or r in odabraniBrojeviValidacija):
		continue
	odabraniBrojeviTest.append(r)

	I = cv2.imread("{}/{}{}.jpg".format(folder, naziv, r))
	cv2.imwrite('Test/{}{}.jpg'.format(naziv, r), I)


#Train
for i in range(0,90):
	if (i+1 in odabraniBrojeviTest or i+1 in odabraniBrojeviValidacija):
		continue
	I = cv2.imread("{}/{}{}.jpg".format(folder, naziv, i+1))
	cv2.imwrite('Train/{}{}.jpg'.format( naziv, i+1), I)

