import numpy as np
import pickle
import cv2
import cvzone

cap = cv2.VideoCapture('vid-pic/carPark.mp4')

with open('CarParkPos', 'rb') as f:
    posList = pickle.load(f)
    # print(posList)
     

width, height = 107, 48

def carParkCheck(imgPro, img):
    
    carParkCount = 0
    for pos in posList:
        x, y = pos
        # Crop 
        carPark_img = imgPro[y:y+height, x:x+width]
        # Count pixels
        countWhite = cv2.countNonZero(carPark_img)

        if countWhite < 900:
            carParkCount += 1
            color = (0, 255, 0) 
        else:
            color = (0, 0, 255)  

        # Draw rectangle
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, 2)
        # Display white pixels 
        cvzone.putTextRect(img, str(countWhite), (x, y + height - 3), scale=1, thickness=2, offset=0, colorR=color)
        
    # Display number of empty parking 
    cvzone.putTextRect(img, f'Free: {carParkCount}/{len(posList)}', (100, 50), scale=3, thickness=5, offset=20, colorR=(0, 200, 0))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv2.medianBlur(imgThreshold, 5)
    imgDilate = cv2.dilate(imgMedian, np.ones((3,3), np.uint8), iterations=1)

    carParkCheck(imgDilate, frame)

    cv2.imshow('Image', frame)
    # cv2.imshow('Threshold', imgThreshold)
    # cv2.imshow('Median', imgMedian)
    # cv2.imshow('Dilate', imgDilate)

    key = cv2.waitKey(25)
    if key == 27 or key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
