import cv2 as cv
import numpy as np
# define a function
def find_coord(event, x, y,flags, params):
    if event == cv.EVENT_FLAG_LBUTTON:
        print(x,'', y)
        #left mouse click
        font =cv.FONT_HERSHEY_PLAIN
        cv.putText(img, str(x) +','+ str(y), (x,y), font, 1, (255,255,0),2 )#text, org, fontFace, fontScale, color)
        cv.imshow("image", img)
    if event == cv.EVENT_RBUTTONDOWN:
        print(x,'' ,y)
        font = cv.FONT_HERSHEY_SIMPLEX
        b = img[y,x,0]
        g = img[y,x,1]
        r = img[y,x,2]
        cv.putText(img, str(b)+ ',' +str(g)+ ',' + str(r), (x,y),font, 1, (42,61,50), 2) #text, org, fontFace, fontScale, color)
        cv.imshow("image", img)



# final function and display
if __name__=="__main__":
    img = cv.imread("resources/wrap.jpg", 1)
    cv.imshow('image', img)
    cv.setMouseCallback("image", find_coord)
    cv.waitKey(0)
    cv.destroyAllWindows()