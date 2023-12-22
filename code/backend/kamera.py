import cv2
import czujnik
import os 

przejscie = 0

while True:
	if czujnik.czunik_kamery() == 0 and przejscie == 0:
		przejscie = 1
		cam = cv2.VideoCapture(0)
		while True:
			ret, image = cam.read()
			cv2.imshow('Imagetest',image)
			break

		folder_path = 'zdj'
		if not os.path.exists(folder_path):
			os.makedirs(folder_path)

		image_path = os.path.join(folder_path, 'testimage1.jpg')
		cv2.imwrite(image_path, image)	
		cam.release()
		cv2.destroyAllWindows()