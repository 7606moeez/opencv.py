import cv2 as cv
import numpy as np
from matplotlib.colors import is_color_like

cap = cv.VideoCapture(0)
frame_width =int(cap.get(3))
frame_height =int(cap.get(4))
out =cv.VideoWriter("resources/out_video.avi", cv.VideoWriter_fourcc('M', 'J', 'P', 'G'),10, (frame_width, frame_height), isColor =False)

while (True):
    (ret, frame) =cap.read()
    # grayframe =cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # (thresh, binary) =cv.threshold(grayframe, 127, 255, cv.THRESH_BINARY)
    if ret == True:
        out.write(frame)
        cv.imshow("video",frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break 
    else:
        break
cap.release()
out.release()       
cv.destroyAllWindows() 