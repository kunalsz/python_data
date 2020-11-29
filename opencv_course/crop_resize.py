import cv2,numpy as np 

img = cv2.imread('./img/lena.jpeg')

imgcrop = img[0:200,0:300]
imgresize = cv2.resize(img,(500,500))

cv2.imshow('croppped',imgcrop)
cv2.imshow('resize',imgresize)



cv2.waitKey(0)
cv2.destroyAllWindows()