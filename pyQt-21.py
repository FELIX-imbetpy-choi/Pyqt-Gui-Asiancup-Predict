import sys # main이란 함수와 class를 인식하게 하기 위해
from PyQt5.QtWidgets import * # 위젯관련
from PyQt5.QtCore import * # 윈도우 전반적인 관련
from PyQt5.QtGui import *
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

train_df = pd.read_csv('./data/train.csv')
train_df.set_index('PassengerId', inplace=True)
train_df['Embarked'].fillna('S', inplace=True)

train_df_T = train_df.copy()
train_df_T.loc[train_df_T['Sex']=='male','Sex'] = 0
train_df_T.loc[train_df_T['Sex']=='female','Sex'] = 1

train_df_T['Embarked_C'] = train_df_T['Embarked'] == 'C'
train_df_T['Embarked_S'] = train_df_T['Embarked'] == 'S'
train_df_T['Embarked_Q'] = train_df_T['Embarked'] == 'Q'

target_col = ['Pclass','Sex','Embarked_C','Embarked_S','Embarked_Q']

train, test = train_test_split(train_df_T, test_size = 0.3, random_state = 0)

train_X = train[target_col]
train_Y = train['Survived']

test_X = test[target_col]
test_Y = test['Survived']

feature_one = train_X.values
target = train_Y.values

tree_model = DecisionTreeClassifier(max_depth=5)
tree_model.fit(X=feature_one, y=target)

pre = tree_model.predict(test_X)

# -------------------------------------------------

class LogInDialog(QDialog): # 상속받는 위치가 QDialog, 새로운 창이 뜨는 게 다이얼로그
    def __init__(self):
        super().__init__()
        self.setupUI() 
        
        # 디폴트값은 None으로 하면 선택안했을때 예측하기 누르면 에러나옴
        self.msg = '1'
        self.sex = '0'
        self.embarked_S = '1'
        self.embarked_C = '0'
        self.embarked_Q = '0'

    def setupUI(self):
        self.setGeometry(1100,200,300,300)
        self.setWindowTitle("예측을 위한 입력")
        self.setWindowIcon(QIcon('star.png'))

# ------------------ Pclass 라디오 버튼

        self.radio1 = QRadioButton("A", self)
        self.radio1.setChecked(True) # 디폴드 값으로 하나 선택되어 있어야함
        self.radio1.clicked.connect(self.radioButtonClicked)

        self.radio2 = QRadioButton("B", self)
        self.radio2.clicked.connect(self.radioButtonClicked)

        self.radio3 = QRadioButton("C", self)
        self.radio3.clicked.connect(self.radioButtonClicked)

        groupBox = QGroupBox("객실등급")
        leftInnerLayout = QHBoxLayout()
        leftInnerLayout.addWidget(self.radio1)
        leftInnerLayout.addWidget(self.radio2)
        leftInnerLayout.addWidget(self.radio3)
        groupBox.setLayout(leftInnerLayout)

# ------------------ 성별 라디오 버튼 Gender(0:남, 1:여)

        self.radio4 = QRadioButton("남자", self)
        self.radio4.setChecked(True) # 디폴드 값으로 하나 선택되어 있어야함
        self.radio4.clicked.connect(self.radioButtonClicked2)

        self.radio5 = QRadioButton("여자", self)
        self.radio5.clicked.connect(self.radioButtonClicked2)

        groupBox2 = QGroupBox("성별선택")
        leftInnerLayout2 = QHBoxLayout()
        leftInnerLayout2.addWidget(self.radio4)
        leftInnerLayout2.addWidget(self.radio5)
        groupBox2.setLayout(leftInnerLayout2)

# ------------------ 항구 선택 라디오 버튼

        self.radio6 = QRadioButton("S", self)
        self.radio6.setChecked(True) # 디폴드 값으로 하나 선택되어 있어야함
        self.radio6.clicked.connect(self.radioButtonClicked3)

        self.radio7 = QRadioButton("C", self)
        self.radio7.clicked.connect(self.radioButtonClicked3)

        self.radio8 = QRadioButton("Q", self)
        self.radio8.clicked.connect(self.radioButtonClicked3)

        groupBox3 = QGroupBox("탑승항구")
        leftInnerLayout3 = QHBoxLayout()
        leftInnerLayout3.addWidget(self.radio6)
        leftInnerLayout3.addWidget(self.radio7)
        leftInnerLayout3.addWidget(self.radio8)
        groupBox3.setLayout(leftInnerLayout3)


