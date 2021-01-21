import cv2 as cv

def nothing(x):
	pass

cap = cv.VideoCapture(0)
cv.namedWindow("result")

cv.createTrackbar("minb", "result", 0, 255, nothing)
cv.createTrackbar("ming", "result", 0, 255, nothing)
cv.createTrackbar("minr", "result", 0, 255, nothing)

cv.createTrackbar("maxb", "result", 0, 255, nothing)
cv.createTrackbar("maxg", "result", 0, 255, nothing)
cv.createTrackbar("maxr", "result", 0, 255, nothing)

minb = 0
ming = 0
minr = 0
maxb = 255
maxg = 255
maxr = 255

while (True):
	ret,frame = cap.read()

	minb = cv.getTrackbarPos("minb", "result")
	ming = cv.getTrackbarPos("ming", "result")
	minr = cv.getTrackbarPos("minr", "result")

	maxb = cv.getTrackbarPos("maxb", "result")
	maxg = cv.getTrackbarPos("maxg", "result")
	maxr = cv.getTrackbarPos("maxr", "result")

	hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
	cv.imshow("hsv", hsv)

	hsv = cv.blur(hsv, (5, 5))
	cv.imshow("blur", hsv)

	mask = cv.inRange(hsv, (minb, ming, minr), (maxb, maxg, maxr))
	cv.imshow("MASK", mask)

	maskEr = cv.erode(mask, None, iterations=2)
	cv.imshow("erode", maskEr)

	maskDi = cv.dilate(mask, None, iterations=2)
	cv.imshow("dilate", maskDi)
	result = cv.bitwise_and(frame, frame, mask=mask)
	cv.imshow("result", result)

	if cv.waitKey(1) == 27:
		break		
cap.release()
cv.destroyAllWindows()