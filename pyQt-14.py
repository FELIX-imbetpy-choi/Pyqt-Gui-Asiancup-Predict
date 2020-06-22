# 중첩 Layout

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
        self.setWindowTitle("pyqt-14") 

        self.setWindowIcon(QIcon('icon.ico'))

        # windows의 위치 및 크기 정하기
        # setGeometry(x축 좌표, y축 좌표, x축 크기, y축 크기)
        self.setGeometry(800,200,500,300)

        # Check Box ------ 체크박스와 라디오버튼은 그룹으로 묶어서 넣어주어야 한다.
        # 나머지는 Vertiacal 으로 레이아웃에 묶고 마지막에 Horizontal 로 묶어주면 나열됨.
        groupBox = QGroupBox("학번")
        checkBox1 = QCheckBox("이름")
        checkBox2 = QCheckBox("총득점")
        checkBox3 = QCheckBox("국어")
        checkBox4 = QCheckBox("영어")
        checkBox5 = QCheckBox("수학")

        # Table
        tableWidget = QTableWidget(10,5)
        tableWidget.setHorizontalHeaderLabels(["이름","국어 점수","영어 점수","수학 점수","총점"])
        tableWidget.resizeColumnsToContents()
        tableWidget.resizeRowsToContents()

        # 왼쪽 Layout
        # Group Box 안에 체크박스 넣기
        leftInnerLayout = QVBoxLayout()
        leftInnerLayout.addWidget(checkBox1)
        leftInnerLayout.addWidget(checkBox2)
        leftInnerLayout.addWidget(checkBox3)
        leftInnerLayout.addWidget(checkBox4)
        leftInnerLayout.addWidget(checkBox5)
        groupBox.setLayout(leftInnerLayout)

        # 체크박스가 들어간 그룹박스를 leftLayOut에 넣기
        leftLayout = QVBoxLayout()
        leftLayout.addWidget(groupBox)

        # 오른쪽 Layout
        rightLayout = QVBoxLayout()
        rightLayout.addWidget(tableWidget)

        # 통합본
        layout = QHBoxLayout()
        layout.addLayout(leftLayout)
        layout.addLayout(rightLayout)

        # 실질적으로 실해되는 부분
        self.setLayout(layout)
 


if __name__ == "__main__":  # 프레임 워크 선언, 메인 메소드
    app = QApplication(sys.argv)
    mywindow = MyWindow() # MyWindow는 사용할 클라스고 mywindow는 인스턴스 (자바에서 new 해서 쓰는거랑 같음)
    mywindow.show() # show해야 화면에 보임
    app.exec_() # 실행
