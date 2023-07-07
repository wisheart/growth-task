import sys
import demo
import os

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QFileDialog
from demo import Ui_MainWindow
from PyQt5 import QtCore
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.media_player = QMediaPlayer(self)
        self.timer_video = QtCore.QTimer()
        self.init()

    def init(self):
        self.ui.pushButton_2.clicked.connect(self.stop)
        self.ui.pushButton.clicked.connect(self.start)
        self.ui.pushButton_3.clicked.connect(self.selectFile)
    def selectFile(self):
        # print("select")
        self.cwd = os.getcwd()
        # file_dialog = QFileDialog()
        file_path, _ = QFileDialog.getOpenFileName(self, "选择视频文件", self.cwd, "视频文件 (*.mp4 *.avi)")
        if file_path:
            print("选择的文件路径：", file_path)
            self.start(file_path)

    def stop(self):
        self.media_player.pause()

    def start(self, file_path):
        media = QMediaContent(QUrl.fromLocalFile(file_path))
        self.media_player.setMedia(media)
        self.media_player.play()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainWindow = MyMainWindow()
    mainWindow.show()

    sys.exit(app.exec_())