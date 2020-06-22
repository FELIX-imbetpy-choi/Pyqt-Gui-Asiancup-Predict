# Check Box

import sys 
from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtGui import * 

class MyWindow(QMainWindow):
    def __init__(self): 
        super().__init__()
        self.setupUI() 
    
    # Window Widget
    def setupUI(self): 
        # Window Title
        self.setWindowTitle("pyqt-07")
        # Window 의 위치 및 크기 정하기
        self.setGeometry(700, 400, 400, 200)
        self.setWindowIcon(QIcon('icon.ico'))

        # Label Text
        textLabel = QLabel("취미 생활 선택", self)
        textLabel.move(10,20)

        # Check Box ----------------추가
        self.checkBox1 = QCheckBox("독서", self)
        self.checkBox1.move(10, 50)
        self.checkBox1.resize(150,30)
        self.checkBox1.stateChanged.connect(self.checkBoxState)
        
        self.checkBox2 = QCheckBox("테니스", self)
        self.checkBox2.move(10, 80)
        self.checkBox2.resize(150,30)
        self.checkBox2.stateChanged.connect(self.checkBoxState)

        self.checkBox3 = QCheckBox("음악편곡", self)
        self.checkBox3.move(10, 110)
        self.checkBox3.resize(150,30)
        self.checkBox3.stateChanged.connect(self.checkBoxState)

        # Status Bar 
        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

    def checkBoxState(self):
        msg = ""
        count = 0
        if self.checkBox1.isChecked():
            msg += "독서 "
            count += 1
        if self.checkBox2.isChecked():
            msg += "테니스 "
            count += 1
        if self.checkBox3.isChecked():
            msg += "음악편곡 "
            count += 1
        
        self.statusBar.showMessage(msg + "%d 가지 선택됨."%count)

if __name__ == "__main__":
    app = QApplication(sys.argv) 
    mywindow = MyWindow()
    mywindow.show() 
    app.exec_() 