# ------------------ 예측버튼 + 전체 레이아웃 위젯

        self.pushButton1 = QPushButton("예측하기")
        self.pushButton1.clicked.connect(self.pushButtonClicked)

        layout = QGridLayout()
        layout.addWidget(groupBox,0,0)
        layout.addWidget(self.pushButton1,0,1)
        layout.addWidget(groupBox2,1,0)
        layout.addWidget(groupBox3,2,0)
        

        self.setLayout(layout)

    def radioButtonClicked(self): # Pclass 라디오 버튼 클릭 시
        
        if self.radio1.isChecked():
            self.msg = "1"
        if self.radio2.isChecked():
            self.msg = "2"
        if self.radio3.isChecked():
            self.msg = "3"

    def radioButtonClicked2(self): # 성별 라디오 버튼 클릭 시
        
        if self.radio4.isChecked():
            self.sex = "0"
        if self.radio5.isChecked():
            self.sex = "1"

    def radioButtonClicked3(self): # 항구 라디오 버튼 클릭 시
        
        if self.radio6.isChecked():
            self.embarked_S = "1"
            self.embarked_C = "0"
            self.embarked_Q = "0"
        if self.radio7.isChecked():
            self.embarked_S = "0"
            self.embarked_C = "1"
            self.embarked_Q = "0"
        if self.radio8.isChecked():
            self.embarked_S = "0"
            self.embarked_C = "0"
            self.embarked_Q = "1"

    def pushButtonClicked(self):
        self.close() # "화면" 닫기

# -------------------------------------------------

class MyWindow(QWidget): # QMainWindow는 기본적으로 레이아웃 가지고있기 때문에 에러걸림
    def __init__(self): # self : 클라스안에 있는 것들만 실행(자바에서 this..), init은 제일 먼저 써야만 하는 함수임
        super().__init__() # 위에 클래스에서 init을 상속받아옴
        self.setupUI() # setupUI를 실행해라

    # window widget
    def setupUI(self):

        # window title
        self.setWindowTitle("pyqt-21") 

        self.setWindowIcon(QIcon('star.png'))

        # windows의 위치 및 크기 정하기
        # setGeometry(x축 좌표, y축 좌표, x축 크기, y축 크기)
        self.setGeometry(800,200,300,200)

        self.label1 = QLabel("타이타닉호의 생존여부 예측(객실등급, 성별)")    
        self.label2 = QLabel("")    
        self.pushButton1 = QPushButton("예측력 측정")
        self.pushButton1.clicked.connect(self.pushButton1Clicked)

        self.pushButton2 = QPushButton("예측하기")
        self.pushButton2.clicked.connect(self.pushButton2Clicked)

        # layout 생성
        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.pushButton1)
        layout.addWidget(self.pushButton2)
        layout.addWidget(self.label2)

        # 실질적으로 실해되는 부분
        self.setLayout(layout)

    def pushButton1Clicked(self):
        self.label2.setText('예측력: '+str(metrics.accuracy_score(pre, test_Y)))
 
    def pushButton2Clicked(self):
        # Dialog 띄우기
        dlg = LogInDialog()
        dlg.exec_()
        pclass = str(dlg.msg)
        gender = str(dlg.sex)
        embarked_S = str(dlg.embarked_S)
        embarked_C = str(dlg.embarked_C)
        embarked_Q = str(dlg.embarked_Q)

        pre = tree_model.predict([['%d'%int(pclass), '%d'%int(gender), '%d'%int(embarked_S), '%d'%int(embarked_C), '%d'%int(embarked_Q)]])
        if pre[0] == 0:
            self.label2.setText('사망')
        else:
            self.label2.setText('생존')


# -------------------------------------------------

if __name__ == "__main__":  # 프레임 워크 선언, 메인 메소드
    app = QApplication(sys.argv)
    mywindow = MyWindow() # MyWindow는 사용할 클라스고 mywindow는 인스턴스 (자바에서 new 해서 쓰는거랑 같음)
    mywindow.show() # show해야 화면에 보임
    app.exec_() # 실행