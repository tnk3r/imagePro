import cv2, sys

if sys.argv[1] == "-w":
    src = cv2.VideoCapture(0)
else:
    src = cv2.VideoCapture(sys.argv[1])

fps = src.get(cv2.CAP_PROP_FPS)
width = src.get(cv2.CAP_PROP_FRAME_WIDTH)
height = src.get(cv2.CAP_PROP_FRAME_HEIGHT)
print "FrameSize: "+str(width)+" x "+str(height)
print "FrameRate: "+str(fps)
frNum = 0
res = ""

while True:

    ret, frame = src.read()

    ## Half the Size // double the proc speed
    height, width = frame.shape[:2]
    res = cv2.resize(frame,(width/2, height/2), interpolation = cv2.INTER_CUBIC)
    frNum += 1
    cv2.imshow('frame',res)
    print "Frame: "+str(frNum)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #

src.release()
cv2.destroyAllWindows()
