import cv2
import numpy as np
print("imported")

img = np.zeros((512,512))

cv2.imshow("image",img)

cv2.waitKey(0)