# split video into frames
import cv2 as cv
import numpy as np

cap = cv.VideoCapture("resources/Money heist.mp4")

frameNr = 0

while (True):
    success, frame = cap.read()
    if success:
        cv.imwrite(f"resources/frames/frame_{frameNr}.jpg", frame) # convert video to jpg (image)    
    else:
        break

    frameNr = frameNr+1

cap.release()