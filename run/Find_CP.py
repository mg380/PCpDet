#!/usr/bin/python
# Standard imports
import cv2
import numpy as np;
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def OpenImage(name):
    img = cv2.imread(name,cv2.IMREAD_GRAYSCALE)
    #blr = cv2.medianBlur(img,5)
    blr = cv2.blur(img,(10,10))
    th = cv2.adaptiveThreshold(blr,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
    null , th2 = cv2.threshold(blr, 30, 255, cv2.THRESH_BINARY_INV) 
    return img , blr, th , th2

F = "/Users/mariograndi/Desktop/Blob_detection/img/4kx4k/20000X_0043.jpeg"
img , blr, th, th2 = OpenImage(F)

images = [img, blr, th , th2]
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.xticks([]),plt.yticks([])
plt.show()
