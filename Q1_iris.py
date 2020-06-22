# iris 머신러닝

import sys 
from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
from PyQt5 import QtCore

# 머신러닝
# SVM(support vector machine)을 이용한 분류
import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
from sklearn import svm, metrics, model_selection
from sklearn.neighbors import KNeighborsClassifier #KNN분류기
knn = KNeighborsClassifier(n_neighbors = 3)

# 데이터 불러오기
csv = pd.read_csv('./data/iris.csv')

# Training 과 Test 분리하기
csv_data=csv[['SepalLength','SepalWidth','PetalLength','PetalWidth']]
csv_label = csv['Name']
train_data, test_data, train_label, test_label = train_test_split(csv_data, csv_label)
 
# Training 데이터 학습시키기
knn.fit(train_data,train_label)
 
 
# # 데이터 예측하기
# pre=knn.predict([[5.1, 3.0, 1.3, 0.2]])
# print('예측 : {}'.format(pre))
 



class MyWindow(QMainWindow):
    def __init__(self): 
        super().__init__()
        self.setupUI() 
    
    # Window Widget
    def setupUI(self): 
        # Window Title
        self.setWindowTitle("iris")
        # Window 의 위치 및 크기 정하기
        self.setGeometry(700, 400, 400, 200)

        # Lable Text
        textLabel = QLabel(" Sepal.Length : ", self)
        textLabel.move(20, 20)

        textLabel = QLabel(" Sepal.Width : ", self)
        textLabel.move(20, 50)

        textLabel = QLabel(" Petal.Length : ", self)
        textLabel.move(20, 80)

        textLabel = QLabel(" Sepal.Width : ", self)
        textLabel.move(20, 110)
    
        # Line Edit ---------- 추가
        self.lineEdit1 = QLineEdit("", self)
        self.lineEdit1.move(150, 20)
        self.lineEdit1.resize(170, 30)
        # 이벤트 추가
        # self.lineEdit.textChanged.connect(self.lineEditChanged) # 글씨가 하나라도 쳐지면 lineEditChanged- 함수에 연결을 해라.
        # self.lineEdit.returnPressed.connect(self.lineEditChanged) # lineEdit에서 Enter 를 눌렀을 때 lineEditChanged- 함수에 연결을 해라.

        self.lineEdit2 = QLineEdit("", self)
        self.lineEdit2.move(150, 50)
        self.lineEdit2.resize(170, 30)

        self.lineEdit3 = QLineEdit("", self)
        self.lineEdit3.move(150, 80)
        self.lineEdit3.resize(170, 30)

        self.lineEdit4 = QLineEdit("", self)
        self.lineEdit4.move(150, 110)
        self.lineEdit4.resize(170, 30)

        # Status Bar --------- 추가 line edit 연결
        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

        # Button 1 
        btn1 = QPushButton("Click ! ", self) 
        btn1.move(200,150) 
        btn1.clicked.connect(self.lineEditChanged) 

    def lineEditChanged(self):
        pre=knn.predict([[float(self.lineEdit1.text()), float(self.lineEdit2.text()), float(self.lineEdit3.text()), float(self.lineEdit4.text())]])
        self.statusBar.showMessage('예측 : {}'.format(pre)) # statusbar 로 lineEdit 의 메세지를 넘겨준다.

 
# # 데이터 예측하기
# pre=knn.predict([[5.1, 3.0, 1.3, 0.2]])
# print('예측 : {}'.format(pre))

if __name__ == "__main__":
    app = QApplication(sys.argv) 
    mywindow = MyWindow()
    mywindow.show() 
    app.exec_() 

