import cv2,numpy as np 



def empty(a):
    pass

cv2.namedWindow('Trackbars')
cv2.resizeWindow('Trackbars',900,400)

cv2.createTrackbar('hue min','Trackbars',0,179,empty)
cv2.createTrackbar('hue max','Trackbars',179,179,empty)
cv2.createTrackbar('sat min','Trackbars',0,255,empty)
cv2.createTrackbar('sat max','Trackbars',255,255,empty)
cv2.createTrackbar('val min','Trackbars',0,255,empty)
cv2.createTrackbar('val max','Trackbars',255,255,empty)



while True:
    img = cv2.imread('./img/cards.jpg')
    imghsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    hmin = cv2.getTrackbarPos('hue min','Trackbars')
    hmax = cv2.getTrackbarPos('hue max','Trackbars')
    smin = cv2.getTrackbarPos('sat min','Trackbars')
    smax = cv2.getTrackbarPos('sat max','Trackbars')
    vmin = cv2.getTrackbarPos('val min','Trackbars')
    vmax = cv2.getTrackbarPos('val max','Trackbars')

    lower = np.array([hmin,smin,vmin])
    upper = np.array([hmax,smax,vmax])

    mask = cv2.inRange(imghsv,lower,upper)

    imgFinal = cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow('Result',imgFinal)

    cv2.waitKey(1)


