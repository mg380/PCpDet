#!/usr/bin/python
# Standard imports
import cv2
import numpy as np;
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Read image
im = cv2.imread("/Users/mariograndi/Desktop/figb.jpg", cv2.IMREAD_GRAYSCALE)
params = cv2.SimpleBlobDetector_Params()
#cv2.imshow("im", im) 
#cv2.waitKey(0) 

lower_white = np.array(30, dtype = "uint16")
upper_white = np.array(255, dtype = "uint16")

black_mask = cv2.inRange(im, lower_white, upper_white)
inv_mask = cv2.bitwise_not(black_mask)
img = im
#res = cv2.bitwise_not(img, img, inv_mask)

cv2.imshow('mask',black_mask)                                                
cv2.waitKey(0) 

bk = np.full(img.shape, 255, dtype=np.uint8)  # white bk

# get masked foreground
fg_masked = cv2.bitwise_and(img, img, mask=black_mask)
# get masked background, mask must be inverted 
#mask = cv2.bitwise_not(mask)
bk_masked = cv2.bitwise_and(bk, bk, mask=inv_mask)

# combine masked foreground and masked background 
final = cv2.bitwise_or(fg_masked, bk_masked)
#mask = cv2.bitwise_not(mask)  # revert mask to original

#cv2.imshow('final',final)
#cv2.waitKey(0)


params.minThreshold = 100
#params.maxThreshold = 200
#params.thresholdStep = 0.5

params.filterByInertia = False
#params.filterByArea = False
#params.minArea = 10
#params.maxArea = 10000

params.filterByArea = True
params.minArea = 10
params.maxArea = 20000


params.filterByColor = True
#cv2.blobColor = 0
cv2.blobColor = 255

params.filterByConvexity = True
cv2.minConvexity = 1

print (params.filterByColor)
print (params.filterByArea)
print (params.filterByCircularity)
print (params.filterByInertia)
print (params.filterByConvexity)

#blur = cv2.GaussianBlur(im,(5,5),0)
#print (blur)

# Filter by Area.
#params.filterByArea = True
#params.minArea = 1500

# Filter by Circularity
#params.filterByCircularity = True
#params.minCircularity = 0.1

# Filter by Convexity
#params.filterByConvexity = True
#params.minConvexity = 0.87
    
# Filter by Inertia
#params.filterByInertia = True
#params.minInertiaRatio = 0.01

# Create a detector with the parameters
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3 :
    detector = cv2.SimpleBlobDetector(params)
else : 
    detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs.
keypoints = detector.detect(im)
print ("keypoints: ")
print (keypoints)
# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
# the size of the circle corresponds to the size of blob

im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

mask_with_keypoints = cv2.drawKeypoints(black_mask, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("mask with keypoints", mask_with_keypoints) 
cv2.waitKey(0) 
if (1 == 1):
#     Show blobs
    cv2.imshow("Keypoints", im_with_keypoints)
    k = cv2.waitKey(0)
    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()
    elif k == ord('s'): # wait for 's' key to save and exit
        #    cv2.imwrite('messigray.png',img)
        cv2.destroyAllWindows()
    
