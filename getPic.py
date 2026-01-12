import numpy as np
import cv2 as cv
import time
import os
from threading import Thread

link = "rtsp://192.168.1.137:8554/live.sdp"
cap = cv.VideoCapture(link)
lastTime = 0
n = 1

text = "Camera Disconnected"
coordinates = (0,100)
font = cv.FONT_HERSHEY_SIMPLEX
fontScale = 1
color = (0,0,255)
thickness = 2


if not cap.isOpened():
 print("Cannot open camera")
 exit()

lastFrame = 0
while True:
 # Capture frame-by-frame
 ret, frame = cap.read()
 # if frame is read correctly ret is True
 if not ret:
     cap.release()
     print("Can't receive frame (stream end?).")
     lastFrame = cv.putText(lastFrame, text, coordinates, font, fontScale, color, thickness, cv.LINE_AA)
     cv.imshow('frame', lastFrame)
     if (time.time()-lastTime)>2:
         cap = cv.VideoCapture(link)
         lastTime = time.time()
 # Our operations on the frame come here
 # Display the resulting frame
 else:
     frame = cv.rotate(frame, cv.ROTATE_90_CLOCKWISE)
     cv.imshow("frame",frame)
     lastFrame = frame
     if (time.time()-lastTime)>0.1:
          cv.imwrite('./captures/'+ str(n) +'.jpg',frame)
          n=n+1
          lastTime = time.time()
          if(n-10)>0: 
              os.remove('./captures/'+ str(n-10) +'.jpg')
 if cv.waitKey(1) == ord('q'):
     break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
