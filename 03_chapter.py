import cv2 as cv
from cv2 import cvtColor
img =cv.imread("resources/moeez.jpg")
# img =cv.resize(img, (800,600))
gray_img =cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow("original",img)
cv.imshow("gray image",gray_img)

cv.waitKey() 