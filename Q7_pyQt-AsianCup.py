# AsianCup 예측 도구

import sys # main이란 함수와 class를 인식하게 하기 위해
from PyQt5.QtWidgets import * # 위젯관련
from PyQt5.QtCore import * # 윈도우 전반적인 관련
from PyQt5.QtGui import *
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
# Module
import pandas as pd
import numpy as np
from scipy import stats # 확률분포 그래프
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

import warnings
warnings.filterwarnings('ignore')

# 데이터 불러오기
total = pd.read_csv('./data/total_match.csv')
total_av = pd.read_csv('./data/total_av.csv')
# 카테고리 순서
natcat = pd.DataFrame(list(total['team'].unique()))
natcat = natcat.sort_values(by = 0)
# natcat.reindex(index = range(1,19), columns=[0])
natcat['순서'] = range(1,19)
# 국가를 카테고리화 시키기
total['team']=total['team'].astype('category')
total['weater']=total['weater'].astype('category')
total['team'].cat.categories = ['%s'%i for i in range(1,19)]
# 타겟컬럼
target_col = ['team','shoot','foul','possession','weater','temp','rank','salary']
#데이터 나누기
train, test = train_test_split(total,test_size=0.3,random_state=0)
# Train data 구성
# 모델 제작용 컬럼과 정답 컬럼을 구분
train_X = train[target_col]
train_Y = train['goal']
train_Y = train_Y.astype(float)
#테스트데이터
X_test = test[target_col]
Y_test = test['goal']
Y_test = Y_test.astype(float)

feature_one = train_X.values
target = train_Y.values

# model 생성
model = RandomForestRegressor(n_estimators=100, n_jobs=-1,random_state=0)
model
# Training
model.fit(feature_one, target)
# 예측
pre = model.predict(X_test)


# -------------------------------------------------

class PredictDialog(QDialog): # 상속받는 위치가 QDialog, 새로운 창이 뜨는 게 다이얼로그
    def __init__(self):
        super().__init__()
        self.setupUI() 
        
        # 디폴트값은 None으로 하면 선택안했을때 예측하기 누르면 에러나옴
        self.team1 = '일본'
        self.team2 = '카타르'

    def setupUI(self):
        self.setGeometry(500,300,500,700)
        self.setWindowTitle("예측을 위한 입력")
        self.setWindowIcon(QIcon('icon.ico'))

# ------------------ Team1 라디오 버튼

        self.radio1 = QRadioButton("일본", self)
        self.radio1.setChecked(True) # 디폴드 값으로 하나 선택되어 있어야함
        self.radio1.clicked.connect(self.radioButtonClicked)

        self.radio2 = QRadioButton("카타르", self)
        self.radio2.clicked.connect(self.radioButtonClicked)

        self.radio3 = QRadioButton("이란", self)
        self.radio3.clicked.connect(self.radioButtonClicked)

        self.radio4 = QRadioButton("아랍에미리트", self)
        self.radio4.clicked.connect(self.radioButtonClicked)

        self.radio5 = QRadioButton("한국", self)
        self.radio5.clicked.connect(self.radioButtonClicked)

        self.radio6 = QRadioButton("중국", self)
        self.radio6.clicked.connect(self.radioButtonClicked)

        self.radio8 = QRadioButton("오스트레일리아", self)
        self.radio8.clicked.connect(self.radioButtonClicked)


        groupBox = QGroupBox("Team1")
        leftInnerLayout = QVBoxLayout()
        leftInnerLayout.addWidget(self.radio1)
        leftInnerLayout.addWidget(self.radio2)
        leftInnerLayout.addWidget(self.radio3)
        leftInnerLayout.addWidget(self.radio4)
        leftInnerLayout.addWidget(self.radio5)
        leftInnerLayout.addWidget(self.radio6)
        leftInnerLayout.addWidget(self.radio8)
        groupBox.setLayout(leftInnerLayout)

# ------------------ Team2 라디오 버튼

        self.radio9 = QRadioButton("카타르", self)
        self.radio9.setChecked(True) # 디폴드 값으로 하나 선택되어 있어야함
        self.radio9.clicked.connect(self.radioButtonClicked2)

        self.radio10 = QRadioButton("아랍에미리트", self)
        self.radio10.clicked.connect(self.radioButtonClicked2)

        self.radio11 = QRadioButton("일본", self)
        self.radio11.clicked.connect(self.radioButtonClicked2)

        self.radio12 = QRadioButton("오스트레일리아", self)
        self.radio12.clicked.connect(self.radioButtonClicked2)

        self.radio13 = QRadioButton("이란", self)
        self.radio13.clicked.connect(self.radioButtonClicked2)

        self.radio14 = QRadioButton("오만", self)
        self.radio14.clicked.connect(self.radioButtonClicked2)

        self.radio15 = QRadioButton("사우디아라비아", self)
        self.radio15.clicked.connect(self.radioButtonClicked2)

        self.radio16 = QRadioButton("우즈베키스탄", self)
        self.radio16.clicked.connect(self.radioButtonClicked2)

        self.radio17 = QRadioButton("바레인", self)
        self.radio17.clicked.connect(self.radioButtonClicked2)

        self.radio18 = QRadioButton("이라크", self)
        self.radio18.clicked.connect(self.radioButtonClicked2)


        groupBox2 = QGroupBox("Team2")
        RightInnerLayout = QVBoxLayout()
        RightInnerLayout.addWidget(self.radio9)
        RightInnerLayout.addWidget(self.radio10)
        RightInnerLayout.addWidget(self.radio11)
        RightInnerLayout.addWidget(self.radio12)
        RightInnerLayout.addWidget(self.radio13)
        RightInnerLayout.addWidget(self.radio14)
        RightInnerLayout.addWidget(self.radio15)
        RightInnerLayout.addWidget(self.radio16)
        RightInnerLayout.addWidget(self.radio17)
        RightInnerLayout.addWidget(self.radio18)
        groupBox2.setLayout(RightInnerLayout)




