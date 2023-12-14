# -*- coding: utf-8 -*-

import cv2 
import numpy as np

cam = cv2.VideoCapture("car9.mp4")

while  cam.isOpened():
    
    ret,frame = cam.read()
    if ret == False:
        break
   
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    row,col = frame.shape[:2]
    def mask(matris):
        x,y = frame.shape[:2]
        mask = np.zeros((x,y),dtype = np.uint8)
        maske = cv2.fillPoly(mask, [matris], 255)
        result = cv2.bitwise_and(frame_gray,frame_gray, mask = maske)
        return result

    
    def edgeDetection(result):
       _ , thresh = cv2.threshold(result,175,255,cv2.THRESH_BINARY)
       k_algılama = cv2.Canny(thresh, 10, 100)
       return k_algılama
        
   
    def drawLines(k_algılama):
       lines = cv2.HoughLinesP(k_algılama, 1, np.pi/180, 1 , 1000 , 1)
       if not isinstance(lines, type(None)):
          for line in lines:
              for x1,y1,x2,y2 in line:
                  cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255),10)
       cv2.imshow("Lane Tracking",frame)
       

   
       
    matris = np.array([[int((3*col)/8) ,int((6*row)/9)], [int((5*col)/8) ,int((6*row)/9)] , 
                      [int((7.2*col)/8) , row -1], [int((0.8*col)/8) ,row - 1]] , dtype=np.int32)
    
    
    drawLines(edgeDetection(mask(matris)))
    
    k = cv2.waitKey(33)
    if k == ord("q"):
        print("video kapatıldı")
        break
cam.release()
cv2.destroyAllWindows()  
