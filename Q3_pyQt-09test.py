# table test

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
        self.setWindowTitle("Q3_pyQt-09test")
        # Window 의 위치 및 크기 정하기
        self.setGeometry(700, 400, 700, 700)
        self.setWindowIcon(QIcon('icon.ico'))

        # Table Widget ------추가
        self.tablewidget = QTableWidget(self)
        self.tablewidget.resize(690,690) # move는 쓰지 않는다. 기본적으로 0,0으로 설정되어 있엄.
        self.tablewidget.setRowCount(6) # row 갯수를 정할 수 있음
        self.tablewidget.setColumnCount(3) # column 갯수를 정함
        self.tablewidget.setHorizontalHeaderItem(0,QTableWidgetItem(str("번호")))
        self.tablewidget.setHorizontalHeaderItem(1,QTableWidgetItem(str("성명")))
        self.tablewidget.setHorizontalHeaderItem(2,QTableWidgetItem(str("점수")))
        self.setTableWidget() # 함수실행
        

    def setTableWidget(self): # ----------추가
        self.tablewidget.setItem(0,0, QTableWidgetItem("(0,0)")) # 테이블 값 삽입 (0,0)위치에 (0,0) 삽입 

       
   
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    mywindow = MyWindow()
    mywindow.show() 
    app.exec_() 