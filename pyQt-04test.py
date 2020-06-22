# 레이블 글자 쓰기


import sys # main을 사용할 수 있게 함.
from PyQt5.QtWidgets import *
# from PyQt5.QtCore import * # 윈도우 전반적 내용 
from PyQt5 import QtCore # 위의 import 와 똑같은 내용

class MyWindow(QMainWindow):
    def __init__(self): 
        super().__init__()
        self.setupUI() 
    
    # Window Widget
    def setupUI(self): 
        # Window Title
        self.setWindowTitle("pyqt-04")
        # Window 의 위치 및 크기 정하기
        self.setGeometry(700, 400, 400, 200)

        # # Lable Text ---- 추가
        # textLabel = QLabel("Message : ", self)
        # textLabel.move(40, 20)

        # 클릭할 때 보여주는 Label - 다른 함수에 영향을 받도록 만듬
        # Label Data
        self.label = QLabel("Message : ", self) # 시작할 땐 아무것도 나오지 않게/ self 사용하여 함수에 영향 받도록
        self.label.move(30,20)
        self.label.resize(230, 30) # ( width, height )


        # Button 1 
        btn1 = QPushButton("Click ! ", self) 
        btn1.move(40,60) 
        # 
        btn1.clicked.connect(self.btn1_clicked) 

        # Button 2
        btn2 = QPushButton("Clear ! ", self) 
        btn2.move(140,60) 
        # 
        btn2.clicked.connect(self.btn2_clicked) 

    # Button Event
    def btn1_clicked(self):
        self.label.setText("Message : 버튼이 클릭되었습니다.")

      # Button Event
    def btn2_clicked(self):
        self.label.setText("Message : ")
        # self.label.clear() # settext("") 와 같은 기능을 함.



if __name__ == "__main__":
    app = QApplication(sys.argv) 
    mywindow = MyWindow()
    mywindow.show() 
    app.exec_() 
