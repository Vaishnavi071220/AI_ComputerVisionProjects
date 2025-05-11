import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
#print(img)
#img[:]= 255,0,0 # colon is for limits/range

cv2.line(img,(0,0), (img.shape[1],img.shape[0]), (0,255,0), 3)
cv2.rectangle(img,(0,0), (250,350), (0,0,255), cv2.FILLED)
cv2.circle(img,(400,50),50,(255,255,0),5)

cv2.putText(img, "Hello, my name is Vaishnavi",(10,500),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2,cv2.LINE_AA)
cv2.imshow("Image",img)

cv2.waitKey(0)