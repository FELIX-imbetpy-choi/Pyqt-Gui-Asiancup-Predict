# lay out - grid

# layout - horizontal / vertical 두가지 있음 가로 / 세로 --> s
 
import sys # main이란 함수와 class를 인식하게 하기 위해
from PyQt5.QtWidgets import * # 위젯관련
from PyQt5.QtCore import * # 윈도우 전반적인 관련
from PyQt5.QtGui import *


class MyWindow(QWidget): # 클라스 만들때 제일 처음 사용하는게 QMainWindow - QMainWindow 사용하면 기본적 레이아웃 적용되어 있음
    def __init__(self): # self : 클라스안에 있는 것들만 실행(자바에서 this..), init은 제일 먼저 써야만 하는 함수임
        super().__init__() # 위에 클래스에서 init을 상속받아옴
        self.setupUI() # setupUI를 실행해라

    # window widget
    def setupUI(self):

        # window title
        self.setWindowTitle("pyQt-12") 
        self.setWindowIcon(QIcon('icon.ico'))
        self.setGeometry(800,200,300,100)

        self.label1 = QLabel("ID : ")
        self.label2 = QLabel("PW : ")
        self.linedit1 = QLineEdit()
        self.linedit2 = QLineEdit()

        # pushButton 
        self.pushButton1 = QPushButton("로그인")

        # lay out 생성 -------------추가
        # lay out 적용시 QMainWindow 를 Qwidget으로 변경 해 주어야 한다.
        # layout = QVBoxLayout()
        layout = QGridLayout() # 좌표값 지정 가능 
        layout.addWidget(self.label1, 0, 0)
        layout.addWidget(self.label2, 1, 0)
        layout.addWidget(self.linedit1, 0, 2)
        layout.addWidget(self.linedit2, 1, 2)
        layout.addWidget(self.pushButton1, 2, 2)

        self.setLayout(layout) # 실행부
        

     


if __name__ == "__main__":  # 프레임 워크 선언, 메인 메소드
    app = QApplication(sys.argv)
    mywindow = MyWindow() # MyWindow는 사용할 클라스고 mywindow는 인스턴스 (자바에서 new 해서 쓰는거랑 같음)
    mywindow.show() # show해야 화면에 보임
    app.exec_() # 실행
