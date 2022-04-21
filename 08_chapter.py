# import libraries
import cv2 as cv
import numpy as np 
from cv2 import cvtColor

#Read the frame on camera(0)
cap = cv.VideoCapture(0)
# display frame by frame
while (True):
    (ret, frame) =cap.read()
    # gray_frame =cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # (thresh, binary) =cv.threshold(gray_frame, 127, 255, cv.THRESH_BINARY)
    if ret == True:

        cv.imshow("original Cam", frame)
        # cv.imshow("gray Cam", gray_frame)
        # cv.imshow("b_w Cam", binary)


        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
# release and close easily    
cap.release()
cv.destroyAllWindows()        
