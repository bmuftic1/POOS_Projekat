import random as random
import os
import cv2

naziv = "CroppedROI"
folder = "../ExtendedCroppedROI"

if (os.path.isdir("../Train3") == False):
    # kreiraj folder
    os.mkdir("../Train3")

if (os.path.isdir("../Test3") == False):
    # kreiraj folder
    os.mkdir("../Test3")

if (os.path.isdir("../Validacija3") == False):
    # kreiraj folder
    os.mkdir("../Validacija3")

#10% validacija - 5 slika po klasi
#20% test - 10 slika po klasi
#70% train - 35 slika po klasi

odabraniBrojeviValidacija = []
d = 1
g = 50

# validacija
while (True):
    if (len(odabraniBrojeviValidacija) == 5 or len(odabraniBrojeviValidacija) == 10):
        d += 30
        g += 30
    elif (len(odabraniBrojeviValidacija) == 15):
        break
    r = random.randint(d, g)
    if (r in odabraniBrojeviValidacija):
        continue
    odabraniBrojeviValidacija.append(r)
    I = cv2.imread("{}/{}.jpeg".format("../ExtendedDataSet", r))
    cv2.imwrite('../Validacija3/{}{}.jpg'.format(naziv, r), I)

odabraniBrojeviTest = []

d = 1
g = 50

# Test
while (True):

    if (len(odabraniBrojeviTest) == 10 or len(odabraniBrojeviTest) == 20):
        d += 30
        g += 30
    elif (len(odabraniBrojeviTest) == 30):
        break

    r = random.randint(d, g)
    if (r in odabraniBrojeviTest or r in odabraniBrojeviValidacija):
        continue
    odabraniBrojeviTest.append(r)

    I = cv2.imread("{}/{}_{}.jpg".format(folder, r, naziv))
    cv2.imwrite('../Test3/{}{}.jpg'.format(naziv, r), I)

# Train
for i in range(0, 150):
    if (i + 1 in odabraniBrojeviTest or i + 1 in odabraniBrojeviValidacija):
        continue
    I = cv2.imread("{}/{}_{}.jpg".format(folder, i + 1, naziv))
    cv2.imwrite('../Train3/{}{}.jpg'.format(naziv, i + 1), I)