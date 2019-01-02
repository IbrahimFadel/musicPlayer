# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'musicPlayer.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import Tk
from tkinter import filedialog
import os

Tk().withdraw()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 10, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Chalkboard")
        font.setPointSize(31)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setObjectName("label")
        self.importBtn = QtWidgets.QPushButton(self.centralwidget)
        self.importBtn.setGeometry(QtCore.QRect(50, 220, 113, 32))
        self.importBtn.setObjectName("importBtn")
        self.playBtn = QtWidgets.QPushButton(self.centralwidget)
        self.playBtn.setGeometry(QtCore.QRect(330, 260, 113, 32))
        self.playBtn.setObjectName("playBtn")
        self.skipBtn = QtWidgets.QPushButton(self.centralwidget)
        self.skipBtn.setGeometry(QtCore.QRect(330, 300, 113, 32))
        self.skipBtn.setObjectName("skipBtn")
        self.currentSongLbl = QtWidgets.QLabel(self.centralwidget)
        self.currentSongLbl.setGeometry(QtCore.QRect(320, 125, 281, 41))
        self.currentSongLbl.setObjectName("currentSongLbl")
        self.songProgress = QtWidgets.QProgressBar(self.centralwidget)
        self.songProgress.setGeometry(QtCore.QRect(300, 160, 118, 23))
        self.songProgress.setProperty("value", 0)
        self.songProgress.setObjectName("songProgress")
        self.volumeSlider = QtWidgets.QSlider(self.centralwidget)
        self.volumeSlider.setGeometry(QtCore.QRect(520, 280, 22, 160))
        self.volumeSlider.setOrientation(QtCore.Qt.Vertical)
        self.volumeSlider.setObjectName("volumeSlider")
        self.volumeLbl = QtWidgets.QLabel(self.centralwidget)
        self.volumeLbl.setGeometry(QtCore.QRect(510, 250, 60, 16))
        self.volumeLbl.setObjectName("volumeLbl")
        self.shuffleRdo = QtWidgets.QRadioButton(self.centralwidget)
        self.shuffleRdo.setGeometry(QtCore.QRect(340, 350, 100, 20))
        self.shuffleRdo.setObjectName("shuffleRdo")
        self.repeatRdo = QtWidgets.QRadioButton(self.centralwidget)
        self.repeatRdo.setGeometry(QtCore.QRect(340, 380, 100, 20))
        self.repeatRdo.setObjectName("repeatRdo")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(50, 250, 256, 192))
        self.listWidget.setObjectName("songsLst")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.importBtn.clicked.connect(self.importPlaylist)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Itunes 2.0"))
        self.importBtn.setText(_translate("MainWindow", "Import Playlist"))
        self.playBtn.setText(_translate("MainWindow", "Play"))
        self.skipBtn.setText(_translate("MainWindow", "Skip"))
        self.currentSongLbl.setText(_translate("MainWindow", "Current Song"))
        self.volumeLbl.setText(_translate("MainWindow", "Volume"))
        self.shuffleRdo.setText(_translate("MainWindow", "Shuffle"))
        self.repeatRdo.setText(_translate("MainWindow", "Repeat Song"))

    def importPlaylist(self):
        directory = filedialog.askdirectory()
        songs = []
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            if filename.endswith(".mp3") or filename.endswith(".wav"): 
                songs.append(filename)
                self.songsLst.addItem(file)
                print(filename)
                continue
            else:
                continue


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
