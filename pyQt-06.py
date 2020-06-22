# Radio Button

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
        self.setWindowTitle("pyqt-06")
        # Window 의 위치 및 크기 정하기
        self.setGeometry(700, 400, 400, 200)
        self.setWindowIcon(QIcon('icon.ico'))

        # Group Box ---------------- 추가
        groupBox = QGroupBox("과일선택", self) 
        groupBox.move(10, 10)
        groupBox.resize(280, 80)

        # Radio Button  ----------------- 추가
        self.radio1 = QRadioButton("사과", self)
        self.radio1.move(20, 20)
        self.radio1.setChecked(True) # 하나는 기본값의로 체크 되어있도록
        self.radio1.clicked.connect(self.radioButtonCliked)
        # Radio Button 
        self.radio2 = QRadioButton("바나나", self)
        self.radio2.move(20, 40)
        self.radio2.clicked.connect(self.radioButtonCliked)
        # Radio Button 
        self.radio3 = QRadioButton("포도", self)
        self.radio3.move(20, 60)
        self.radio3.clicked.connect(self.radioButtonCliked)

        # Status Bar 
        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

    def radioButtonCliked(self):
        msg = ""
        if self.radio1.isChecked():
            msg = "사과"
        elif self.radio2.isChecked():
            msg = "바나나"
        else :
            msg = "포도"
        
        self.statusBar.showMessage(msg + "가 선택됨.")

if __name__ == "__main__":
    app = QApplication(sys.argv) 
    mywindow = MyWindow()
    mywindow.show() 
    app.exec_() 