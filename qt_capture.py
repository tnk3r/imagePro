import cv2
from PyQt4 import QtGui, QtCore
import numpy as np


class Capture():
    def __init__(self):
        self.capturing = False
        self.warpvalue = False
        self.flipvalue = False
        self.c = cv2.VideoCapture(0)

    def startCapture(self):
        print "pressed start"
        self.capturing = True
        cap = self.c
        self.warp1value = 0
        self.warp2value = 0


        while(self.capturing):
            ret, frame = cap.read()
            w,h,ch = frame.shape

            if self.flipvalue == True:
                frame = cv2.flip(frame, 0)

            if self.warpvalue == True:
                K = np.array([[1280, 0, 720], [0, 1280, 720],[0, 0, 1]])
                d = np.array([self.warp1value, self.warp2value, 0, 0, 0])
                newcamera, roi = cv2.getOptimalNewCameraMatrix(K, d, (w, h), 0)
                frame = cv2.undistort(frame, K, d, None, newcamera)

                # pts1 = np.float32([[self.warp1value,self.warp2value],[0,0],[0,400],[600,400]])
                # pts2 = np.float32([[0,0],[400,0],[0,400],[600,400]])
                # M = cv2.getPerspectiveTransform(pts1,pts2)
                # frame = cv2.warpPerspective(frame,M,(1200,600))

            cv2.imshow("Capture", frame)
            cv2.waitKey(5)
        cv2.destroyAllWindows()

    def endCapture(self):
        print "pressed End"
        self.capturing = False

    def warp(self):
        if self.warpvalue == False:
            self.warpvalue = True
        else:
            self.warpvalue = False

    def flip(self):
        if self.flipvalue == False:
            self.flipvalue = True
        else:
            self.flipvalue = False

    def move_warp1(self, value):
        self.warp1value = value / 10

    def move_warp2(self, value):
        self.warp2value = value / 10

    def quitCapture(self):
        cap = self.c
        cv2.destroyAllWindows()
        cap.release()
        QtCore.QCoreApplication.quit()

class Window(QtGui.QWidget):
    def __init__(self):

        QtGui.QWidget.__init__(self)
        self.setWindowTitle('Control Panel')

        self.capture = Capture()
        self.start_button = QtGui.QPushButton('Start',self)
        self.start_button.clicked.connect(self.capture.startCapture)

        self.end_button = QtGui.QPushButton('End',self)
        self.end_button.clicked.connect(self.capture.endCapture)

        self.quit_button = QtGui.QPushButton('Quit',self)
        self.quit_button.clicked.connect(self.capture.quitCapture)

        self.warp_button = QtGui.QPushButton('Warp', self)
        self.warp_button.clicked.connect(self.capture.warp)

        self.flipbutton = QtGui.QPushButton('Flip', self)
        self.flipbutton.clicked.connect(self.capture.flip)

        self.warp1_slider = QtGui.QSlider(1, self)
        self.warp1_slider.sliderMoved.connect(self.calc_slider1)
        self.warp2_slider = QtGui.QSlider(1, self)
        self.warp2_slider.sliderMoved.connect(self.calc_slider2)

        vbox = QtGui.QVBoxLayout(self)
        vbox.addWidget(self.start_button)
        vbox.addWidget(self.end_button)
        vbox.addWidget(self.quit_button)
        vbox.addWidget(self.warp_button)
        vbox.addWidget(self.flipbutton)
        vbox.addWidget(self.warp1_slider)
        vbox.addWidget(self.warp2_slider)

        self.setLayout(vbox)
        self.setGeometry(100,100,200,200)
        self.show()

    def calc_slider1(self, event):
        self.capture.move_warp1(self.warp1_slider.value())

    def calc_slider2(self, event):
        self.capture.move_warp2(self.warp2_slider.value())


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
