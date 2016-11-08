import numpy as np
import cv2, sys

# opens a webcam with -w or opens a file as 1st arg
if sys.argv[1] == "-w":
    src = cv2.VideoCapture(0)
else:
    src = cv2.VideoCapture(sys.argv[1])

distCoeff = np.zeros((4,1),np.float64)

k1 = -1.0e-5; # warping
k2 = 0.0;
p1 = 0.0;
p2 = 0.0;

distCoeff[0,0] = k1;
distCoeff[1,0] = k2;
distCoeff[2,0] = p1;
distCoeff[3,0] = p2;

cam = np.eye(3,dtype=np.float32)

while True:
    ret, frame = src.read()
    width, height, ch = frame.shape

    cam[0,2] = width/2.0  # define center x
    cam[1,2] = height/2.0 # define center y
    cam[0,0] = 10.        # define focal length x
    cam[1,1] = 10.        # define focal length y

    dst = cv2.undistort(frame,cam,distCoeff)

    cv2.imshow('dst',dst)
    cv2.waitKey(5)
cv2.destroyAllWindows()