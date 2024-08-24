import numpy as np 
import cv2

cap = cv2.VideoCapture('vid-pic/carPark.mp4')

ret, frame = cap.read()

cv2.imwrite('vid-pic/carParkImg.png', frame)
