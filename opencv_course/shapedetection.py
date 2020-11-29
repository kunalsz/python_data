import cv2,numpy as np 

img = cv2.imread('./img/shapes.png')

canny = cv2.Canny(img,50,100)

contours,heirarchy = cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

for cnt in contours:
    area = cv2.contourArea(cnt)
    print(area)

    peri = cv2.arcLength(cnt,True)

    approx = cv2.approxPolyDP(cnt,0.02*peri,True)
    
    lenap  = len(approx)

    x,y,w,h =cv2.boundingRect(approx)

    cv2.drawContours(img,cnt,-1,(255,0,255),3)

cv2.imshow('original',img)
cv2.imshow('canny',canny)

cv2.waitKey(0)
cv2.destroyAllWindows()