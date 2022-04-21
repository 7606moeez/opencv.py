 # import libraries
import cv2 as cv
import numpy as np 

#Read the frame on camera(0)
cap = cv.VideoCapture(0)
frame_width =int(cap.get(3))
frame_height =int(cap.get(4))
out =cv.VideoWriter("resources/output.avi", cv.VideoWriter_fourcc('M','J', 'P', 'G'), 20, (frame_width, frame_height))

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


# cap.set(10,50) brightness level
# cap.set(3,640)width level
# cap.set(4,480)height level
