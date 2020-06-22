# 타이타닉 생존력 예측

import sys # main이란 함수와 class를 인식하게 하기 위해
from PyQt5.QtWidgets import * # 위젯관련
from PyQt5.QtCore import * # 윈도우 전반적인 관련
from PyQt5.QtGui import *
import pandas as pd
import numpy as np

# 데이터 불러오기
train_df = pd.read_csv('./data/train.csv',index_col='PassengerId')
train_df.head()
train_df['Embarked'].fillna('S',inplace=True)
# 예측 모델 생성
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
# scikit-learn을 사용하기 위해 컬럼을 수치화
# 원본은 두고 복사본 생성
train_df_T = train_df.copy()
# 예측을 위한 컬럼 확인
target_col = ['Pclass','Sex','Embarked']
train_df_T[target_col].head()
# 성별을 숫자로 전환
train_df_T.loc[train_df_T['Sex']=='male','Sex']=0
train_df_T.loc[train_df_T['Sex']=='female','Sex']=1
train_df_T[target_col].head()
train_df_T['Embarked_C']=train_df_T['Embarked'] == 'C'
train_df_T['Embarked_S']=train_df_T['Embarked'] == 'S'
train_df_T['Embarked_Q']=train_df_T['Embarked'] == 'Q'
train_df_T[['Embarked','Embarked_C','Embarked_S','Embarked_Q']].head()
# true flase는 머신러닝에서 자동으로 0과 1으로 들어간다.
target_col = ['Pclass','Sex','Embarked_C','Embarked_S','Embarked_Q']
# train 과 test의 비율조정(7:3비율)
train, test = train_test_split(train_df_T,test_size=0.3, random_state=0)
# train data 구성
# 모델 제작용 컬럼과 정답 컬럼을 구분
train_X = train[target_col]
train_Y = train['Survived']
# 테스트 데이터 만들기
test_X = test[target_col]
test_Y = test['Survived']
feature_one = train_X.values
target = train_Y.values
# model 생성
tree_model=DecisionTreeClassifier(max_depth=5)
# model 적용
tree_model.fit(feature_one,target)
# test Data로 예측모델 구현
pre = tree_model.predict(test_X)
# test Data의 예측력 확인
print('타이타닉 예측력 :',metrics.accuracy_score(pre,test_Y))

#예측하기
pre = tree_model.predict([[1,0,0,1,0]])




# 클래스 NEW
class PredictW(QDialog):
    def __init__(self): 
        super().__init__()
        self.setupUI()
        self.id = None # id값 설정
        self.password = None

    def setupUI(self):
        self.setGeometry(1100, 200, 300, 100)
        self.setWindowTitle("예측을 위한 입력")
        self.setWindowIcon(QIcon('icon.ico'))

        label1 = QLabel('Pclass(1,2,3) ')
        label2 = QLabel('Gender(0(남),1(여)) : ')
        label3 = QLabel('Embarked(0(C),1(S),2(Q)) : ')

        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.lineEdit3 = QLineEdit()

        self.pushButton1 = QPushButton("예측하기")
        self.pushButton1.clicked.connect(self.pushButtonClicked)

        # layout
        layout = QGridLayout()

        layout.addWidget(label1, 0,0)
        layout.addWidget(self.lineEdit1, 0,1)
        layout.addWidget(self.pushButton1, 0,2)
        layout.addWidget(label2, 1,0)
        layout.addWidget(self.lineEdit2, 1,1)
        layout.addWidget(label3, 2,0)
        layout.addWidget(self.lineEdit3, 2,1)

        # 실질적으로 실행되는 부분
        self.setLayout(layout)

    def pushButtonClicked(self):
        self.pclass = self.lineEdit1.text()
        self.gender = self.lineEdit2.text()
        self.embarked = self.lineEdit2.text()
        self.close() # 화면만 닫아준다.

# CLASS
class MyWindow(QWidget): 
    def __init__(self): 
        super().__init__()
        self.setupUI() 

    # window widget
    def setupUI(self):

        # window title
        self.setWindowTitle("타이타닉 예측") 
        self.setWindowIcon(QIcon('icon.ico'))
        # windows의 위치 및 크기 정하기
        self.setGeometry(800,200,500,300)

        #버튼
        self.pushButton1 = QPushButton("예측력 측정")
        self.pushButton1.clicked.connect(self.pushButton1Clicked)

        self.pushButton2 = QPushButton("예측하기")
        self.pushButton2.clicked.connect(self.pushButton2Clicked)

        # text
        self.label = QLabel('')


        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.pushButton1)
        layout.addWidget(self.pushButton2)
        layout.addWidget(self.label)

        # 실질적으로 실행되는 부분
        self.setLayout(layout)


    def pushButton1Clicked(self):
        pre = tree_model.predict(test_X)
        self.label.setText("예측력 : %0.4f"%metrics.accuracy_score(pre,test_Y))

    def pushButton2Clicked(self):
        # Dialog 띄우기-------------클래스 생성 필요
        dlg = PredictW() # 클래스 연결
        dlg.exec_() # 실행부분
        pre = tree_model.predict(test_X)
        pclass = dlg.pclass
        pclass = int(pclass)
        gender = dlg.gender
        gender = int(gender)
        embarked = dlg.embarked
        embarked = int(embarked)
        # embarked
        if embarked == 0: # C
            emb1 = 1
            emb2 = 0
            emb3 = 0
        elif embarked == 1: # S
            emb1 = 0
            emb2 = 1
            emb3 = 0
        else:
            emb1 = 0
            emb2 = 0
            emb3 = 1


        pre = tree_model.predict([[pclass,gender,emb1,emb2,emb3]])
        if pre == 0:
            msg = '생존'
        else:
            msg = '사망'
        self.label.setText("%s"%msg)
        

if __name__ == "__main__": 
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_() 
