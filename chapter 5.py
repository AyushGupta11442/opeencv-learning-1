import cv2
import numpy as np


def empty():
    pass

path = "resources/images.jpg"
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",640,240)
cv2.createTrackbar("hue min ","Trackbars",0,170,empty)
cv2.createTrackbar("hue max ","Trackbars",179,170,empty)
cv2.createTrackbar("sat min ","Trackbars",0,255,empty)
cv2.createTrackbar("sat max ","Trackbars",255,255,empty)
cv2.createTrackbar("val min ","Trackbars",0,255,empty)
cv2.createTrackbar("val max ","Trackbars",180,255,empty)


while True:
    img = cv2.imread(path)
    imgHsv = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("hue min ","Trackbars")
    h_max = cv2.getTrackbarPos("hue max ", "Trackbars")
    s_min = cv2.getTrackbarPos("sat min ", "Trackbars")
    s_max = cv2.getTrackbarPos("sat max ", "Trackbars")
    v_min = cv2.getTrackbarPos("val min ", "Trackbars")
    v_max = cv2.getTrackbarPos("val max ", "Trackbars")
    lower = np.array([h_min,s_min,v_min])
    uper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHsv , lower,uper)
    # by this function we are masking like whatever in the while will be masked and whatever in the black is masked out so just for reference  i had put the 180 in hmax
    # to get that masked image from the original image this is the following code



    imgresult  = cv2.bitwise_and(img , img , mask = mask)   #what it does is it will take two images and do and of both like where pixel is present in both the image then it will show that pixel or it will not showe the pixrl







    # cv2.imshow("original",img)
    # cv2.imshow("HSV",imgHsv)
    # cv2.imshow("mask", mask)
    # cv2.imshow("masked image", imgresult)

    def stackImages(scale,imgArray):
        rows = len(imgArray)
        cols = len(imgArray[0])
        rowsAvailable = isinstance(imgArray[0], list)
        width = imgArray[0][0].shape[1]
        height = imgArray[0][0].shape[0]
        if rowsAvailable:
            for x in range ( 0, rows):
                for y in range(0, cols):
                    if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                        imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                    else:
                        imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                    if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
            imageBlank = np.zeros((height, width, 3), np.uint8)
            hor = [imageBlank]*rows
            hor_con = [imageBlank]*rows
            for x in range(0, rows):
                hor[x] = np.hstack(imgArray[x])
            ver = np.vstack(hor)
        else:
            for x in range(0, rows):
                if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                    imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
                else:
                    imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
                if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
            hor= np.hstack(imgArray)
            ver = hor
        return ver


    imagstacked = stackImages(0.6,([img , imgHsv],[mask,imgresult]))
    cv2.imshow("image stacked" , imagstacked)


    cv2.waitKey(1)

