# 두개의 클래스 사용

import sys # main이란 함수와 class를 인식하게 하기 위해
from PyQt5.QtWidgets import * # 위젯관련
from PyQt5.QtCore import * # 윈도우 전반적인 관련
from PyQt5.QtGui import *


# 클래스 NEW
class LogInDialog(QDialog):
    def __init__(self): 
        super().__init__()
        self.setupUI()
        self.id = None # id값 설정
        self.password = None

    def setupUI(self):
        self.setGeometry(1100, 200, 300, 100)
        self.setWindowTitle("로그인")
        self.setWindowIcon(QIcon('icon.ico'))

        label1 = QLabel('ID : ')
        label2 = QLabel('Password : ')

        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()

        self.pushButton1 = QPushButton("로그인")
        self.pushButton1.clicked.connect(self.pushButtonClicked)

        # layout
        layout = QGridLayout()

        layout.addWidget(label1, 0,0)
        layout.addWidget(self.lineEdit1, 0,1)
        layout.addWidget(self.pushButton1, 0,2)
        layout.addWidget(label2, 1,0)
        layout.addWidget(self.lineEdit2, 1,1)

        # 실질적으로 실행되는 부분
        self.setLayout(layout)

    def pushButtonClicked(self):
        self.id = self.lineEdit1.text()
        self.password = self.lineEdit2.text()
        self.close() # 화면만 닫아준다.

# CLASS
class MyWindow(QWidget): 
    def __init__(self): 
        super().__init__()
        self.setupUI() 

    # window widget
    def setupUI(self):

        # window title
        self.setWindowTitle("pyQt-19") 
        self.setWindowIcon(QIcon('icon.ico'))
        # windows의 위치 및 크기 정하기
        self.setGeometry(800,200,500,300)

        #버튼
        self.pushButton = QPushButton("Log In Dialog")
        self.pushButton.clicked.connect(self.pushButtonClicked)

        self.label = QLabel("==")

        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.pushButton)
        layout.addWidget(self.label)

        # 실질적으로 실행되는 부분
        self.setLayout(layout)

    def pushButtonClicked(self):
        # Dialog 띄우기-------------클래스 생성 필요
        dlg = LogInDialog() # 클래스 연결
        dlg.exec_() # 실행부분
        id = dlg.id
        password = dlg.password
        self.label.setText("id : %s \nPassword : %s"%(id,password))
        

if __name__ == "__main__": 
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_() 
