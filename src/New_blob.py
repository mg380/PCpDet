#!/usr/bin/python                                                                                  
# Standard imports                                                                                 
import cv2                                                                                         
import numpy as np;                                                                                
import matplotlib.pyplot as plt                                                                    
import matplotlib.image as mpimg                                                                   
import math                                
                                                                                                                                              
# Read image                                                                                   
im = cv2.imread("/Users/mariograndi/Desktop/figb.jpg")                       
#params = cv2.SimpleBlobDetector_Params()       
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) 

#imgray = cv2.bitwise_not(imgray)    

#cv2.imshow("imgray",imgray)                                                                                                   
#cv2.waitKey(0)  

#lower_white = np.array(35, dtype = "uint16")                                                                                                  
#upper_white = np.array(255, dtype = "uint16")                                                                                                 
                                                                                                                                              
#mask = cv2.inRange(imgray, lower_white, upper_white)  
#mask = cv2.bitwise_not(mask)
  
cv2.imshow("imgray",imgray)
#cv2.waitKey(0)
#cv2.imshow("mask",mask)
#cv2.imwrite('figb_mask.jpg',mask)
#cv2.waitKey(0)


#img = cv2.imread("/Users/mariograndi/Desktop/figb_mask.jpg") 
#imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

#imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
#im_gauss = cv2.GaussianBlur(imgray, (5, 5), 0)
#im_gauss = imgray
#ret, thresh = cv2.threshold(im_gauss, 127, 255, cv2.THRESH_BINARY)
ret, thresh = cv2.threshold(imgray, 50, 255, cv2.THRESH_BINARY_INV)
# get contours
thresh = cv2.erode(thresh, None, iterations=2)
#thresh = cv2.dilate(thresh, None, iterations=4)

cv2.imshow("thresh",thresh)                                                                                                                                                          
#cv2.waitKey(0)  

im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#cv2.imshow("im2",im2)
#cv2.waitKey(0)


contours_area = []
# calculate area and filter into new array
i=0
for con in contours:
    i=i+1
    area = cv2.contourArea(con)
    if 150 < area < 400:
        print (str(area)+"   ---->  "+str(i))
        contours_area.append(con)


contours_cirles = []

# check if contour is of circular shape
for con in contours_area:
    perimeter = cv2.arcLength(con, True)
    area = cv2.contourArea(con)
    if perimeter == 0:
        continue
    circularity = 4*math.pi*(area/(perimeter*perimeter))
    print (circularity)
    if 0.4 < circularity:
        print ("post : " + str(circularity))
        contours_cirles.append(con)


#print (contours_cirles)

cv2.drawContours(im, contours_cirles, -1, (255,0,0), 3)




cv2.imshow("cont",im)
cv2.waitKey(0)
