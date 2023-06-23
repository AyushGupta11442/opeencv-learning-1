import cv2
import numpy as np
print("imported")

img = np.zeros((512,512,3),np.uint8)
# print(img)
# img[:] = 255,0,0  # for all image the colour will be blue

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)   #in this we have to give three para meter mage , starting point  , ending point , colour , no of channel of colour
cv2.rectangle(img,(0,0),(img.shape[1] - 100,img.shape[0] -100),(0,0,255),3)
cv2.circle(img,(400,50),(30),(255,0,255),3)  # in this we have to define image then coordinate of centre then the radius of the circle ,color , channel
cv2.putText(img,"opencv",(300,100),cv2.FONT_HERSHEY_SIMPLEX ,2,(1,150,0) , 1) # in we have to give image, what text to show , coordinate of the text , font of the text , scale , colour , thickness
cv2.imshow("image",img)

cv2.waitKey(0)