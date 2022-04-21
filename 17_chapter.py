#  DECTECTION IN IMAGE
import cv2 as cv 
img = cv.imread("resources/moeez.jpg")
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
face_cascade = cv.CascadeClassifier('resources/haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray_img, 1.1, 4)
# draw a rectangle
for (x,y,w,h) in faces:
    cv.rectangle(img, (x,y), (x+w, y+h), (255,0,255),2)
cv.imshow("original", img)
cv.waitKey(0)
cv.destroyAllWindows()