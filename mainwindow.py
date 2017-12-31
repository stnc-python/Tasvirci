#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Tasvirci by OsmanDE
# github.com/OsmanDE/Tasvirci

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(613, 409)
        MainWindow.setMinimumSize(QtCore.QSize(613, 409))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.openBtn = QtWidgets.QPushButton(self.frame)
        self.openBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.openBtn.setIcon(icon)
        self.openBtn.setIconSize(QtCore.QSize(32, 32))
        self.openBtn.setObjectName("openBtn")
        self.verticalLayout.addWidget(self.openBtn)
        self.saveBtn = QtWidgets.QPushButton(self.frame)
        self.saveBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveBtn.setIcon(icon1)
        self.saveBtn.setIconSize(QtCore.QSize(32, 32))
        self.saveBtn.setObjectName("saveBtn")
        self.verticalLayout.addWidget(self.saveBtn)
        self.resizeBtn = QtWidgets.QPushButton(self.frame)
        self.resizeBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/resize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.resizeBtn.setIcon(icon2)
        self.resizeBtn.setIconSize(QtCore.QSize(32, 32))
        self.resizeBtn.setObjectName("resizeBtn")
        self.verticalLayout.addWidget(self.resizeBtn)
        self.cropBtn = QtWidgets.QPushButton(self.frame)
        self.cropBtn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/crop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cropBtn.setIcon(icon3)
        self.cropBtn.setIconSize(QtCore.QSize(32, 32))
        self.cropBtn.setObjectName("cropBtn")
        self.verticalLayout.addWidget(self.cropBtn)
        self.addBorderBtn = QtWidgets.QPushButton(self.frame)
        self.addBorderBtn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/addborder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addBorderBtn.setIcon(icon4)
        self.addBorderBtn.setIconSize(QtCore.QSize(32, 32))
        self.addBorderBtn.setObjectName("addBorderBtn")
        self.verticalLayout.addWidget(self.addBorderBtn)
        self.photoGridBtn = QtWidgets.QPushButton(self.frame)
        self.photoGridBtn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/creategrid.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.photoGridBtn.setIcon(icon5)
        self.photoGridBtn.setIconSize(QtCore.QSize(32, 32))
        self.photoGridBtn.setObjectName("photoGridBtn")
        self.verticalLayout.addWidget(self.photoGridBtn)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.quitBtn = QtWidgets.QPushButton(self.frame)
        self.quitBtn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.quitBtn.setIcon(icon6)
        self.quitBtn.setIconSize(QtCore.QSize(32, 32))
        self.quitBtn.setObjectName("quitBtn")
        self.verticalLayout.addWidget(self.quitBtn)
        self.horizontalLayout.addWidget(self.frame)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 509, 384))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.prevBtn = QtWidgets.QPushButton(self.frame_2)
        self.prevBtn.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/prev.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.prevBtn.setIcon(icon7)
        self.prevBtn.setIconSize(QtCore.QSize(32, 32))
        self.prevBtn.setObjectName("prevBtn")
        self.verticalLayout_2.addWidget(self.prevBtn)
        self.nextBtn = QtWidgets.QPushButton(self.frame_2)
        self.nextBtn.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextBtn.setIcon(icon8)
        self.nextBtn.setIconSize(QtCore.QSize(32, 32))
        self.nextBtn.setObjectName("nextBtn")
        self.verticalLayout_2.addWidget(self.nextBtn)
        self.zoomInBtn = QtWidgets.QPushButton(self.frame_2)
        self.zoomInBtn.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/zoomin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoomInBtn.setIcon(icon9)
        self.zoomInBtn.setIconSize(QtCore.QSize(32, 32))
        self.zoomInBtn.setObjectName("zoomInBtn")
        self.verticalLayout_2.addWidget(self.zoomInBtn)
        self.zoomOutBtn = QtWidgets.QPushButton(self.frame_2)
        self.zoomOutBtn.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/zoomout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoomOutBtn.setIcon(icon10)
        self.zoomOutBtn.setIconSize(QtCore.QSize(32, 32))
        self.zoomOutBtn.setObjectName("zoomOutBtn")
        self.verticalLayout_2.addWidget(self.zoomOutBtn)
        self.origSizeBtn = QtWidgets.QPushButton(self.frame_2)
        self.origSizeBtn.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/originalsize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.origSizeBtn.setIcon(icon11)
        self.origSizeBtn.setIconSize(QtCore.QSize(32, 32))
        self.origSizeBtn.setObjectName("origSizeBtn")
        self.verticalLayout_2.addWidget(self.origSizeBtn)
        self.rotateLeftBtn = QtWidgets.QPushButton(self.frame_2)
        self.rotateLeftBtn.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/rotateleft.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rotateLeftBtn.setIcon(icon12)
        self.rotateLeftBtn.setIconSize(QtCore.QSize(32, 32))
        self.rotateLeftBtn.setObjectName("rotateLeftBtn")
        self.verticalLayout_2.addWidget(self.rotateLeftBtn)
        self.rotateRightBtn = QtWidgets.QPushButton(self.frame_2)
        self.rotateRightBtn.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/rotateright.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rotateRightBtn.setIcon(icon13)
        self.rotateRightBtn.setIconSize(QtCore.QSize(32, 32))
        self.rotateRightBtn.setObjectName("rotateRightBtn")
        self.verticalLayout_2.addWidget(self.rotateRightBtn)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.slideShowBtn = QtWidgets.QPushButton(self.frame_2)
        self.slideShowBtn.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.slideShowBtn.setIcon(icon14)
        self.slideShowBtn.setIconSize(QtCore.QSize(32, 32))
        self.slideShowBtn.setCheckable(True)
        self.slideShowBtn.setObjectName("slideShowBtn")
        self.verticalLayout_2.addWidget(self.slideShowBtn)
        self.horizontalLayout.addWidget(self.frame_2)
        self.horizontalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tasvirci"))

import resources_rc
