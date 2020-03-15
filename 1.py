import numpy as np
import cv2

img = cv2.imread('Buoy.jpeg')

# filters
blur = cv2.blur(img,(5,5))
blur0=cv2.medianBlur(blur,5)
blur1= cv2.GaussianBlur(blur0,(5,5),0)
blur2= cv2.bilateralFilter(blur1,9,75,75)


gray_image = cv2.cvtColor(blur2, cv2.COLOR_BGR2GRAY)

# convert the grayscale image to binary image
ret,thresh = cv2.threshold(gray_image,135,255,0)

# find contours in the binary image
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(str(len(contours)))
cv2.drawContours(img, contours, -1, (0,255,0), 3)
        
	
    
for c in contours:
   
   M = cv2.moments(c)
   cX = int(M["m10"] / M["m00"])
   cY = int(M["m01"] / M["m00"])
   cv2.circle(img, (cX, cY), 5, (255, 255, 255), -1)
   print(cX,cY)


   # display the image
   cv2.imshow("Image", img)
   cv2.waitKey(0)
