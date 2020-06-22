 # 
import sys # main을 사용할 수 있게 함.
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self): # self는 class 안에 있는 것들만 작업 - class 만들 때 init 을 가장먼저 꼭 써줘야.
        super().__init__() # 자기 위의 클라스  - 여기서 상속을 받아와 실행
        self.setupUI() # setup UI를 실행하라
    
    # Window Widget
    def setupUI(self): # 화면에 띄울 그림들을 여기서 다 작성해 주어야 함.
        # Window Title
        self.setWindowTitle("샘플")

        # Button
        btn1 = QPushButton("Click me!", self) # 버튼은 위치지정 필요.
        btn1.move(50,40) # 버튼 위치 
        btn1.clicked.connect(self.btn1_clicked) # btn1 클릭시 btn1_clicked 함수를 실행하라

    # Button Event
    def btn1_clicked(self):
        QMessageBox.about(self, "메세지", "Clicked! \n 클릭했음") # 메세지 박스 타이틀 , 내용 지정
        QMessageBox.size(10)



if __name__ == "__main__":
    app = QApplication(sys.argv) # 프레임워크를 사용하겠다고 정의하는 부분.
    mywindow = MyWindow() # 클래스이름을 지정해 주는 것이다. - 클래스를 만들어 줘야함.
    mywindow.show() # 화면에 표시.
    app.exec_() # 실행.