import sys # main이란 함수와 class를 인식하게 하기 위해
from PyQt5.QtWidgets import * # 위젯관련
from PyQt5.QtCore import * # 윈도우 전반적인 관련
from PyQt5.QtGui import *

student_top5 = {
    'stcode' : ['19001', '19002','19003','19004','19005'],
    'stname' : ['홍길동','임꺽정','대장금','신선한','기발한'],
    'kor' : ['100','90','80','70','60'],
    'eng' : ['100','90','80','70','60'],
    'math' : ['100','90','80','70','60'],
    'total' : ['0','0','0','0','0']
}

column_idx_lookup = {'stcode':0, 'stname':1,'kor':2, 'eng':3, 'math':4, 'total':5}


class MyWindow(QWidget): # QMainWindow는 기본적으로 레이아웃 가지고있기 때문에 에러걸림
    def __init__(self): # self : 클라스안에 있는 것들만 실행(자바에서 this..), init은 제일 먼저 써야만 하는 함수임
        super().__init__() # 위에 클래스에서 init을 상속받아옴
        self.setupUI() # setupUI를 실행해라

    # window widget
    def setupUI(self):

        # window title
        self.setWindowTitle("pyQt-14teachers") 

        self.setWindowIcon(QIcon('star.png'))

        # windows의 위치 및 크기 정하기
        # setGeometry(x축 좌표, y축 좌표, x축 크기, y축 크기)
        self.setGeometry(800,200,500,300)

        # Check Box
        groupBox = QGroupBox("검색옵션")
        checkBox1 = QCheckBox("이름")
        checkBox2 = QCheckBox("총득점")
        checkBox3 = QCheckBox("국어")
        checkBox4 = QCheckBox("영어")
        checkBox5 = QCheckBox("수학")

        # Table
        self.tableWidget = QTableWidget(self) # 데이터가 바뀌어야하니까 self(이벤트가 발생하면 self붙여주기)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(6)
        self.setTableTotalCalc() # 총점계산
        self.setTableWidgetData() # 화면출력

        # 왼쪽 Layout
        # Group Box 안에 체크박스 넣기 - 체크 박스와 라디오 버튼의 경우만 그룹박스에 넣어주고 나머지는 그냥 VLayout만들어놓고 마지막에 HLayOut으로 합침
        leftInnerLayout = QVBoxLayout()
        leftInnerLayout.addWidget(checkBox1)
        leftInnerLayout.addWidget(checkBox2)
        leftInnerLayout.addWidget(checkBox3)
        leftInnerLayout.addWidget(checkBox4)
        leftInnerLayout.addWidget(checkBox5)
        groupBox.setLayout(leftInnerLayout) # 그룹박스에 체크박스들이 들어있는 레이아웃 추가 해줌

        # 체크박스가 들어간 그룹박스를 leftLayOut에 넣기
        leftLayout = QVBoxLayout()
        leftLayout.addWidget(groupBox)

        # 오른쪽 Layout
        rightLayout = QVBoxLayout()
        rightLayout.addWidget(self.tableWidget)

        # 통합본
        layout = QHBoxLayout()
        layout.addLayout(leftLayout)
        layout.addLayout(rightLayout)

        # 실질적으로 실행되는 부분
        self.setLayout(layout)

    def setTableTotalCalc(self):
        for i in range(5):
            calcTemp = int(student_top5['kor'][i]) + int(student_top5['eng'][i]) + int(student_top5['math'][i]) # int로 바꿔서 계산
            student_top5['total'][i] = str(calcTemp) # str로 바꿔서 넣어주기
        
    def setTableWidgetData(self):
        column_headers = ["학번","이름","국어 점수","영어 점수","수학 점수","총점"]
        self.tableWidget.setHorizontalHeaderLabels(column_headers)
        
        for k,v in student_top5.items():
            col = column_idx_lookup[k]
            for row, val in enumerate(v):
                item = QTableWidgetItem(val) # 테이블 위젯 데이터 넣고 빼고할때는 이렇게 해야함
                if col > 0:
                    item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight) # 세로축은 센터, 가로축은 오른쪽 정렬
                self.tableWidget.setItem(row,col,item)

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()


 


if __name__ == "__main__":  # 프레임 워크 선언, 메인 메소드
    app = QApplication(sys.argv)
    mywindow = MyWindow() # MyWindow는 사용할 클라스고 mywindow는 인스턴스 (자바에서 new 해서 쓰는거랑 같음)
    mywindow.show() # show해야 화면에 보임
    app.exec_() # 실행
