import numpy as np
import cv2 as cv
# import video
from PIL import Image
cap = cv.VideoCapture(0)

while (True):
	ret, frame = cap.read()
	cv.imshow("Frame", frame)
	frameCopy = frame.copy()
	hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
	hsv = cv.blur(hsv, (5, 5))
	mask = cv.inRange(hsv, (0, 160, 180), (255, 255, 255))
	mask = cv.dilate(mask, None, iterations=2)
	cv.imshow("dilate", mask)

	contours = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
	contours = contours[0]
	if contours: 
		contours = sorted(contours, key=cv.contourArea, reverse=True)
		cv.drawContours(frame, contours, 0, (255, 0, 0), 3)
		cv.imshow("contours", frame)

		(x, y, w, h) = cv.boundingRect(contours[0])
		cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
		cv.imshow("rect", frame)

		roImg = frameCopy[y:y+h, x:x+h]
		cv.imshow("detect", roImg)
		roImg = cv.resize(roImg, (64, 64))
		roImg = cv.inRange(roImg, (0, 160, 180), (255, 255, 255))
		cv.imshow("resizedImg", roImg )
		countPix = 0
		for i in range(64):
			for j in range(64):
				if roImg[i].any():
					countPix += 1
		if countPix > 200:
			print("Lable of my longsleeve")
			print(countPix)


	if cv.waitKey(1) == 27:
		break

cap.release()
cv.destroyAllWindows()