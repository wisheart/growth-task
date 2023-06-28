# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'video.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(670, 559)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_video = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_video.sizePolicy().hasHeightForWidth())
        self.label_video.setSizePolicy(sizePolicy)
        self.label_video.setObjectName("label_video")
        self.verticalLayout.addWidget(self.label_video)
        self.widget = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_select = QtWidgets.QPushButton(self.widget)
        self.pushButton_select.setObjectName("pushButton_select")
        self.horizontalLayout.addWidget(self.pushButton_select)
        self.pushButton_start = QtWidgets.QPushButton(self.widget)
        self.pushButton_start.setObjectName("pushButton_start")
        self.horizontalLayout.addWidget(self.pushButton_start)
        self.pushButton_stop = QtWidgets.QPushButton(self.widget)
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.horizontalLayout.addWidget(self.pushButton_stop)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_video.setText(_translate("Form", "video"))
        self.pushButton_select.setText(_translate("Form", "select"))
        self.pushButton_start.setText(_translate("Form", "start"))
        self.pushButton_stop.setText(_translate("Form", "stop"))
