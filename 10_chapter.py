#IMAGE SAVING AND WRITING
import cv2 as cv
from cv2 import imshow
from cv2 import imwrite
import numpy as np

img =cv.imread("resources/moeez.jpg")
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# blurr image
blurr_img =cv.GaussianBlur(gray_img, (7,7), 0)
# edges method
edge_img = cv.Canny(img, 48, 48)
# thickness of lines
mat_kernel =np.ones((3,3), np.uint8)      #more thickness

dilate_img = cv.dilate(edge_img, (mat_kernel), iterations =1)

resize_image =cv.resize(img, (500,700))

#cropp image
cropped_img = img[0:350, 0:400]

#making thinner outline
ero_img = cv.erode(dilate_img, mat_kernel, iterations =1)


cv.imshow('original', img)
cv.imshow('gray', gray_img)
cv.imshow('blurr',blurr_img)
cv.imshow('edge',edge_img)
cv.imshow('dilate',dilate_img)
cv.imshow('mat',mat_kernel)
cv.imshow('resize',resize_image)
cv.imshow('eros',ero_img)
cv.imshow('crop',cropped_img)
cv.waitKey(0)
        
    
cv.destroyAllWindows()

#resize_image =cv.resize(img, (350,290))
