import cv2
import matplotlib.pyplot as plt
import spasavanjeSlika as ss

def denoiseImage (image):
    ''' linija za čitanje slike nam poslije neće ni trebati, jer će funkcija primati
        sliku, a ne path '''
    image = cv2.imread('image.jpg')
    reducedNoise = cv2.bilateralFilter(image, 9, 75, 75)
    ''' ovaj dio poslije treba zakomentarisati - stavljeno samo da se može
        odbraniti projekat '''
    plt.subplot(121),plt.imshow(image),plt.title('Originalna slika')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(reducedNoise),plt.title('Zamagljena slika')
    plt.xticks([]), plt.yticks([])
    plt.show()
    ss.spasiSliku("BlurImages", "image", "1", reducedNoise)

denoiseImage("")