# Status Bar

import sys 
from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
from PyQt5 import QtCore

class MyWindow(QMainWindow):
    def __init__(self): 
        super().__init__()
        self.setupUI() 
    
    # Window Widget
    def setupUI(self): 
        # Window Title
        self.setWindowTitle("pyqt-05")
        # Window 의 위치 및 크기 정하기
        self.setGeometry(700, 400, 400, 200)

        # Lable Text
        textLabel = QLabel(" 아이디 : ", self)
        textLabel.move(20, 20)
    
        # Line Edit ---------- 추가
        self.lineEdit = QLineEdit("", self)
        self.lineEdit.move(80, 20)
        self.lineEdit.resize(170, 30)
        # 이벤트 추가
        # self.lineEdit.textChanged.connect(self.lineEditChanged) # 글씨가 하나라도 쳐지면 lineEditChanged- 함수에 연결을 해라.
        self.lineEdit.returnPressed.connect(self.lineEditChanged) # lineEdit에서 Enter 를 눌렀을 때 lineEditChanged- 함수에 연결을 해라.


        # Status Bar --------- 추가 line edit 연결
        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

    def lineEditChanged(self):
        self.statusBar.showMessage(self.lineEdit.text()) # statusbar 로 lineEdit 의 메세지를 넘겨준다.

if __name__ == "__main__":
    app = QApplication(sys.argv) 
    mywindow = MyWindow()
    mywindow.show() 
    app.exec_() 