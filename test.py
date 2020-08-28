import cv2 as cv
import numpy as np
img=cv.imread('1.png',cv.IMREAD_COLOR)
cv.imshow('image', img)
cv.waitKey(0) 
cv.destroyAllWindows()