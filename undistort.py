import numpy as np
import cv2
import sys

# K = np.array([[1755.04324, 0., 650.63], [0, 1754.95349, 545.9389],[0, 0, 1]])
# d = np.array([.16858, 0.57600, 0, 0, 0]) # just use first two terms
K = np.array([[1280, 0, 720], [0, 1280, 720],[0, 0, 1]])

d = np.array([0, 0, 0, 0, 0]) # just use first two terms

img = cv2.VideoCapture(sys.argv[1])
ret, frame = img.read()
w, h, ch = frame.shape
newcamera, roi = cv2.getOptimalNewCameraMatrix(K, d, (w, h), 0)

while True:
    ret, frame = img.read()
    # frame = cv2.resize(frame, (1920, 1080))
    newimg = cv2.undistort(frame, K, d, None, newcamera)
    cv2.imshow(sys.argv[1], newimg)
    cv2.waitKey(5)


# newfname = 'out.mp4'
# cv2.imwrite(newfname, newimg)