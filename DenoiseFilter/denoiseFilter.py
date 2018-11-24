import cv2
import matplotlib.pyplot as plt
import spasavanjeSlika as ss

def denoiseImage (image):
    im2 = image.copy()
    return cv2.bilateralFilter(im2, 9, 75, 75)


image = cv2.imread('image.jpeg')
reducedNoise = denoiseImage(image)
plt.subplot(121), plt.imshow(image), plt.title('Originalna slika')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(reducedNoise), plt.title('Zamagljena slika')
plt.xticks([]), plt.yticks([])
plt.show()
ss.spasiSliku("BlurImages", "image", "1", reducedNoise)