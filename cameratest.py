#!/usr/bin/python
# -*- coding: utf-8 -*-
import cv2
import time
 
AUTO = True # Take pictures automatically, or manually press the s key to take pictures
 INTERVAL = 2 # Automatic photo interval
 
 
cv2.namedWindow("left")
cv2.namedWindow("right")
cv2.moveWindow("left", 0, 0)
cv2.moveWindow("right", 400, 0)
left_camera = cv2.VideoCapture(0 + cv2.CAP_DSHOW)#left
 cv2.VideoCapture.set(left_camera, 3, 480) # Property identifier here is required to be int
 cv2.VideoCapture.set(left_camera, 4, 640) # 3 means CV_CAP_PROP_FRAME_WIDTH, set to 270. (Set to 1 and 270 have the same effect)
 right_camera = cv2.VideoCapture(1 + cv2.CAP_DSHOW)#right
cv2.VideoCapture.set(right_camera, 3, 480)
cv2.VideoCapture.set(right_camera, 4, 640)
 
counter = 0
utc = time.time()
 pattern = (12, 8) # Checkerboard size
 folder = "./snapshot/test1/" # Photo file directory
 
def shot(pos, frame):
    global counter
    path = folder + pos + "_" + str(counter) + ".jpg"
 
    cv2.imwrite(path, frame)
    print("snapshot saved into: " + path)
 
while True:
    ret, left_frame = left_camera.read()
    ret, right_frame = right_camera.read()
 
    cv2.imshow("left", left_frame)
    cv2.imshow("right", right_frame)
 
    now = time.time()
    if AUTO and now - utc >= INTERVAL:
        shot("left", left_frame)
        shot("right", right_frame)
        counter += 1
        utc = now
 
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    elif key == ord("s"):
        shot("left", left_frame)
        shot("right", right_frame)
        counter += 1
 
left_camera.release()
right_camera.release()
cv2.destroyWindow("left")
cv2.destroyWindow("right")
