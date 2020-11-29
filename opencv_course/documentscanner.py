import cv2
import numpy as np

src = cv2.VideoCapture(0)

def getcontours(img):

    canny = cv2.Canny(img,150,150)

    kernel = np.ones((5,5),np.uint8)

    canny = cv2.erode(canny,kernel,iterations=1)

    contours,heirarchy = cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        maxarea = 0
        area = cv2.contourArea(cnt)
        biggest = np.array([])

        if area>5000:

            peri  = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)

            if area>maxarea and len(approx)==4:
                biggest=approx
                maxarea = area
                print(biggest)

        #x,y,w,h = cv2.boundingRect(approx)

    cv2.drawContours(img,biggest,-1,(255,0,0),3)


while True:
    ret,frame = src.read()

    #newcnt = getcontours(frame)
    #cv2.drawContours(frame,newcnt,-1,(255,0,0),4)

    
    cv2.imshow('final',frame)
    cv2.waitKey(1)