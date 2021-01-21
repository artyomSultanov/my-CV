import cv2 as cv

cam = cv.VideoCapture(0)

hog = cv.HOGDescriptor()
hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())


while True:
	ret, frame = cam.read()
	frame = cv.resize(frame, (400, 300))
	cv.imshow('frame', frame)
	(rects, weights) = hog.detectMultiScale(frame, scale=1.1, winStride=(2, 2))
	
	for (x, y, w, h) in rects:
		cv.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
	cv.imshow('detect', frame)
	if cv.waitKey(1) == 27:
		break

cv.destroyAllWindows()
cam.release()

