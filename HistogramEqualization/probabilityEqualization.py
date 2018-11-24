import cv2
import numpy
import matplotlib.pyplot as plt
import spasavanjeSlika as ss

def equalizeHistogram (image, factor):
    image2 = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
    height, width, channels = image2.shape
    array = []
    for i in range(0, 256):
        array.append(0)
    for x in range(0, height):
        for y in range(0, width):
            index = image2[x,y,1]
            array[index] += 1
            minIndex = 0
            maxIndex = 255
            if index - factor > 0:
                minIndex = index - factor
            if index + factor < 255:
                maxIndex = index + factor
            rangeForMin = array[(minIndex):(maxIndex+1)]
            min = numpy.argmin(rangeForMin) + (minIndex)
            image2[x,y,1] = min
    image2 = cv2.cvtColor(image2, cv2.COLOR_HLS2BGR)
    return image2


image = cv2.imread('image.jpeg')
enhancedImage = equalizeHistogram(image, 30)
plt.subplot(221), plt.imshow(image), plt.title('Originalna slika')
plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(enhancedImage), plt.title('Ujednačena slika')
plt.xticks([]), plt.yticks([])
histogram1 = cv2.calcHist([image],[0],None,[256],[0,256])
plt.subplot(223), plt.plot(histogram1), plt.title('Histogram originalne slike')
plt.xlim([0,256])
histogram2 = cv2.calcHist([enhancedImage],[0],None,[256],[0,256])
plt.subplot(224), plt.plot(histogram2), plt.title('Histogram ujednačene slike')
plt.xlim([0,256])
plt.show()
ss.spasiSliku("EqualizedImages", "image", 1, enhancedImage)