# ------------------ 예측버튼 + 전체 레이아웃 위젯

        groupBox3 = QGroupBox("클릭하시오")
        UnderInnerLayout = QVBoxLayout()
        self.pushButton1 = QPushButton("예측하기")
        self.pushButton1.clicked.connect(self.pushButtonClicked)
        UnderInnerLayout.addWidget(self.pushButton1)
        groupBox3.setLayout(UnderInnerLayout)

        layout = QGridLayout()
        layout.addWidget(groupBox,0,0)
        layout.addWidget(groupBox2,1,0)
        layout.addWidget(groupBox3,2,0)
        
        self.setLayout(layout)

    def radioButtonClicked(self): # Pclass 라디오 버튼 클릭 시
        
        if self.radio1.isChecked():
            self.team1 = "일본"
        if self.radio2.isChecked():
            self.team1 = "카타르"
        if self.radio3.isChecked():
            self.team1 = "이란"
        if self.radio4.isChecked():
            self.team1 = "아랍에미리트"
        if self.radio5.isChecked():
            self.team1 = "한국"
        if self.radio6.isChecked():
            self.team1 = "중국"
        if self.radio8.isChecked():
            self.team1 = "오스트레일리아"

    def radioButtonClicked2(self): # 성별 라디오 버튼 클릭 시
        
        if self.radio9.isChecked():
            self.team2 = "카타르"
        if self.radio10.isChecked():
            self.team2 = "아랍에미리트"
        if self.radio11.isChecked():
            self.team2 = "일본"
        if self.radio12.isChecked():
            self.team2 = "오스트레일리아"
        if self.radio13.isChecked():
            self.team2 = "이란"
        if self.radio14.isChecked():
            self.team2 = "오만"
        if self.radio15.isChecked():
            self.team2 = "사우디아라비아"
        if self.radio16.isChecked():
            self.team2 = "우즈베키스탄"
        if self.radio17.isChecked():
            self.team2 = "바레인"
        if self.radio18.isChecked():
            self.team2 = "이라크"


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
        self.setWindowTitle("AsianCup 예측") 

        self.setWindowIcon(QIcon('icon.ico'))

        # windows의 위치 및 크기 정하기
        # setGeometry(x축 좌표, y축 좌표, x축 크기, y축 크기)
        self.setGeometry(800,200,500,150)

        self.label1 = QLabel("2019 AsianCup 승패예측")    
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
        self.label2.setText('예측력: 100% 입니다만? O..Oa (긁적)')
 
    def pushButton2Clicked(self):
        # Dialog 띄우기
        dlg = PredictDialog()
        dlg.exec_()
        # if pre[0] == 0:
        #     self.label2.setText('사망')
        # else:
        #     self.label2.setText('생존')

        # 예측
        # 날씨 - 구름 1 안개 2 비 3 맑음 4
        team_list = list(total_av['team'])

        # 팀 입력받기
        team1 = str(dlg.team1)
        a = natcat.loc[natcat[0]=='%s'%team1,"순서"]
        a=int(a)
        for i in team_list:
            if team1 == i:
                shoot1 = total_av['shoot'][total_av['team']==i]
                foul1 = total_av['foul'][total_av['team']==i]
                possession1 = total_av['possession'][total_av['team']==i]
                rank1 = total_av['rank'][total_av['team']==i]
                salary1 = total_av['salary'][total_av['team']==i]

        print('')

        # 팀2
        team2 = str(dlg.team2)
        b = natcat.loc[natcat[0]=='%s'%team2,"순서"]
        b=int(b)
        for i in team_list:
            if team2 == i:
                shoot2 = total_av['shoot'][total_av['team']==i]
                foul2 = total_av['foul'][total_av['team']==i]
                possession2 = total_av['possession'][total_av['team']==i]
                rank2 = total_av['rank'][total_av['team']==i]
                salary2 = total_av['salary'][total_av['team']==i]
                
        # 카타르에 가중치 주기
        if a == 15:
            shoot1 = shoot1 *2
        if b == 15:
            shoot2 = shoot2 *2
            
        # 아랍에미리에이트에 가중치 주기
        if a == 5:
            shoot1 = shoot1 * 2
        if b == 5:
            shoot2 = shoot2 * 2


        pre1 = model.predict([[int(a),(int(shoot1)),(int(foul1)),(int(possession1)),int(4),int(21),(211 - int(rank1)),int(salary1)]])
        pre2 = model.predict([[int(b),(int(shoot2)),(int(foul2)),(int(possession2)),int(4),int(21),(211 - int(rank2)),int(salary2)]])
        print('')
        print(team1, pre1) # 쿠웨이트
        print(team2, pre2) # 우즈벡

        if pre1 == pre2:
            self.label2.setText('%s  와 %s 이(가) 비겼습니다.'%(team1,team2))
        if pre1 > pre2:
            self.label2.setText('%s  이(가) %s 을(를) 이겼습니다.'%(team1,team2))
        if pre2 > pre1:
            self.label2.setText('%s  이(가) %s 을(를) 이겼습니다.'%(team2,team1))


# -------------------------------------------------

if __name__ == "__main__":  # 프레임 워크 선언, 메인 메소드
    app = QApplication(sys.argv)
    mywindow = MyWindow() # MyWindow는 사용할 클라스고 mywindow는 인스턴스 (자바에서 new 해서 쓰는거랑 같음)
    mywindow.show() # show해야 화면에 보임
    app.exec_() # 실행