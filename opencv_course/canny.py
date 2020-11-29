
import numpy as np 
import cv2

img  = cv2.imread('./img/lena.jpeg')

cannyimg = cv2.Canny(img,100,200)

kernel = np.ones((2,2),np.uint8)
erode = cv2.erode(cannyimg,kernel,iterations=1)
dilate = cv2.dilate(cannyimg,kernel,iterations=1)


cv2.imshow('normal',img) 
cv2.imshow('Canny',cannyimg) 
cv2.imshow('Erode',erode) 
cv2.imshow('Dilate',dilate) 

cv2.waitKey(0)
cv2.destroyAllWindows()