import cv2
import matplotlib.pyplot as plt
import spasavanjeSlika as ss

def increaseBrightness (image, factor):
    factorscaled = (factor / 100) + 1
    return cv2.convertScaleAbs(image, 1, factorscaled)


image = cv2.imread('image.jpeg')
brighterImage = increaseBrightness(image, 20)
plt.subplot(121), plt.imshow(image), plt.title('Originalna slika')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(brighterImage), plt.title('Posvijetljena slika')
plt.xticks([]), plt.yticks([])
plt.show()
ss.spasiSliku("BrighterImages", "image", 2, brighterImage)