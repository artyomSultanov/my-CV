import cv2 as cv
import numpy as np

i = 1
while i < 4:
	frame = cv.imread(str(i) + '.jpeg')
	frame = cv.resize(frame, (60, 120))
	cv.imshow(str(i), frame)

	cutedFrame = frame[20:101, 8:52]
	cv.imshow("cutedFrame" + str(i), cutedFrame)

	hsv = cv.cvtColor(cutedFrame, cv.COLOR_BGR2HSV)
	v = hsv[:, :, 2]
	cv.imshow('v' + str(i), v)

	red_sum = np.sum(v[0:27, 0:44])
	yellow_sum = np.sum(v[28:54, 0:44])
	green_sum = np.sum(v[55:81, 0:44])

	cv.rectangle(cutedFrame, (0, 0), (44, 27), (0, 0, 255), 2)
	cv.rectangle(cutedFrame, (0, 28), (44, 54), (0, 255, 255), 2)
	cv.rectangle(cutedFrame, (0, 55), (44, 81), (0, 255, 0), 2)
	cv.imshow("frameCopy" + str(i), cutedFrame)

	print(str(red_sum) + ' : ' + str(yellow_sum) + ' : ' + str(green_sum))

	if green_sum > yellow_sum and green_sum > red_sum:
		print('green')
	elif yellow_sum > green_sum and yellow_sum > red_sum:
		print('yellow')
	else:
		print('red')

	key = cv.waitKey(1)
	if key == ord("n"):
		i += 1

	if key == 27:
		break

cv.destroyAllWindows()