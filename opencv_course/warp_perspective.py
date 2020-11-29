import cv2,numpy as np

img  = cv2.imread('./img/cards.jpg')


# 140,236  273,214  320,420 177,448

pts1 = np.float32([[140,236],[273,214],[177,448],[320,420]])
pts2 = np.float32([[0,0],[200,0],[0,250],[200,250]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)

final = cv2.warpPerspective(img,matrix,(200,250))

cv2.imshow('img',final)

cv2.waitKey(0)
cv2.destroyAllWindows()
