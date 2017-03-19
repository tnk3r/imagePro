import numpy as np
import cv2, sys

if sys.argv[1] == "-w":
    src = cv2.VideoCapture(0)
else:
    src = cv2.VideoCapture(sys.argv[1])


while True:
    ret, frame = src.read()
    ## Half the Size // double the proc speed
    height, width = frame.shape[:2]
    res = cv2.resize(frame,(width/2, height/2), interpolation = cv2.INTER_CUBIC)


    cv2.imshow('frame',res)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

src.release()
cv2.destroyAllWindows()
