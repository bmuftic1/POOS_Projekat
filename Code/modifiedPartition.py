import random as random
import os
import cv2

naziv = "CroppedROI"
folder = "../CroppedROI"

if (os.path.isdir("../Train2") == False):
    # kreiraj folder
    os.mkdir("../Train2")

if (os.path.isdir("../Test2") == False):
    # kreiraj folder
    os.mkdir("../Test2")

if (os.path.isdir("../Validacija2") == False):
    # kreiraj folder
    os.mkdir("../Validacija2")

# 10% validacija - 3 slike po klasi
# 10% test - 3 slika po klasi
# 80% train - 24 slike po klasi

odabraniBrojeviValidacija = []
d = 1
g = 30

# validacija
while (True):
    if (len(odabraniBrojeviValidacija) == 3 or len(odabraniBrojeviValidacija) == 6):
        d += 30
        g += 30
    elif (len(odabraniBrojeviValidacija) == 9):
        break
    r = random.randint(d, g)
    if (r in odabraniBrojeviValidacija):
        continue
    odabraniBrojeviValidacija.append(r)
    I = cv2.imread("{}/{}.jpeg".format("../DataSet", r))
    cv2.imwrite('../Validacija2/{}{}.jpg'.format(naziv, r), I)

odabraniBrojeviTest = []

d = 1
g = 30

# Test
while (True):

    if (len(odabraniBrojeviTest) == 3 or len(odabraniBrojeviTest) == 6):
        d += 30
        g += 30
    elif (len(odabraniBrojeviTest) == 9):
        break

    r = random.randint(d, g)
    if (r in odabraniBrojeviTest or r in odabraniBrojeviValidacija):
        continue
    odabraniBrojeviTest.append(r)

    I = cv2.imread("{}/{}_{}.jpg".format(folder, r, naziv))
    cv2.imwrite('../Test2/{}{}.jpg'.format(naziv, r), I)

# Train
for i in range(0, 90):
    if (i + 1 in odabraniBrojeviTest or i + 1 in odabraniBrojeviValidacija):
        continue
    I = cv2.imread("{}/{}_{}.jpg".format(folder, i + 1, naziv))
    cv2.imwrite('../Train2/{}{}.jpg'.format(naziv, i + 1), I)