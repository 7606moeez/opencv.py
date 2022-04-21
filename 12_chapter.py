import cv2 as cv
import numpy as np

cap = cv.VideoCapture(1)
# resolution(1280*720)
# cap.set(3,1280)
# cap.set(4, 720)

def hd_resolution():
    cap.set(3,1280)
    cap.set(4, 720) 

hd_resolution()
def fhd_resolution():
    cap.set(3,1280)
    cap.set(4, 720)

# fhd_resolution() 
frame_width =int(cap.get(3))
frame_height =int(cap.get(4))
out =cv.VideoWriter("resources/output1.avi", cv.VideoWriter_fourcc('M','J', 'P', 'G'), 20, (frame_width, frame_height))

# (thresh, binary) =cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
# display frame by frame
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        out.write(frame)
        cv.imshow("video", frame)
        # to quit with 'q':
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
# release and close easily    
cap.release()
out.release()
cv.destroyAllWindows()  
       