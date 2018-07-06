#!/usr/bin/python
# Standard imports
import cv2
import numpy as np;
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math

def OpenImage(name):
#    img = cv2.imread(name,cv2.IMREAD_GRAYSCALE)
    imgo = cv2.imread(name)
    img = cv2.cvtColor(imgo, cv2.COLOR_BGR2GRAY) 
    #blr = cv2.medianBlur(img,5)
    blr = cv2.blur(img,(20,20))
    th = cv2.adaptiveThreshold(blr,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
    null , th2 = cv2.threshold(blr, 45, 255, cv2.THRESH_BINARY_INV) 
    return imgo ,img, blr, th , th2


def findContour(thresh):
    original, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_area = []
    # calculate area and filter into new array
    i=0
    for con in contours:
        i=i+1
        area = cv2.contourArea(con)
        if 320 < area:
            contours_area.append(con)
            contours_circles = []
            # check if contour is of circular shape
    for con in contours_area:
        perimeter = cv2.arcLength(con, True)
        area = cv2.contourArea(con)
        circularity = 4*math.pi*(area/(perimeter*perimeter))
        if 0.6 < circularity:
           # plt.plot(area,circularity,'ro')
           # plt.plot()
            contours_circles.append(con)
    return contours_circles







F = "/Users/mariograndi/Desktop/Blob_detection/img/4kx4k/20000X_0002.jpeg"
imgo ,img , blr, th, th2 = OpenImage(F)
images = [imgo, img, blr, th , th2]

cv2.imshow("original",imgo)
cv2.imshow("blurred",blr)
cv2.imshow("threshold",th2)
cont = findContour(th2)
cv2.drawContours(imgo,cont,-1,(250,100,0),3)
cv2.imshow("contoured",imgo)
cv2.waitKey()

#plt.imshow(th2,'gray')
#for i in range(4):
#    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
#    plt.xticks([]),plt.yticks([])
plt.show()


