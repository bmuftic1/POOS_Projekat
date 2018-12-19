for i in range(0, 90):
	try:
		Slika = cv2.imread('./Train/CroppedROI{}.jpg'
				.format(i + 1))
		B = cv2.inRange(Slika, lowerR, upperR)
		if (i > 29):
			klasa = 2
		if (i > 59):
			klasa = 3
		print("{}, {}\n".format(i, klasa))
		shape = cv2.getStructuringElement
				(cv2.MORPH_ELLIPSE, (2, 2))
		nm = cv2.morphologyEx(B, cv2.MORPH_OPEN, shape)
		shape2 = cv2.getStructuringElement
				(cv2.MORPH_ELLIPSE, (3, 5))
		NewMask = cv2.dilate(nm, shape2)
		B = NewMask
		huMoments = cv2.HuMoments(cv2.moments(B))
					.flatten()
		for i in range(0, 7):
			huMoments[i] = -1 * m.copysign(1.0, 
			huMoments[i]) * m.log10(abs(huMoments[i]))
		f = open("./DeskriptorTrain.csv", "a")
		f.write("{},{},{},{},{},{},{},{}\n"
		.format(huMoments[0],huMoments[1], huMoments[2],
		huMoments[3], huMoments[4], huMoments[5],
		huMoments[6], klasa))