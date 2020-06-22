# table 심화

import sys # main이란 함수와 class를 인식하게 하기 위해
from PyQt5.QtWidgets import * # 위젯관련
from PyQt5.QtCore import * # 윈도우 전반적인 관련
from PyQt5.QtGui import *

student_top5 = {
    'stcode' : ['19001', '19002','19003','19004','19005'],
    'stname' : ['홍길동','임꺽정','대장금','신선한','기발한'],
    'stgrade' : ['100','90','80','70','60']
}
column_idx_lookup = {'stcode':0, 'stname':1,'stgrade':2}

class MyWindow(QMainWindow): # 클라스 만들때 제일 처음 사용하는게 QMainWindow
    def __init__(self): # self : 클라스안에 있는 것들만 실행(자바에서 this..), init은 제일 먼저 써야만 하는 함수임
        super().__init__() # 위에 클래스에서 init을 상속받아옴
        self.setupUI() # setupUI를 실행해라

    # window widget
    def setupUI(self):

        # window title
        self.setWindowTitle("pyQt-09") 

        self.setWindowIcon(QIcon('icon.ico'))

        # windows의 위치 및 크기 정하기
        self.setGeometry(700,400,300,300)
        
        # Table Widget
        self.tableWidget = QTableWidget(self)
        self.tableWidget.resize(290,290)
        self.tableWidget.setRowCount(5) # row 몇 개 쓸지
        self.tableWidget.setColumnCount(3) # column 몇 개 쓸지
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers) # 테이블 내용 수정 못하게 설정

        # 테이블에 데이터 넣는 함수 실행
        self.setTableWidetData()

    def setTableWidetData(self):
        # 컬럼 헤더 값 넣기
        column_header = ['학번','성명','점수']        
        self.tableWidget.setHorizontalHeaderLabels(column_header) 

        # 키값 value값 가져오기 ----------- for 문 충분히 이해하기.
        for k,v in student_top5.items():
            col = column_idx_lookup[k] # 0,1,2가 들어옴
            for row, val in enumerate(v): # 해당 value값이 몇번째 값인지 알기 위해
                item = QTableWidgetItem(val)
                # 점수 컬럼의 데이터는 오른쪽 정렬 + 중앙으로 조정
                if col == 2:
                    item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter) 
                self.tableWidget.setItem(row,col,item)

        self.tableWidget.resizeColumnsToContents() # 열 크기를 데이터에 맞게 조정
        self.tableWidget.resizeRowsToContents() # 행 크기를 데이터에 맞게 조정


if __name__ == "__main__":  # 프레임 워크 선언, 메인 메소드
    app = QApplication(sys.argv)
    mywindow = MyWindow() # MyWindow는 사용할 클라스고 mywindow는 인스턴스 (자바에서 new 해서 쓰는거랑 같음)
    mywindow.show() # show해야 화면에 보임
    app.exec_() # 실행
