#IMAGE SAVING AND WRITING
import cv2 as cv
from cv2 import imshow
from cv2 import imwrite

img =cv.imread("resources/moeez.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


(thresh, binary) =cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
imwrite('resources/Image_gray.jpg', gray)
imwrite('resources/Image_bw.jpg', binary)


# cv.imshow('original', img)
# cv.imshow('gray', gray)
# cv.imshow('black and white', binary)
cv.waitKey(0)
cv.destroyAllWindows()

