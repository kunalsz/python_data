import cv2,numpy as np 

src = cv2.VideoCapture(0)
src.set(3,480)
src.set(4,640)

colors = [[62,65,107,84,140,209],[10,91,0,22,255,255],[97,54,0,179,207,157]]

realcolors = [[0,255,0],[0,89,255],[255,0,0]]

def empty(a):
    pass

points = []



def findCol(img,colors,realcolors):
    imghsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    count = 0
    newpnts = []

    for col in colors:
        lower = np.array(col[0:3])
        upper = np.array(col[3:6])
        mask = cv2.inRange(imghsv,lower,upper)

        x,y = getcontours(mask)
        cv2.circle(img,(x,y),10,realcolors[count],cv2.FILLED)

        if x!=0 and y!=0:
            newpnts.append([x,y,count])
        count += 1

    return newpnts

def getcontours(img):
    contours,heirarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)  
        if area>500:
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)

            x,y,w,h = cv2.boundingRect(approx)

    return x+w//2,y    



def draw(pts,color):
    for point in pts:
        #cv2.line(imgResult,(point[-3],point[-4]),(point[-1],point[-2]),(255,0,0),10)
        cv2.circle(imgResult,(point[0],point[1]),10,color[point[2]],cv2.FILLED)





while True:
    success, img = src.read()
    imgResult = img.copy()
    newPoints = findCol(img, colors,realcolors)
    if len(newPoints)!=0:
        for newP in newPoints:
            points.append(newP)
    if len(points)!=0:
        draw(points,realcolors)
 
 
    cv2.imshow("Result", imgResult)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break