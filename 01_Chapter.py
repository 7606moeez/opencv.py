import cv2 as cv
import numpy as np 
from cv2 import cvtColor
img =cv.imread("resources/img.jpg.jpg")
gray_img =cvtColor(img, cv.COLOR_BGR2GRAY)

blurr_img =cv.GaussianBlur(img, (23,23), 2)


resized_img =cv.resize(img ,(450,250))





cv.imshow("Pehli Image", img)
# cv.imshow("dossri image", resized_img)
cv.imshow("teesri image", gray_img)
cv.imshow("Blurr image", blurr_img)

cv.waitKey(0)
cv.destroyAllWindows()

