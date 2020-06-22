# table teacher

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
        self.setWindowTitle("pyqt-09")
        # Window 의 위치 및 크기 정하기
        self.setGeometry(700, 400, 300, 300)
        self.setWindowIcon(QIcon('icon.ico'))

        # Table Widget ------추가
        self.tablewidget = QTableWidget(self)
        self.tablewidget.resize(290,290) # move는 쓰지 않는다. 기본적으로 0,0으로 설정되어 있엄.
        self.tablewidget.setRowCount(2) # row 갯수를 정할 수 있음
        self.tablewidget.setColumnCount(2) # column 갯수를 정함
        self.setTableWidget() # 함수실행

    def setTableWidget(self): # ----------추가
        self.tablewidget.setItem(0,0, QTableWidgetItem("(0,0)")) # 테이블 값 삽입 (0,0)위치에 (0,0) 삽입 
        self.tablewidget.setItem(0,1, QTableWidgetItem("(0,1)")) # QTableWidgetItem는 object로 데이터가 들어감
        self.tablewidget.setItem(1,0, QTableWidgetItem("(1,0)")) 
        self.tablewidget.setItem(1,1, QTableWidgetItem("(1,1)")) 

       
   
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    mywindow = MyWindow()
    mywindow.show() 
    app.exec_() 