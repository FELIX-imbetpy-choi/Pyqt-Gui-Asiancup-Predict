# RottenT DB / CSV 

import sys 
from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtGui import * # -----추가 아이콘 사용
# 사용 모듈
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request as req
# Sql 사용
from sqlalchemy import create_engine 


class MyWindow(QMainWindow):
    def __init__(self): 
        super().__init__()
        self.setupUI() 
    
    # Window Widget
    def setupUI(self): 
        # Window Title
        self.setWindowTitle("RottenTomatoes Scrapy")
        # Window 의 위치 및 크기 정하기
        self.setGeometry(700, 400, 400, 200)
        # 아아콘
        self.setWindowIcon(QIcon('icon.ico'))

        # Lable Text
        textLabel = QLabel(" 년도 : ", self)
        textLabel.move(20, 20)

        # Lable Text
        self.textLabel2 = QLabel(" 결과 : ", self)
        self.textLabel2.move(100, 120)

    
        # Line Edit ---------- 추가
        self.lineEdit1 = QLineEdit("", self)
        self.lineEdit1.move(150, 20)
        self.lineEdit1.resize(170, 30)
        # 이벤트 추가
        # self.lineEdit.textChanged.connect(self.lineEditChanged) # 글씨가 하나라도 쳐지면 lineEditChanged- 함수에 연결을 해라.
        # self.lineEdit.returnPressed.connect(self.lineEditChanged) # lineEdit에서 Enter 를 눌렀을 때 lineEditChanged- 함수에 연결을 해라.



        # Button 1 -- CSV 저장
        btn1 = QPushButton("1. CSV 만들기", self) 
        btn1.move(20,70) 
        btn1.resize(170, 30)
        btn1.clicked.connect(self.btn1_clicked) 
        

        
        # Button 2 -- DB에 저장
        btn2 = QPushButton("2. DB 저장하기", self) 
        btn2.move(200,70) 
        btn2.resize(170, 30)
        btn2.clicked.connect(self.btn2_clicked) 

    def lineEditChanged1(self):
        self.lineEdit1.text()

    def lineEditChanged2(self):
        self.lineEdit1.text()

    # Button Event
    def btn1_clicked(self):
        # HTML
        url = 'http://www.rottentomatoes.com/top/bestofrt/?year=%s'%(self.lineEdit1.text())
        res = req.urlopen(url)
        # HTML 분석
        soup = BeautifulSoup(res, 'html.parser')
        # 데이터 추출하기
        aprice = soup.select('#top_movies_main > div > table > tr > td > a')
        num = 0
        list1 = []
        for i in aprice:
            data = []
            num=num+1
            data.append(num)
            data.append(i.string.strip())
            list1.append(data)
        
        ml=pd.DataFrame(list1)

        count = 0
        Tlist = []
        for i in ml[1]:
            smallist = []
            count += 1
            smallist.append(count)
            smallist.append(i.replace("(2018)",""))
            Tlist.append(smallist)
            
        Mtitle = pd.DataFrame(Tlist)
        Mtitle['year'] = 2018
        Mtitle.columns = ['rank', 'title', 'year']
        
        Mtitle.to_csv('./data/Movie%s.csv'%(self.lineEdit1.text()),index=False,encoding='utf-8') 

        self.textLabel2.setText("결과 : CSV 를만들었습니다.")
        self.textLabel2.resize(250, 30)

      # Button Event
    def btn2_clicked(self):
         # HTML
        url = 'http://www.rottentomatoes.com/top/bestofrt/?year=%s'%(self.lineEdit1.text())
        res = req.urlopen(url)
        # HTML 분석
        soup = BeautifulSoup(res, 'html.parser')
        # 데이터 추출하기
        aprice = soup.select('#top_movies_main > div > table > tr > td > a')
        num = 0
        list1 = []
        for i in aprice:
            data = []
            num=num+1
            data.append(num)
            data.append(i.string.strip())
            list1.append(data)
        
        ml=pd.DataFrame(list1)

        count = 0
        Tlist = []
        for i in ml[1]:
            smallist = []
            count += 1
            smallist.append(count)
            smallist.append(i.replace("(2018)",""))
            Tlist.append(smallist)
            
        Mtitle = pd.DataFrame(Tlist)
        Mtitle['year'] = 2018
        Mtitle.columns = ['rank', 'title', 'year']
        
        # 데이터베이스 연결
        engine = create_engine("mysql+pymysql://root:" + "1111" + "@127.0.0.1:3306/movie?charset=utf8",
                            encoding = 'utf-8')
        conn = engine.connect()
        # name 은 테이블 / con은 컨넥트 엔진 / if_exist 만약 있으면 append 추가 하라! / index는 없이
        Mtitle.to_sql(name='movie',con=engine,if_exists='append',index=False)

        
        self.textLabel2.setText("결과 : DB에 저장했습니다.")
        self.textLabel2.resize(250, 30)
        # self.label.clear() # settext("") 와 같은 기능을 함.

 



if __name__ == "__main__":
    app = QApplication(sys.argv) 
    mywindow = MyWindow()
    mywindow.show() 
    app.exec_() 

