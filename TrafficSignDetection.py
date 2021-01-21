import cv2 as cv
import numpy as np


cap =cv.VideoCapture(0)

pedestrian = cv.resize(cv.imread("pedestrianR.jpg"), (64, 64))
no_drive = cv.resize(cv.imread("noDriveR.jpg"), (64, 64))
brick = cv.resize(cv.imread("brick.jpg"), (64, 64))
give_way = cv.resize(cv.imread("giveWay.jpg"), (64, 64))
speedBump_and_roadWorks = cv.resize(cv.imread("speedBump.jpg"), (64, 64))
stop = cv.resize(cv.imread("stop.png"), (64, 64))
parking = cv.resize(cv.imread("parking.jpg"), (64, 64))



cv.imshow("pedestrian", pedestrian)
cv.imshow("no_drive",no_drive)
cv.imshow("brick",brick)
cv.imshow("giveWay",give_way)
cv.imshow("speedBump",speedBump_and_roadWorks)
cv.imshow("stop",stop)
cv.imshow("parking",parking)

 

cv.imshow("pedestrianBIN", pedestrian)
cv.imshow("no_driveBIN",no_drive)
cv.imshow("brickBIN",brick)
cv.imshow("giveWayBIN",give_way)
cv.imshow("speedBumpBIN",speedBump_and_roadWorks)
cv.imshow("stopBIN",stop)
cv.imshow("parkingBIN",parking)

while (True):
    ret,frame= cap.read()
    frameBase = frame.copy()
    cv.imshow("frame",frame)

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    cv.imshow("hsv",hsv)
    blur = cv.blur(hsv, (5, 5))
    # cv.imshow("blur", blur)
    thresh = cv.inRange(blur, (89, 124, 73), (255, 255, 255))   # Это пороги для детектирования
    # cv.imshow("thresh", thresh)
    thresh = cv.erode(thresh, None, iterations=2)
    thresh = cv.dilate(thresh, None, iterations=5)
    cv.imshow("mask", thresh)

    countours = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)  # cv.CHAIN_APPROX_SIMPLE
    countours = countours[1]

    if countours:
        countours = sorted(countours, key=cv.contourArea, reverse=True)
        cv.drawContours(frame, countours[0], -1, (255, 0, 255), 3)
        cv.imshow("countour", frame)

        rect = cv.minAreaRect(countours[0])
        box = np.int0(cv.boxPoints(rect))
        cv.drawContours(frame, [box], -1, (0, 255, 0), 3)

        (x, y, w, h) = cv.boundingRect(countours[0])
        cv.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), thickness=2, lineType=8, shift=0)
        #cv.imshow("Detect", frame)
        roiImg = frameBase[y:y + h, x:x + w]
        cv.imshow("Detect", roiImg)

        resizedRoi = cv.resize(roiImg, (64, 64))
        cv.imshow("ResizedRoi", resizedRoi)
        sign = cv.inRange(resizedRoi, (89, 124, 73), (255, 255, 255))     # Это пороги для распознавания
        cv.imshow("sign",sign)


        pedestrian_val=0
        no_drive_val=0
        brick_val=0
        stop_val=0
        park_val=0
        give_way_val=0
        sB_and_rW_val=0

        for i in range(64):
            for j in range(64):
                if (sign[i][j]==pedestrian[i][j]):
                    pedestrian_val+=1
                if (sign[i][j]==no_drive[i][j]):
                    no_drive_val+=1
                if (sign[i][j]==brick[i][j]):
                    brick_val+=1
                if (sign[i][j]==stop[i][j]):
                    stop_val+=1
                if (sign[i][j]==give_way[i][j]):
                    give_way_val+=1
                if (sign[i][j]==speedBump_and_roadWorks[i][j]):
                    sB_and_rW_val+=1
                if (sign[i][j]==parking[i][j]):
                    park_val+=1

        # print ('ped_val: ' + str(pedestrian_val))
        # print ('nodri_vl: ' + str(no_drive_val))
        # print ('brick_val: ' + str(brick_val))
        # print ('stop_val: ' + str(stop_val))
        # print ('park_val: ' + str(park_val))
        # print ('gvWay_val: ' + str(give_way_val))
        # print ('SBaRW_val: ' + str(sB_and_rW_val))

        valDict =  {
                    'pedestrian': pedestrian_val,
                    'no drive': no_drive_val,
                    'brick': brick_val,
                    'stop': stop_val,
                    'parking': park_val,
                    'give way': give_way_val,
                    'speed bump and working of road': sB_and_rW_val
                   }

        valArr = valDict.items()
        maxVal = 0

        for k, v in valArr:
            if v > maxVal:
                maxVal = v
        for k, v in valArr:
            if v == maxVal:
                print(k)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
