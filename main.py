# -*- coding: utf-8 -*-
import numpy as np
import cv2

#Load a color image in grayscale
img = cv2.imread('coins.jpg',0) # 0 for grayscale and 1 for color.
cv2.imshow('image',img)
cv2.waitKey(0) # waits until a key press event occurs.
cv2.destroyAllWindows()