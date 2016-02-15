# -*- coding: utf-8 -*-
import numpy as np
import cv2

#Load a color image in grayscale
img = cv2.imread('attachment-1.jpg') # 0 for grayscale and 1 for color.
b,g,r = cv2.split(img)
rgb_img = cv2.merge([r,g,b])

#counting the number of coins
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,210,255,cv2.THRESH_BINARY)

# noise removal
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
#closing = cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel, iterations = 3)
#cv2.imshow('image',opening)

opening, contours, hierarchy = cv2.findContours(opening,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[4]
blobs = []
for c in contours:
    area = cv2.contourArea(c)
    if area > 250:
        blobs.append(c)

#print "length ", len(blobs)

#blobs.remove([])

bb = cv2.drawContours(img, blobs, -1, (0,255,0), 3)

# to show image.
cv2.imshow('image',bb)
cv2.waitKey(0)
cv2.destroyAllWindows()