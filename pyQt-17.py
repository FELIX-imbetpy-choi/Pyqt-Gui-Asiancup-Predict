# File 위치 불러오기

import sys # main이란 함수와 class를 인식하게 하기 위해
from PyQt5.QtWidgets import * # 위젯관련
from PyQt5.QtCore import * # 윈도우 전반적인 관련
from PyQt5.QtGui import *



class MyWindow(QWidget): # QMainWindow는 기본적으로 레이아웃 가지고있기 때문에 에러걸림
    def __init__(self): # self : 클라스안에 있는 것들만 실행(자바에서 this..), init은 제일 먼저 써야만 하는 함수임
        super().__init__() # 위에 클래스에서 init을 상속받아옴
        self.setupUI() # setupUI를 실행해라

    # window widget
    def setupUI(self):

        # window title
        self.setWindowTitle("pyQt-17") 

        self.setWindowIcon(QIcon('icon.ico'))

        # windows의 위치 및 크기 정하기
        # setGeometry(x축 좌표, y축 좌표, x축 크기, y축 크기)
        self.setGeometry(800,200,500,300)

        self.pushButton = QPushButton("File Open")
        self.pushButton.clicked.connect(self.pushButtonClicked)

        self.label = QLabel("이곳에 파일 위치 이름이 보입니다.")

        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.pushButton)
        layout.addWidget(self.label)

        # 실질적으로 실행되는 부분
        self.setLayout(layout)

    def pushButtonClicked(self):
        fname = QFileDialog.getOpenFileName(self) # filename을 쓰면 1개만 받아옴
        self.label.setText(fname[0])
        print(fname)

if __name__ == "__main__":  # 프레임 워크 선언, 메인 메소드
    app = QApplication(sys.argv)
    mywindow = MyWindow() # MyWindow는 사용할 클라스고 mywindow는 인스턴스 (자바에서 new 해서 쓰는거랑 같음)
    mywindow.show() # show해야 화면에 보임
    app.exec_() # 실행
