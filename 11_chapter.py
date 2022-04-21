import numpy as np
import cv2 as cv
# Draw a canvas
img =np.zeros((600,600))
img1 =np.ones((600,600))
# shape a image
print(img.shape)
#Adding a canvas
colored_img = np.zeros((600,600, 3), np.uint8)
colored_img[:] = 350,0,255 #color complete
# part/image of color
colored_img[100:250, 100:300] = 2,0,150
# line of image
cv.line(colored_img,(0,0),(600,600),(255,255,50),2)
#rectangular of image
cv.rectangle(colored_img,(100,100),(150,150),(255,240,0),cv.FILLED)
# Adding a circle
cv.circle(colored_img,(300,300),46, (255,100,0),cv.FILLED) 
# Adding Text 
cv.putText(colored_img,"Moeez with python ka chilla",(67,450),cv.FONT_HERSHEY_DUPLEX, 1 ,(150,50,50),3)








# cv.imshow('zeros',img)
# # cv.imshow('ones',img1)
cv.imshow('Image', colored_img)
cv.waitKey(0)
cv.destroyAllWindows()
