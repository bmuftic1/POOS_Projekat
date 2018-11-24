import cv2
import matplotlib.pyplot as plt
import spasavanjeSlika as ss

def increaseContrast (image, factor):
    im2 = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
    mean = cv2.mean(im2)
    height, width, channels = im2.shape
    for x in range(0, height):
        for y in range(0, width):
            if im2[x,y,1] < mean[1] and im2[x,y,1] > factor:
                im2[x,y][1] -= factor
            if im2[x,y,1] > mean[1] and im2[x,y,1] < 255 - factor:
                im2[x,y,1] += factor
    return cv2.cvtColor(im2, cv2.COLOR_HLS2BGR)


image = cv2.imread('image.jpeg')
enhancedImage = increaseContrast(image, 20)
plt.subplot(121), plt.imshow(image), plt.title('Originalna slika')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(enhancedImage), plt.title('Poboljšana slika')
plt.xticks([]), plt.yticks([])
plt.show()
ss.spasiSliku("ContrastImages", "image", 1, enhancedImage)