# READING A VIDEO
import cv2 as cv
cap = cv.VideoCapture('resources/Money heist.mp4')

if (cap.isOpened() == False):
    print("error in reading video")

    # reading and playing
while(cap.isOpened()):
    ret, frame =cap.read()
    if ret == True:
        cv.imshow("Money heist", frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()       
cv.destroyAllWindows()        
