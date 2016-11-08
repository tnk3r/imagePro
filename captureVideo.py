import cv2
import sys, os, time
#### WEBCAM ####
#
# if sys.argv[1] == 'webcam':
#     cap = cv2.VideoCapture(0)
# else:
#     cap = cv2.VideoCapture(sys.argv[1])

# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(sys.argv[1])
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter(sys.argv[2],fourcc, 24.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    # fet, frame2 = img.read()
    if ret == True:
        # frame2 = cv2.resize(frame2, (600, 480))
        # dst = cv2.addWeighted(frame,0.7,frame2,0.3,0)
        # frame = cv2.flip(frame, 0)
        # out.write(frame)

        cv2.imshow('frame',dst)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
