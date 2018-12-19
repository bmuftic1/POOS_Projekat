import cv2
import os


def spasiSliku(folder, naziv, broj, slika):

	if (os.path.isdir(folder)==False):
		#kreiraj folder
		os.mkdir(folder)

	try:
		cv2.imwrite('./{}/{}_{}.jpg'.format(folder, broj, naziv), slika)
	except cv2.error as e:
		print('Slika {}{} nije spasena! Provjeriti da li postoji folder {}'.format(naziv, broj, folder))
