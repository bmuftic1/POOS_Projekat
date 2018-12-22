B = cv2.inRange(Slika, lowerR, upperR)
shape = cv2.getStructuringElement
		(cv2.MORPH_ELLIPSE, (2,2))
nm = cv2.morphologyEx
		(B,cv2.MORPH_OPEN, shape)
shape2 = cv2.getStructuringElement
		(cv2.MORPH_ELLIPSE, (3,5))
NewMask= cv2.dilate(nm,shape2)
B=NewMask
huMoments = cv2.HuMoments
		(cv2.moments(B)).flatten()
for i in range(0,7):
	huMoments[i] = -1 
	* m.copysign(1.0, huMoments[i])
	* m.log10(abs(huMoments[i]))
huMoments = huMoments.reshape(1,7)
rez = model.predict(huMoments)