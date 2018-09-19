#!/usr/bin/python
# Standard imports
import cv2
import numpy as np;
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math
import os
import sys

def OpenImage(name):
#    img = cv2.imread(name,cv2.IMREAD_GRAYSCALE)
    imgo = cv2.imread(name)
    img = cv2.cvtColor(imgo, cv2.COLOR_BGR2GRAY) 
    #img = cv2.imread(name, cv2.COLOR_BGR2GRAY) 
    #blr = cv2.medianBlur(img,5)
    blr = cv2.blur(img,(20,20))
    #null , th = cv2.threshold(blr, 45, 255, cv2.THRESH_BINARY_INV)
    #th = cv2.adaptiveThreshold(blr,225,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    null , th = cv2.threshold(blr, 70, 255, cv2.THRESH_BINARY_INV)
    kernel = np.ones((5,5),np.uint8)
    ero = cv2.erode(th,kernel,iterations = 1) 
    th_alt =cv2.blur(th,(2,2))
    return imgo ,img, blr, th, ero


def findContour(thresh):
    original, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_area = []
    contours_circles = []
    # calculate area and filter into new array
    i=0
    print("area")
    for con in contours:
        i=i+1
        area = cv2.contourArea(con)
        if 1000 < area:
            print(area)
            contours_area.append(con)
            # check if contour is of circular shape
    #a=len(contours_area)
    #print(a)
    print("cont")
    for con in contours_area:
        perimeter = cv2.arcLength(con, True)
        area = cv2.contourArea(con)
        circularity = 4*math.pi*(area/(perimeter*perimeter))
        if 0.4 < circularity:
            print(circularity)
            # plt.plot(area,circularity,'ro')
            # plt.plot()
            contours_circles.append(con)
    return contours_circles


 
F = "/Users/mariograndi/Desktop/Mario/Blob_detection/img/4kx4k/20000X_0043.jpeg"
imgo ,img , blr, th, th2 = OpenImage(F)
images = [imgo, img, blr, th , th2]

cv2.imshow("original",cv2.resize(imgo,(600,600)))
cv2.imshow("blurred",cv2.resize(blr,(600,600)))
cv2.imshow("eroded",cv2.resize(th2,(600,600)))
cv2.imshow("threshold",cv2.resize(th,(600,600)))
cont = findContour(th2)
cv2.drawContours(imgo,cont,-1,(250,100,0),3)
cv2.imshow("contoured",cv2.resize(imgo,(600,600)))

#small = cv2.resize(imgo, (600,600)) 
#cv2.imshow("smaller",small)

#plt.imshow(th2,'gray')
# for i in range(4):
#     plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
#     plt.xticks([]),plt.yticks([])
#     sys.stdout.write('\r')
#     # the exact output you're looking for:
#     sys.stdout.write("[%-20s] %d%%" % ('='*i, 1*i))
#     sys.stdout.flush()
    
#plt.show()
cv2.waitKey()
cv2.destroyAllWindows()
