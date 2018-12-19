import cv2
import spasavanjeSlika as ss
import linearStretchingContrast as lsc
import sharpenFilter as sf

file  = open("../KoordinateROI.txt", "r")
coordinateLines = file.readlines()
for i in range(1, len(coordinateLines) - 1):
    coordinateLine = coordinateLines[i][5:]
    coordinates = coordinateLine.split(",")
    coordinates[3] = coordinates[3][:len(coordinates[3])]
    photo = cv2.imread('../ROI/{}_ROI.jpg'.format(i))
    croppedPhoto = photo[int(coordinates[1]):int(coordinates[3]), int(coordinates[0]):int(coordinates[2]), :]
    contrastPhoto = lsc.increaseContrast(croppedPhoto, 30)
    sharpPhoto = sf.sharpenImage(croppedPhoto)
    ss.spasiSliku("../CroppedROI", "CroppedROI", i, sharpPhoto)