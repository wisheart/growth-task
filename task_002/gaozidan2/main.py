from  avideo import Ui_Form

import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
import cv2
import os
import qimage2ndarray


class VideoShow(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(VideoShow, self).__init__(parent)
        self.setupUi(self)
        self.timer_video = QtCore.QTimer()
        self.init()

    def init(self):
        self.pushButton_start.clicked.connect(self.btn_start_clicked)
        self.pushButton_stop.clicked.connect(self.btn_stop_clicked)
        self.pushButton_select.clicked.connect(self.btn_select_clicked)

    def btn_select_clicked(self):
        self.cwd = os.getcwd()
        self.videoName, _ = QFileDialog.getOpenFileName(self, '选择视频文件', self.cwd, "Video files(*.mp4 , *.avi)")
        self.cap = cv2.VideoCapture(self.videoName)
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.btn_start_clicked()


    def btn_start_clicked(self):
        self.timer_video.start(int(1000 / self.fps))
        self.timer_video.timeout.connect(self.show_video)


    def btn_stop_clicked(self):
        self.timer_video.stop()

    def show_video(self):
        ret, img = self.cap.read()
        self.img = cv2.resize(img, (1068, 623), interpolation=cv2.INTER_CUBIC)
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        qimg = qimage2ndarray.array2qimage(self.img)
        self.label_video.setPixmap(QPixmap(qimg))
        self.label_video.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '退出', "退出该界面？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = VideoShow()
    ui.show()
    sys.exit(app.exec_())