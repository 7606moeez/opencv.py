import cv2 as cv
import numpy as np

img = cv.imread('resources/wrap.jpg')
# print(img.shape)

point1 = np.float32([[80,251],[376,125],[196,466],[500,278]])
# width = 532
# height = 594
width, height = 500, 360

point2 = np.float32([[0,0],[532,0],[0,400],[width,height]])


matrix = cv.getPerspectiveTransform(point1, point2)
out_img = cv.warpPerspective(img, matrix,(width, height))

cv.imwrite('resources/wrapp.jpg', out_img) 


cv.imshow('image', img)
cv.imshow('transform', out_img)
cv.waitKey(0)
cv.destroyAllWindows()