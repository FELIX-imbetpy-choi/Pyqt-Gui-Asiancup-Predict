# 그래프 그리기

import sys # main이란 함수와 class를 인식하게 하기 위해
from PyQt5.QtWidgets import * # 위젯관련
from PyQt5.QtCore import * # 윈도우 전반적인 관련
from PyQt5.QtGui import *
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas # 여기서 그림 그리려면 필요한 함수



# CLASS
class MyWindow(QWidget): 
    def __init__(self): 
        super().__init__()
        self.setupUI() 

    # window widget
    def setupUI(self):

        # window title
        self.setWindowTitle("pyQt-20") 
        self.setWindowIcon(QIcon('icon.ico'))
        # windows의 위치 및 크기 정하기
        self.setGeometry(600,200,1200,600)

        #버튼
        self.pushButton1 = QPushButton("선그래프")
        self.pushButton1.clicked.connect(self.pushButton1Clicked)

        self.pushButton2 = QPushButton("막대그래프")
        self.pushButton2.clicked.connect(self.pushButton2Clicked)

        # Figure Canvas-------------추가
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig) # 캔버스를 만들어 놓고 그림을 그리는 구조 


        # layout
        leftLayout = QVBoxLayout()
        leftLayout.addWidget(self.canvas)

        rightLayout = QVBoxLayout()
        rightLayout.addWidget(self.pushButton1)
        rightLayout.addWidget(self.pushButton2)
        rightLayout.addStretch(1) # 버튼을 상단에 붙게 만들어줌

        layout = QHBoxLayout()
        layout.addLayout(leftLayout)
        layout.addLayout(rightLayout)
        layout.setStretchFactor(leftLayout, 1) 
        layout.setStretchFactor(rightLayout, 0) # 줄여도 버튼 크기가 줄어들지 않게 함

        # 실질적으로 실행되는 부분
        self.setLayout(layout)

    def pushButton1Clicked(self):
        s = pd.Series(np.random.randn(10).cumsum(), index=np.arange(0,100,10))
        ax = self.fig.add_subplot(111) # 항상 subplot으로 정해서 써줘야함 1행 1열 1번째
        ax.clear() # clear canvas
        ax.plot(s)
        self.canvas.draw()

    def pushButton2Clicked(self):
        animals = ['cat','dog','rabbit','horse']
        numbers = np.random.randn(4)
        ax2 = self.fig.add_subplot(111)
        ax2.clear()
        ax2.bar(animals, numbers)
        self.canvas.draw()
        

if __name__ == "__main__": 
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_() 
