import cv2
import czujnik 

przejscie = 0

while True:
	if czujnik.czunik_kamery() == 0 and przejscie == 0:
		przejscie = 1
		cam = cv2.VideoCapture(0)
		while True:
			ret, image = cam.read()
			cv2.imshow('Imagetest',image)
			break

		cv2.imwrite('/home/Alusya/Desktop/inzynierka/robot/zdj/testimage1.jpg', image)
		cam.release()
		cv2.destroyAllWindows()