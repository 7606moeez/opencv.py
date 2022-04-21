import cv2 as cv
import numpy as np 
# from cv2 import cvtColor
img =cv.imread("resources/mahad.jpg")
img=cv.resize(img, (400,600))

# gray_img =cvtColor(img, cv.COLOR_BGR2GRAY)



cv.imshow("Pehli Image", img)
# cv.imshow("Gray Image", gray_img)

cv.waitKey(0)
cv.destroyAllWindows()