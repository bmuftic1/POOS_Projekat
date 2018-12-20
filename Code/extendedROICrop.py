import cv2
import spasavanjeSlika as ss
#import linearStretchingContrast as lsc
#import sharpenFilter as sf

from PIL import Image
import numpy

def normalizeRed(intensity):
    iI = intensity
    minI = 60
    maxI = 215
    minO = 0
    maxO = 255
    iO = (iI - minI) * (((maxO - minO) / (maxI - minI)) + minO)
    return iO


def normalizeGreen(intensity):
    iI = intensity
    minI = 50
    maxI = 215
    minO = 0
    maxO = 255
    iO = (iI - minI) * (((maxO - minO) / (maxI - minI)) + minO)
    return iO


def normalizeBlue(intensity):
    iI = intensity
    minI = 50
    maxI = 215
    minO = 0
    maxO = 255
    iO = (iI - minI) * (((maxO - minO) / (maxI - minI)) + minO)
    return iO

def increaseContrast (image, factor):
    pil_im = Image.fromarray(image)
    multiBands = pil_im.split()

    normalizedRedBand = multiBands[2].point(normalizeRed)
    normalizedGreenBand = multiBands[1].point(normalizeGreen)
    normalizedBlueBand = multiBands[0].point(normalizeBlue)

    new_pil_im = Image.merge("RGB", (normalizedRedBand, normalizedGreenBand, normalizedBlueBand))
    im2 = cv2.cvtColor(numpy.array(new_pil_im), cv2.COLOR_RGB2BGR)

    return im2

def sharpenImage(image):
    kernel_sharpening = numpy.array([[0, -2, 0],
                                  [-2, 9, -2],
                                  [0, -2, 0]])

    sharpened = cv2.filter2D(image, -1, kernel_sharpening)
    return sharpened


file  = open("../KoordinateROIExtended.txt", "r")
coordinateLines = file.readlines()
for i in range(0, len(coordinateLines)):
    if i < 99:
        coordinateLine = coordinateLines[i][5:]
    else:
        coordinateLine = coordinateLines[i][6:]
    coordinates = coordinateLine.split(",")
    coordinates[3] = coordinates[3][:len(coordinates[3])]
    photo = cv2.imread('../ExtendedROI/{}_ROI.jpg'.format(i + 1))
    croppedPhoto = photo[int(coordinates[1]):int(coordinates[3]), int(coordinates[0]):int(coordinates[2]), :]
    contrastPhoto = increaseContrast(croppedPhoto, 30)
    sharpPhoto = sharpenImage(croppedPhoto)
    ss.spasiSliku("../ExtendedCroppedROI", "CroppedROI", i + 1, sharpPhoto)