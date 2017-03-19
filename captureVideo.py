import cv2, imutils
import numpy as np

cap = cv2.VideoCapture(0)
fps = cap.get(cv2.CAP_PROP_FPS)

angle = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
    	rotated = imutils.rotate_bound(frame, angle)
    	cv2.imshow("Rotated (Correct)", rotated)
        angle+=45
    cv2.waitKey(5)


cap.release()
cv2.destroyAllWindows()
