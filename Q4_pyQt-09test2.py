# table test2

import sys 
from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtGui import * 
import pandas as pd
import numpy as np


student_top5 = {
    'stcode' : ['190001','190002','190003','190004','190005'],
    'stname' : ['홍길동','임꺽정','대장금','신선한','기발한'],
    'stgrade' : ['100','90','80','70','60'],
}

class MyWindow(QMainWindow):
    def __init__(self): 
        super().__init__()
        self.setupUI() 
    
    # Window Widget
    def setupUI(self): 
        # Window Title
        self.setWindowTitle("Q4_pyQt-09test2")
        # Window 의 위치 및 크기 정하기
        self.setGeometry(700, 400, 700, 700)
        self.setWindowIcon(QIcon('icon.ico'))

        # Table Widget ------추가
        self.tablewidget = QTableWidget(self)
        self.tablewidget.resize(690,690) # move는 쓰지 않는다. 기본적으로 0,0으로 설정되어 있엄.
        self.tablewidget.setRowCount(5) # row 갯수를 정할 수 있음
        self.tablewidget.setColumnCount(3) # column 갯수를 정함
        self.tablewidget.setHorizontalHeaderItem(0,QTableWidgetItem(str("번호")))
        self.tablewidget.setHorizontalHeaderItem(1,QTableWidgetItem(str("성명")))
        self.tablewidget.setHorizontalHeaderItem(2,QTableWidgetItem(str("점수")))
        self.setTableWidget() # 함수실행
        

    def setTableWidget(self): # ----------추가
        kk = pd.DataFrame(student_top5)
        kk.columns = [0,1,2]
        for i in range(0,5):
            for k in range(0,3):
                print(kk.loc[i,k])
                target = kk.loc[i,k]
                self.tablewidget.setItem(i,k, QTableWidgetItem("%s"%target)) # 테이블 값 삽입 (0,0)위치에 (0,0) 삽입 

       
   
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    mywindow = MyWindow()
    mywindow.show() 
    app.exec_() 