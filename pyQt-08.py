# SpinBox

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
        self.setWindowTitle("pyqt-08")
        # Window 의 위치 및 크기 정하기
        self.setGeometry(700, 400, 300, 300)
        self.setWindowIcon(QIcon('icon.ico'))

        # Label Text
        textLabel = QLabel("주문 수량 : ", self)
        textLabel.move(10,20)

        # SpinBox---------------추가
        self.spinbox = QSpinBox(self)
        self.spinbox.move(80,25)
        self.spinbox.resize(80,22)
        # 시작숫자, 증가숫자, 최소값, 최대값 정의 -------------추가
        self.spinbox.setValue(10) # 초기값 10부터 시작하겠다.
        self.spinbox.setSingleStep(5) # 증가숫자 5씩 증가시키겠다.
        self.spinbox.setMinimum(5) # 최소값
        self.spinbox.setMaximum(10000) # 최고값
        self.spinbox.valueChanged.connect(self.spinboxChanged) # 이 문장을 맨 마지막에 써줘야한다. - 파이썬은 한줄씩 컴파일

        # Status Bar 
        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

    def spinboxChanged(self):
        val = self.spinbox.value() # SpinBox 값 가져오기
        msg = "%d 개를 주문 하였습니다.! "%val
        self.statusBar.showMessage(msg)

if __name__ == "__main__":
    app = QApplication(sys.argv) 
    mywindow = MyWindow()
    mywindow.show() 
    app.exec_() 