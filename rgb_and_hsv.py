import cv2 as cv

rgb = cv.imread("RGB.jpeg")
rgb = cv.resize(rgb, (700, 350))
cv.imshow("rgb", rgb)

b = rgb[:, :, 0]
g = rgb[:, :, 1]
r = rgb[:, :, 2]

cv.imshow('b', b)
cv.imshow('g', g)
cv.imshow('r', r)

hsv = cv.cvtColor(rgb, cv.COLOR_BGR2HSV)

h = hsv[:, :, 0]
s = hsv[:, :, 1]
v = hsv[:, :, 2]

cv.imshow('h', h)
cv.imshow('s', s)
cv.imshow('v', v)

while True:


	if cv.waitKey(1) == 27:
		break

cv.destroyAllWindows()
 
