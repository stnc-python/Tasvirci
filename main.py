#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Tasvirci by OsmanDE
# github.com/OsmanDE/Tasvirci

import sys, os
sys.path.append(os.path.dirname(__file__)) 

from PyQt5.QtCore import (pyqtSignal, QPoint, Qt, QSettings, QFileInfo, QTimer, QRect, QSize, QEventLoop, QSettings )
from PyQt5.QtGui import QIcon, QPainter, QPen, QColor, QPixmap, QImageReader, QMovie, QTransform, QIntValidator
from PyQt5.QtWidgets import ( QApplication, QMainWindow, QLabel, QHBoxLayout, QSizePolicy, 
        QDialog, QFileDialog, QInputDialog, QCheckBox, QDoubleSpinBox, QPushButton )

from mainwindow import Ui_MainWindow
from resize_dialog import Ui_ResizeDialog
from photogrid import GridDialog


class Image(QLabel):
    imageUpdated = pyqtSignal()
    def __init__(self, *args):
        QLabel.__init__(self, *args)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setMouseTracking(True)
        self.mouse_pressed = False
        self.animation = False
        self.crop_mode = False
        self.scale = 1.0

    def setAnimation(self, anim):
        self.scale = 1.0
        self.pic = QPixmap()
        self.setMovie(anim)
        anim.start()
        self.animation = True

    def setImage(self, pixmap):
        self.pic = pixmap                
        self.showScaled()
        self.animation = False

    def showScaled(self):
        if self.scale == 1.0:
            pm = self.pic.copy()
        else:
            pm = self.pic.scaledToHeight(self.scale*self.pic.height(), Qt.SmoothTransformation)
        self.setPixmap(pm)
        self.imageUpdated.emit()

    def rotate(self, degree):
        transform = QTransform()
        transform.rotate(degree)
        self.pic = self.pic.transformed(transform)
        self.showScaled()

    def zoomBy(self, factor):
        self.scale *= factor
        self.showScaled()

    def enableCropMode(self, enable):
        if enable:
            self.crop_mode = True
            self.scaleW = self.pixmap().width()/self.pic.width()
            self.scaleH = self.pixmap().height()/self.pic.height()
            self.pm_tmp = self.pixmap().copy()
            self.topleft = QPoint(0,0)
            self.btmright = QPoint(self.pixmap().width()-1, self.pixmap().height()-1)
            self.last_pt = QPoint(self.btmright)
            self.p1, self.p2 = QPoint(self.topleft), QPoint(self.btmright)
            self.crop_width, self.crop_height = 3.5, 4.5
            self.lock_crop_ratio = False
            self.imgAspect = self.pic.width()/self.pic.height()
            self.drawCropBox()
        else:
            self.crop_mode = False
            del self.pm_tmp
            self.showScaled()

    def mousePressEvent(self, ev):
        if not self.crop_mode : return
        self.mouse_pressed = True
        self.clk_pos = ev.pos()
        self.p1, self.p2 = QPoint(self.topleft), QPoint(self.btmright) 
        if QRect(self.topleft, QSize(60, 60)).contains(self.clk_pos): 
            self.clk_area = 1
        elif QRect(self.btmright, QSize(-60, -60)).contains(self.clk_pos): 
            self.clk_area = 2
        elif QRect(self.topleft, self.btmright).contains(self.clk_pos): 
            self.clk_area = 3
        else:
            self.clk_area = 0

    def mouseReleaseEvent(self, ev):
        if not self.crop_mode: return
        self.mouse_pressed = False
        self.topleft, self.btmright = self.p1, self.p2

    def mouseMoveEvent(self, ev):
        if not (self.mouse_pressed and self.crop_mode) : return
        moved = ev.pos() - self.clk_pos
        boxAspect = self.crop_width/self.crop_height

        if self.clk_area == 1: 
            new_p1 = self.topleft + moved
            self.p1 = QPoint(max(0, new_p1.x()), max(0, new_p1.y()))
            if self.lock_crop_ratio:
                if self.imgAspect>boxAspect: self.p1.setX(round(self.p2.x() - (self.p2.y()-self.p1.y()+1)*boxAspect -1))
                if self.imgAspect<boxAspect: self.p1.setY(round(self.p2.y() - (self.p2.x()-self.p1.x()+1)/boxAspect -1))

        elif self.clk_area == 2: 
            new_p2 = self.btmright + moved
            self.p2 = QPoint(min(self.last_pt.x(), new_p2.x()), min(self.last_pt.y(), new_p2.y()))
            if self.lock_crop_ratio:
                if self.imgAspect>boxAspect: self.p2.setX(round(self.p1.x() + (self.p2.y()-self.p1.y()+1)*boxAspect -1))
                if self.imgAspect<boxAspect: self.p2.setY(round(self.p1.y() + (self.p2.x()-self.p1.x()+1)/boxAspect -1))
            
        elif self.clk_area == 3:
            min_dx, max_dx = -self.topleft.x(), self.last_pt.x()-self.btmright.x()
            min_dy, max_dy = -self.topleft.y(), self.last_pt.y()-self.btmright.y()
            dx = max(moved.x(), min_dx) if (moved.x() < 0) else min(moved.x(), max_dx)
            dy = max(moved.y(), min_dy) if (moved.y() < 0) else min(moved.y(), max_dy)
            self.p1 = self.topleft + QPoint(dx, dy)
            self.p2 = self.btmright + QPoint(dx, dy)

        self.drawCropBox()

    def drawCropBox(self):
        pm = self.pm_tmp.copy()
        pm_box = pm.copy(self.p1.x(), self.p1.y(), self.p2.x()-self.p1.x(), self.p2.y()-self.p1.y())
        painter = QPainter(pm)
        painter.fillRect(0,0, pm.width(), pm.height(), QColor(127,127,127,127))
        painter.drawPixmap(self.p1.x(), self.p1.y(), pm_box)
        painter.drawRect(self.p1.x(), self.p1.y(), self.p2.x()-self.p1.x(), self.p2.y()-self.p1.y())
        painter.drawRect(self.p1.x(), self.p1.y(), 59, 59)
        painter.drawRect(self.p2.x(), self.p2.y(), -59, -59)
        painter.setPen(Qt.white)
        painter.drawRect(self.p1.x()+1, self.p1.y()+1, 57, 57)
        painter.drawRect(self.p2.x()-1, self.p2.y()-1, -57, -57)
        painter.end()
        self.setPixmap(pm)
        self.imageUpdated.emit()

    def lockCropRatio(self, checked):
        self.lock_crop_ratio = bool(checked)

    def setCropWidth(self, value):
        self.crop_width = value

    def setCropHeight(self, value):
        self.crop_height = value

    def cropImage(self):
        w, h = round((self.btmright.x()-self.topleft.x()+1)/self.scaleW), round((self.btmright.y()-self.topleft.y()+1)/self.scaleH)
        pm = self.pic.copy(round(self.topleft.x()/self.scaleW), round(self.topleft.y()/self.scaleH), w, h)
        self.setImage(pm)


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.setupUi(self, self)
        layout = QHBoxLayout(self.scrollAreaWidgetContents)
        layout.setContentsMargins(0, 0, 0, 0)
        self.image = Image(self)
        layout.addWidget(self.image)
        self.slideShowBtn.setCheckable(True)
        self.connectSignals()
        self.settings = QSettings(self)
        desktop = QApplication.desktop()
        self.screen_width = desktop.availableGeometry().width()
        self.screen_height = desktop.availableGeometry().height()
        self.timer = False
        self.filepath = ''
        self.offset_x = int(self.settings.value("OffsetX", 4))
        self.offset_y = int(self.settings.value("OffsetY", 26))
        self.btnboxwidth = int(self.settings.value("BtnBoxWidth", 60))
        self.crop_widgets = []

    def connectSignals(self):
        self.openBtn.clicked.connect(self.openFile)
        self.saveBtn.clicked.connect(self.saveFile)
        self.resizeBtn.clicked.connect(self.resizeImage)
        self.cropBtn.clicked.connect(self.cropImage)
        self.addBorderBtn.clicked.connect(self.addBorder)
        self.photoGridBtn.clicked.connect(self.createPhotoGrid)
        self.quitBtn.clicked.connect(self.close)
        self.prevBtn.clicked.connect(self.openPrevImage)
        self.nextBtn.clicked.connect(self.openNextImage)
        self.zoomInBtn.clicked.connect(self.zoomInImage)
        self.zoomOutBtn.clicked.connect(self.zoomOutImage)
        self.origSizeBtn.clicked.connect(self.origSizeImage)
        self.rotateLeftBtn.clicked.connect(self.rotateLeft)
        self.rotateRightBtn.clicked.connect(self.rotateRight)
        self.slideShowBtn.clicked.connect(self.playSlideShow)
        self.image.imageUpdated.connect(self.updateStatus)
        self.openBtn.setShortcut('Ctrl+O')
        self.saveBtn.setShortcut('Ctrl+S')
        self.resizeBtn.setShortcut('Ctrl+R')
        self.cropBtn.setShortcut('Ctrl+X')
        self.addBorderBtn.setShortcut('Ctrl+B')
        self.photoGridBtn.setShortcut('Ctrl+G')
        self.quitBtn.setShortcut('Esc')
        self.prevBtn.setShortcut('Left')
        self.nextBtn.setShortcut('Right')
        self.zoomInBtn.setShortcut('+')
        self.zoomOutBtn.setShortcut('-')
        self.origSizeBtn.setShortcut('1')
        self.rotateLeftBtn.setShortcut('Ctrl+Left')
        self.rotateRightBtn.setShortcut('Ctrl+Right')
        self.slideShowBtn.setShortcut('Space')

    def openFile(self, filepath=False):
        if not filepath :
            filefilter = "Image files (*.jpg *.png *.jpeg *.svg *.gif *.tiff *.ppm *.bmp);;JPEG Images (*.jpg *.jpeg);;PNG Images (*.png);;SVG Images (*.svg);;All Files (*)"
            filepath, sel_filter = QFileDialog.getOpenFileName(self, 'Seyahatname - Resmi Aç', self.filepath, filefilter)            
            if filepath == '' : return
        image_reader = QImageReader(filepath)
        if image_reader.format() == 'gif': 
            anim = QMovie(filepath)
            self.image.setAnimation(anim)
            self.adjustWindowSize(True)
            self.statusbar.showMessage("Çözünürlük : %ix%i" % (self.image.width(), self.image.height()))
            self.disableButtons(True)
        else:                         
          image_reader.setAutoTransform(True)
          pm = QPixmap.fromImageReader(image_reader)
          if not pm.isNull() :
            self.image.scale = self.getOptimumScale(pm)
            self.image.setImage(pm)
            self.adjustWindowSize()
            self.disableButtons(False)
          else:
            return
        self.filepath = filepath
        self.setWindowTitle('Tasvirci - '+QFileInfo(filepath).fileName())

    def saveFile(self):
        quality = -1
        filefilter = "Image files (*.jpg *.png *.jpeg *.ppm *.bmp *.tiff);;JPEG Image (*.jpg);;PNG Image (*.png);;Tagged Image (*.tiff);;Portable Pixmap (*.ppm);;X11 Pixmap (*.xpm);;Windows Bitmap (*.bmp)"
        filepath, sel_filter = QFileDialog.getSaveFileName(self, 'Seyahatname - Resmi Kaydet', self.filepath, filefilter)
        if filepath != '':
            if self.image.animation:
                pm = self.image.movie().currentPixmap()
            else:
                pm = self.image.pic
            if not pm.isNull():
                pm.save(filepath, None, quality)

    def resizeImage(self):
        dialog = ResizeDialog(self, self.image.pic.width(), self.image.pic.height())
        if dialog.exec_() == 1 :
            img_width, img_height = dialog.widthEdit.text(), dialog.heightEdit.text()
            if img_width!='' and img_height!='' :
                pm = self.image.pic.scaled(int(img_width), int(img_height), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
            elif img_width!='' :
                pm = self.image.pic.scaledToWidth(int(img_width), Qt.SmoothTransformation)
            elif img_height!='' :
                pm = self.image.pic.scaledToHeight(int(img_height), Qt.SmoothTransformation)
            else :
                return
            self.image.setImage(pm)


    def cropImage(self):
        if not self.image.crop_mode:
            self.image.enableCropMode(True)
            lockratio = QCheckBox("Oranı Koru  ", self.statusbar)
            self.statusbar.addPermanentWidget(lockratio)
            labelWH = QLabel("<b>E:B (En:Boy) =</b>", self.statusbar)
            self.statusbar.addPermanentWidget(labelWH)
            labelWH.setEnabled(False)
            spinWidth = QDoubleSpinBox(self.statusbar)
            spinWidth.setRange(0.1, 9.9)
            spinWidth.setSingleStep(0.1)
            spinWidth.setDecimals(1)
            spinWidth.setMaximumWidth(40)
            spinWidth.setValue(3.5)
            spinWidth.setEnabled(False)
            self.statusbar.addPermanentWidget(spinWidth)
            colon = QLabel(":", self.statusbar)
            self.statusbar.addPermanentWidget(colon)
            spinHeight = QDoubleSpinBox(self.statusbar)
            spinHeight.setRange(0.1, 9.9)
            spinHeight.setSingleStep(0.1)
            spinHeight.setDecimals(1)
            spinHeight.setMaximumWidth(40)
            spinHeight.setValue(4.5)
            spinHeight.setEnabled(False)
            self.statusbar.addPermanentWidget(spinHeight)
            cropnowBtn = QPushButton("Kırp", self.statusbar)
            self.statusbar.addPermanentWidget(cropnowBtn)
            cropcancelBtn = QPushButton("İptal", self.statusbar)
            self.statusbar.addPermanentWidget(cropcancelBtn)
            lockratio.toggled.connect(labelWH.setEnabled)
            lockratio.toggled.connect(spinWidth.setEnabled)
            lockratio.toggled.connect(spinHeight.setEnabled)
            lockratio.toggled.connect(self.image.lockCropRatio)
            spinWidth.valueChanged.connect(self.image.setCropWidth)
            spinHeight.valueChanged.connect(self.image.setCropHeight)
            cropnowBtn.clicked.connect(self.image.cropImage)
            cropnowBtn.clicked.connect(self.cancelCropping)
            cropcancelBtn.clicked.connect(self.cancelCropping)
            self.crop_widgets += [lockratio, labelWH, spinWidth, colon, spinHeight, cropnowBtn, cropcancelBtn]

    def cancelCropping(self):
        self.image.enableCropMode(False)
        while len(self.crop_widgets)> 0:
            widget = self.crop_widgets.pop()
            self.statusbar.removeWidget(widget)
            widget.deleteLater()

    def addBorder(self):
        width, ok = QInputDialog.getInt(self, 'Tasvirci - Çerçeve Ekle', 'Çerçeve Kalınlığı :', 2, 1)
        if ok:
            painter = QPainter(self.image.pic)
            pen = QPen(Qt.black)
            pen.setWidth(width)
            pen.setJoinStyle(Qt.MiterJoin);
            painter.setPen(pen)
            painter.drawRect(width/2, width/2, self.image.pic.width()-width, self.image.pic.height()-width)
            self.image.showScaled()

    def createPhotoGrid(self):
        dialog = GridDialog(self.image.pic, self)
        if dialog.exec_() == 1:
            self.image.scale = self.getOptimumScale(dialog.gridPaper.photo_grid)
            self.image.setImage(dialog.gridPaper.photo_grid)
            self.adjustWindowSize()

    def openPrevImage(self):
        fi = QFileInfo(self.filepath)
        if not fi.exists() : return
        filename = fi.fileName()
        basedir = fi.absolutePath()         
        file_filter = ["*.jpg", "*.jpeg", "*.png", "*.gif", "*.svg", "*.bmp", "*.tiff"]
        image_list = fi.dir().entryList(file_filter)

        index = image_list.index(filename)
        prevfile = image_list[index-1]
        self.openFile(basedir + '/' + prevfile)

    def openNextImage(self):
        fi = QFileInfo(self.filepath)
        if not fi.exists() : return
        filename = fi.fileName()
        basedir = fi.absolutePath()         
        file_filter = ["*.jpg", "*.jpeg", "*.png", "*.gif", "*.svg", "*.bmp", "*.tiff"]
        image_list = fi.dir().entryList(file_filter)
        index = image_list.index(filename)
        if index == len(image_list)-1 : index = -1
        nextfile = image_list[index+1]
        self.openFile(basedir + '/' + nextfile)

    def zoomInImage(self):
        self.image.zoomBy(6.0/5)

    def zoomOutImage(self):
        self.image.zoomBy(5.0/6)

    def origSizeImage(self):
        self.image.scale = 1.0
        self.image.showScaled()

    def rotateLeft(self):
        self.image.rotate(270)

    def rotateRight(self):
        self.image.rotate(90)

    def playSlideShow(self, checked):
        if checked : 
            if not self.timer:
                self.timer = QTimer(self)
                self.timer.timeout.connect(self.openNextImage)
            self.timer.start(3000)
            self.slideShowBtn.setIcon(QIcon(':/pause.png'))
        else:       
            self.timer.stop()
            self.slideShowBtn.setIcon(QIcon(':/play.png'))

    def getOptimumScale(self, pixmap):
        img_width = pixmap.width()
        img_height = pixmap.height()
        max_width = self.screen_width - (2*self.btnboxwidth + 2*self.offset_x)
        max_height = self.screen_height - (self.offset_y + self.offset_x + 4+32)
        if img_width > max_width or img_height > max_height :
            if (max_width/max_height > img_width/img_height) :
                scale = max_height/img_height
            else :
                scale = max_width/img_width
        else:
            scale = 1.0
        return scale

    def adjustWindowSize(self, animation=False):
        if self.isMaximized() : return
        if animation:
            wait(30)       
            self.resize(self.image.width() + 2*self.btnboxwidth + 4, 
                    self.image.height() + 4+32)
        else:
            self.resize(self.image.pixmap().width() + 2*self.btnboxwidth + 4, 
                    self.image.pixmap().height() + 4+32)
        self.move((self.screen_width - (self.width() + 2*self.offset_x) )/2+self.offset_x, 
                  (self.screen_height - (self.height() + self.offset_x + self.offset_y))/2+self.offset_y )

    def updateStatus(self):
        if self.image.crop_mode:
            width = round((self.image.p2.x() - self.image.p1.x() + 1)/self.image.scaleW)
            height = round((self.image.p2.y() - self.image.p1.y() + 1)/self.image.scaleH)
        else:
            width = self.image.pic.width()
            height = self.image.pic.height()
        text = "Çözünürlük : %ix%i , Oran : %3.2fx" % (width, height, self.image.scale)
        self.statusbar.showMessage(text)

    def disableButtons(self, disable):
        self.resizeBtn.setDisabled(disable)
        self.cropBtn.setDisabled(disable)
        self.addBorderBtn.setDisabled(disable)
        self.photoGridBtn.setDisabled(disable)
        self.zoomInBtn.setDisabled(disable)
        self.zoomOutBtn.setDisabled(disable)
        self.origSizeBtn.setDisabled(disable)
        self.rotateLeftBtn.setDisabled(disable)
        self.rotateRightBtn.setDisabled(disable)

    def closeEvent(self, ev):
        self.settings.setValue('OffsetX', self.geometry().x()-self.x())
        self.settings.setValue('OffsetY', self.geometry().y()-self.y())
        self.settings.setValue('BtnBoxWidth', self.frame.width())
        QMainWindow.closeEvent(self, ev)

class ResizeDialog(QDialog, Ui_ResizeDialog):
    def __init__(self, parent, img_width, img_height):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.frame.hide()
        self.resize(353, 200)
        validator = QIntValidator(self)
        self.widthEdit.setValidator(validator)
        self.heightEdit.setValidator(validator)
        self.spinWidth.setValue(img_width*2.54/300)
        self.spinHeight.setValue(img_height*2.54/300)
        self.checkBox.toggled.connect(self.toggleAdvanced)
        self.spinWidth.valueChanged.connect(self.onValueChange)
        self.spinHeight.valueChanged.connect(self.onValueChange)
        self.spinDPI.valueChanged.connect(self.onValueChange)
        self.widthEdit.setFocus()

    def toggleAdvanced(self, checked):
        if checked:
            self.frame.show()
        else:
            self.frame.hide()

    def onValueChange(self, value):
        DPI = self.spinDPI.value()
        self.widthEdit.setText( str(round(DPI * self.spinWidth.value()/2.54)))
        self.heightEdit.setText( str(round(DPI * self.spinHeight.value()/2.54)))
        
def wait(millisec):
    loop = QEventLoop()
    QTimer.singleShot(millisec, loop.quit)
    loop.exec_()

def main():
    app = QApplication(sys.argv)
    app.setOrganizationName("Tasvirci")
    app.setApplicationName("Tasvirci")
    win = Window()
    win.show()
    if len(sys.argv)>1 :
        path = os.path.abspath(sys.argv[-1])
        if os.path.exists(path):
            win.openFile(path)
    else:
        pm = QPixmap('tasvirAraclari/osman.png')
        win.image.setImage(pm)
        win.adjustWindowSize()

    sys.exit(app.exec_())

if __name__== '__main__':
    main()
