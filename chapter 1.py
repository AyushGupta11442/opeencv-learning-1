import cv2
import numpy as np
print("pakage imported")

#  importing image and showing image using open cv


img = cv2.imread("resources/images.jpg")


# to resize
cv2.imshow("Output",img)
print(img.shape)

imgResize = cv2.resize(img,(1000,1000))
print(imgResize.shape)
cv2.imshow("Output1",img)
cv2.waitKey(0)


imagecropped  = img[0:200,200:500]


#
# cv2.imshow("Output",img)
#
# cv2.waitKey(0)


# putting some basic function in photo
# kernal = np.ones((5,5),np.uint8)
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
# imgCanny = cv2.Canny(img,100,200)
# imgdialation = cv2.dilate(imgCanny , kernal, iterations = 1)
# imgeroded = cv2.erode(imgCanny , kernal, iterations = 1)
#
# cv2.imshow("grey image", imgGray)
# cv2.imshow("Blur image", imgBlur)
# cv2.imshow("canny image", imgCanny)
# cv2.imshow("Dialation image", imgdialation)
# cv2.imshow("eroded image", imgeroded)
# cv2.waitKey(0)



# importing video and displaying video using open cv

# cap = cv2.VideoCapture("resources/pexels-christopher-schultz-5927708-1080x1920-30fps.mp4")


# for web cam we use id

# cap = cv2.VideoCapture(0)
# cap.set(3,640)  # defining width
# cap.set(4,480)  # defining height
#
# while True:
#     success , img = cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
