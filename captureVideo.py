import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fps = cap.get(cv2.CAP_PROP_FPS)

angle = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
    	cv2.imshow("image", frame)

    cv2.waitKey(5)


cap.release()
cv2.destroyAllWindows()
