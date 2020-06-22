# 종료 버튼 2가지 사용

import sys # main을 사용할 수 있게 함.
from PyQt5.QtWidgets import *
from PyQt5.QtCore import * # 윈도우 전반적 내용 

class MyWindow(QMainWindow):
    def __init__(self): 
        super().__init__()
        self.setupUI() 
    
    # Window Widget
    def setupUI(self): 
        # Window Title
        self.setWindowTitle("pyqt-02")
        # Window 의 위치 및 크기 정하기
        # setGeometry(x축 좌표, y축 좌표, x축 크기, y축 크기)
        self.setGeometry(500, 400, 400, 200)


        # Button
        btn1 = QPushButton("메세지", self) 
        btn2 = QPushButton("닫기", self)
        btn1.move(70,40) # 해당 Window 에서의 좌표 
        btn2.move(170,40)
        # 전체 윈도우 종료버튼
        btn1.clicked.connect(self.btn1_clicked) # 닫기는 기본제공. 함수 제작 필요 없음.
        # 해당 윈도우만 종료
        btn2.clicked.connect(QCoreApplication.instance().quit)

    # Button Event
    def btn1_clicked(self):
        QMessageBox.about(self, "메세지", "Clicked! \n 클릭했음") 
        QMessageBox.size(10)



if __name__ == "__main__":
    app = QApplication(sys.argv) 
    mywindow = MyWindow()
    mywindow.show() 
    app.exec_() 
