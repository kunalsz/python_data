import cv2,numpy as np 

src = cv2.VideoCapture(0)
src.set(3,320)
src.set(4,580)

while True:
    ret,frame = src.read()

    cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

    faces = cascade.detectMultiScale(frame,1.05,4)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow('vid',frame)

    cv2.waitKey(1)











"""
img = cv2.imread('./img/lena.jpeg')

cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

faces = cascade.detectMultiScale(img,1.05,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow('final',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""