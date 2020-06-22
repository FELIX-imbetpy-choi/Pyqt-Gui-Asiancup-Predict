# 숫자 값 받아오기

import sys # main이란 함수와 class를 인식하게 하기 위해
from PyQt5.QtWidgets import * # 위젯관련
from PyQt5.QtCore import * # 윈도우 전반적인 관련
from PyQt5.QtGui import *



class MyWindow(QWidget): 
    def __init__(self): 
        super().__init__()
        self.setupUI() 

    # window widget
    def setupUI(self):

        # window title
        self.setWindowTitle("pyQt-18") 
        self.setWindowIcon(QIcon('icon.ico'))
        # windows의 위치 및 크기 정하기
        self.setGeometry(800,200,500,300)

        #버튼
        self.pushButton = QPushButton("File Open")
        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.label = QLabel("이곳에 입력한 숫자가 뜹니다.")

        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.pushButton)
        layout.addWidget(self.label)

        # 실질적으로 실행되는 부분
        self.setLayout(layout)

    def pushButtonClicked(self):
        text, ok = QInputDialog.getInt(self, '숫자입력','숫자를 입력하세요') # 앞은 숫자값 , 뒤는 true false 값이 나옴
        if ok:
            self.label.setText(str(text))

if __name__ == "__main__":  # 프레임 워크 선언, 메인 메소드
    app = QApplication(sys.argv)
    mywindow = MyWindow() # MyWindow는 사용할 클라스고 mywindow는 인스턴스 (자바에서 new 해서 쓰는거랑 같음)
    mywindow.show() # show해야 화면에 보임
    app.exec_() # 실행
