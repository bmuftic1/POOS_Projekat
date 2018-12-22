import cv2
import matplotlib.pyplot as plt
import os as os
import pickle
import math as m
import numpy

class Slider:
    def __init__(self, x, y):
        self.windowSize = 50
        self.step = 10  # how much the slider moves
        self.scaleChange = 0.5  # if there is a need for scaling
        self.imageSize = [x, y]  #
        self.coordinates = [[0, 0], [self.windowSize, 0], [0, self.windowSize], [self.windowSize, self.windowSize]]  # upper left, upper right, lower left, lower right
        self.maxScale = 4
        self.currentScale = 0
        self.willScale = True
    def getCoordinates(self):
        return self.coordinates
    def slide(self):
        # staying in the same row, moving right
        if self.coordinates[1][0] + self.step <= self.imageSize[0]:
            for i in range(0, 4):
                self.coordinates[i][0] += self.step
        # going into the next row
        elif self.coordinates[3][1] + self.step <= self.imageSize[1]:
            self.coordinates[0][0] = 0
            self.coordinates[1][0] = self.windowSize
            self.coordinates[2][0] = 0
            self.coordinates[3][0] = self.windowSize
            for i in range(0, 4):
                self.coordinates[i][1] += self.step
        # cannot go to the next row - change scale and begin over
        else:
            self.currentScale += 1
            if self.currentScale == self.maxScale or not self.willScale:
                return False
            self.windowSize += int(self.windowSize * self.scaleChange)
            self.coordinates = [[0, 0], [self.windowSize, 0], [0, self.windowSize], [self.windowSize, self.windowSize]]
        return True
    def oneSlide(self, image):
        return image[int(self.coordinates[0][1]):int(self.coordinates[2][1]), int(self.coordinates[0][0]):int(self.coordinates[1][0]), :]

os.chdir('..')
here = os.path.dirname(os.path.abspath(__file__))
exportGaussianNB = os.path.join(here, '../Model/modelExportGaussianNB.sav')

lowerR = (170, 0, 0)
upperR = (255, 130, 160)

model = pickle.load(open(exportGaussianNB, 'rb'))

for i in range(0, 90):
    try:
        photo = cv2.imread('./Validacija/CroppedROI{}.jpg'.format(i+1))
        slider = Slider(len(photo[0]), len(photo))
        plt.show()
        foundRectangles = []
        results = [0, 0, 0]
        while (True):
            photoNew = cv2.imread('./Validacija/CroppedROI{}.jpg'.format(i+1))
            rectangle = slider.oneSlide(photoNew)
            B = cv2.inRange(rectangle, lowerR, upperR)
            shape = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))
            nm = cv2.morphologyEx(B, cv2.MORPH_OPEN, shape)
            shape2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 5))
            NewMask = cv2.dilate(nm, shape2)
            B = NewMask
            huMoments = cv2.HuMoments(cv2.moments(B)).flatten()
            a = 1
            try:
                coordinates = slider.getCoordinates()
                for j in range(0, 7):
                    huMoments[j] = -1 * m.copysign(1.0, huMoments[j]) * m.log10(abs(huMoments[j]))
                huMoments = huMoments.reshape(1, 7)
                results[int(model.predict(huMoments)) - 1] += 1
                h, w, _ = photoNew.shape
                B, contours, _ = cv2.findContours(B, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)
                contours = sorted(contours, key=cv2.contourArea, reverse=True)
                (x, y, w, h) = cv2.boundingRect(contours[0])
                if len(foundRectangles) == 0:
                    foundRectangles.append([coordinates[0][0], coordinates[0][1], coordinates[3][0], coordinates[3][1]])
                    slider.willScale = False
                else:
                    if coordinates[0][0] < foundRectangles[0][0]:
                        foundRectangles[0][0] = coordinates[0][0]
                    if coordinates[0][1] < foundRectangles[0][1]:
                        foundRectangles[0][1] = coordinates[0][1]
                    if coordinates[3][0] > foundRectangles[0][2]:
                        foundRectangles[0][2] = coordinates[3][0]
                    if coordinates[3][1] > foundRectangles[0][3]:
                        foundRectangles[0][3] = coordinates[3][1]
                photo2 = cv2.rectangle(photoNew, (coordinates[0][0], coordinates[0][1]), (coordinates[3][0], coordinates[3][1]), (255, 0, 0), 1)
                cv2.imshow('Slika', photo2)
                cv2.waitKey(5)
                provjera = slider.slide()
                if provjera == False:
                    break
            except:
                coordinates = slider.getCoordinates()
                photo2 = cv2.rectangle(photoNew, (coordinates[0][0], coordinates[0][1]), (coordinates[3][0], coordinates[3][1]), (255, 0, 0), 1)
                cv2.imshow('Slika', photo2)
                cv2.waitKey(5)
                provjera = slider.slide()
                if provjera == False:
                    break
        font = cv2.FONT_HERSHEY_SIMPLEX
        photo2 = cv2.rectangle(photo, (foundRectangles[0][0], foundRectangles[0][1]), (foundRectangles[0][2], foundRectangles[0][3]), (255, 0, 0), 2)
        text = ""
        if results[2] > 75:
            result = 2
        else:
            result = numpy.argmax(results[0:2])
        if result == 0:
            text = "Lymphocyte (1)"
        elif result == 1:
            text = "Neutrophil (2)"
        elif result == 2:
            text = "Something else (3)"
        if text != "":
            cv2.putText(photo2, text, (15, 35), cv2.FONT_HERSHEY_TRIPLEX, 0.4, (255, 0, 0), 1, cv2.LINE_AA)
            cv2.imshow('Slika', photo2)
            cv2.waitKey()
    except:
        print('DW, ALL GOOD, CONTINUING...')

'''for i in range(0, 90):
    try:
        photo = cv2.imread('./Validacija/CroppedROI{}.jpg'.format(i+1))
        slider = Slider(len(photo[0]), len(photo))
        plt.show()
        while (True):
            photoNew = cv2.imread('./Validacija/CroppedROI{}.jpg'.format(i+1))
            slider.oneSlide(photo)
            coordinates = slider.getCoordinates()
            photo2 = cv2.rectangle(photoNew, (coordinates[0][0], coordinates[0][1]), (coordinates[3][0], coordinates[3][1]), (255, 0, 0), 1)
            cv2.imshow('Slika', photo2)
            cv2.waitKey(5)
            provjera = slider.slide()
            if provjera == False:
                break
    except:
        print('DW, ALL GOOD, CONTINUING...')'''