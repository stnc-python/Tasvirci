#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Tasvirci by OsmanDE
# github.com/OsmanDE/Tasvirci

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ResizeDialog(object):
    def setupUi(self, ResizeDialog):
        ResizeDialog.setObjectName("ResizeDialog")
        ResizeDialog.resize(353, 254)
        self.gridLayout_2 = QtWidgets.QGridLayout(ResizeDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(ResizeDialog)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(ResizeDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(ResizeDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 4, 0, 1, 2)
        self.frame = QtWidgets.QFrame(ResizeDialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.spinWidth = QtWidgets.QDoubleSpinBox(self.frame)
        self.spinWidth.setAlignment(QtCore.Qt.AlignCenter)
        self.spinWidth.setDecimals(1)
        self.spinWidth.setSingleStep(0.1)
        self.spinWidth.setObjectName("spinWidth")
        self.gridLayout.addWidget(self.spinWidth, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.spinDPI = QtWidgets.QSpinBox(self.frame)
        self.spinDPI.setAlignment(QtCore.Qt.AlignCenter)
        self.spinDPI.setMinimum(75)
        self.spinDPI.setMaximum(1000)
        self.spinDPI.setProperty("value", 300)
        self.spinDPI.setObjectName("spinDPI")
        self.gridLayout.addWidget(self.spinDPI, 0, 1, 1, 1)
        self.spinHeight = QtWidgets.QDoubleSpinBox(self.frame)
        self.spinHeight.setAlignment(QtCore.Qt.AlignCenter)
        self.spinHeight.setDecimals(1)
        self.spinHeight.setSingleStep(0.1)
        self.spinHeight.setObjectName("spinHeight")
        self.gridLayout.addWidget(self.spinHeight, 2, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 3, 0, 1, 2)
        self.checkBox = QtWidgets.QCheckBox(ResizeDialog)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 2, 0, 1, 2)
        self.widthEdit = QtWidgets.QLineEdit(ResizeDialog)
        self.widthEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.widthEdit.setObjectName("widthEdit")
        self.gridLayout_2.addWidget(self.widthEdit, 0, 1, 1, 1)
        self.heightEdit = QtWidgets.QLineEdit(ResizeDialog)
        self.heightEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.heightEdit.setObjectName("heightEdit")
        self.gridLayout_2.addWidget(self.heightEdit, 1, 1, 1, 1)

        self.retranslateUi(ResizeDialog)
        self.buttonBox.accepted.connect(ResizeDialog.accept)
        self.buttonBox.rejected.connect(ResizeDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ResizeDialog)

    def retranslateUi(self, ResizeDialog):
        _translate = QtCore.QCoreApplication.translate
        ResizeDialog.setWindowTitle(_translate("ResizeDialog", "Yeniden Boyutlandır - Tasvirci"))
        self.label.setText(_translate("ResizeDialog", "En :"))
        self.label_2.setText(_translate("ResizeDialog", "Boy :"))
        self.label_5.setText(_translate("ResizeDialog", "Boy :"))
        self.label_3.setText(_translate("ResizeDialog", "DPI :"))
        self.spinWidth.setSuffix(_translate("ResizeDialog", " cm"))
        self.label_4.setText(_translate("ResizeDialog", "En :"))
        self.spinHeight.setSuffix(_translate("ResizeDialog", " cm"))
        self.checkBox.setText(_translate("ResizeDialog", "Gelişmiş Düzenleme Moduna Geç"))
