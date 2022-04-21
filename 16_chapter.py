import cv2 as cv 
import numpy as np 
from cv2 import imshow

# img = cv.imread('resources/moeez.jpg')
# sliders
def slider():
    pass
path = "resources/wrap.jpg"
cv.namedWindow("Bars")
cv.resizeWindow("Bars", 640,300)
cv.createTrackbar("Hue_min", "Bars", 0, 179, slider)
cv.createTrackbar("Hue_max", "Bars", 179, 179, slider)
cv.createTrackbar("sat_min", "Bars", 0, 255, slider)
cv.createTrackbar("sat_max", "Bars", 255,255, slider)
cv.createTrackbar("val_min", "Bars", 0,255, slider)
cv.createTrackbar("val_max", "Bars", 255, 255, slider)

img = cv.imread(path)
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)


# Hue_min = cv.getTrackbarPos("Hue_min", "Bars")
# print(Hue_min)

while True:
    img = cv.imread(path)
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    Hue_min = cv.getTrackbarPos("Hue_min", "Bars")
    Hue_max = cv.getTrackbarPos("Hue_max", "Bars")
    sat_min = cv.getTrackbarPos("sat_min", "Bars")
    sat_max = cv.getTrackbarPos("sat_max", "Bars")
    val_min = cv.getTrackbarPos("val_min", "Bars")
    val_max = cv.getTrackbarPos("val_max", "Bars")
    print(Hue_min,Hue_max,sat_min,sat_max,val_min,val_max)
#    lower array
    lower = np.array([Hue_min, sat_min, val_min])
    upper = np.array([Hue_max, sat_max, val_max])
    mask_img = cv.inRange(hsv_img, lower, upper)
    out_img = cv.bitwise_and(img,img,  mask =mask_img)
    cv.imshow("Original", img)
    cv.imshow("HSV", hsv_img)
    cv.imshow("mask", mask_img)
    cv.imshow("out", out_img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cv.destroyAllWindows()
