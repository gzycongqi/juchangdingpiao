import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QDialog
import PyQt5.QtWidgets


from src import seat
from src import chooseuse
from src import userlog
import managerlog

from managerlog import *
from userlog import *
import managerwork
import userwork

from chooseuse import Ui_Dialog as choose_Ui # 选择界面的库
from userlog import   Ui_Dialog as log_Ui # 登录界面的库
from seat import Ui_Dialog as seat_Ui
from src import dealdate
dealdate.work()
list=seat.list
success1=0
def changesu(a):
    global success1
    success1=a



class chooseWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.choose_ui = chooseuse.Ui_Dialog()
        self.choose_ui.setupUi(self)


class userlogWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.userlog_ui = userlog.Ui_Dialog()
        self.userlog_ui.setupUi(self)

class managerlogWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.managerlog_ui = managerlog.Ui_Dialog()
        self.managerlog_ui.setupUi(self)






class managerworkWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.managerwork_ui = managerwork.Ui_Dialog()
        self.managerwork_ui.setupUi(self)

class userworkWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.userwork_ui = userwork.Ui_Dialog()
        self.userwork_ui.setupUi(self)


class seatWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.seat_ui = seat.Ui_Dialog()
        self.seat_ui.setupUi(self)

def work():
    if getsuccess()==1:
        managerwork.show()
        managerlog.close()

def work2():

    if userlog.userlog_ui.success1==1:
        userwork.show()
        userlog.close()





app = QApplication(sys.argv)
choose = chooseWindow()
userlog = userlogWindow()
managerlog=managerlogWindow()

managerwork=managerworkWindow()
userwork=userworkWindow()
seat=seatWindow()




# 通过toolButton将两个窗体关联
managerloggo = choose.choose_ui.pushButton
managerloggo.clicked.connect(managerlog.show)
managerloggo.clicked.connect(choose.close)
userloggo = choose.choose_ui.pushButton_2
userloggo.clicked.connect(userlog.show)
userloggo.clicked.connect(choose.close)

#managerdenglu=managerlog.managerlog_ui.pushButton_1
managerdenglu=managerlog.managerlog_ui.pushButton_1
managerdenglu.clicked.connect(work)


userdenglu = userlog.userlog_ui.pushButton_1
userdenglu.clicked.connect(work2)


selectseat=userwork.userwork_ui.pushButton
selectseat.clicked.connect(seat.show)
clo1=seat.seat_ui.pushButton
clo1.clicked.connect(seat.close)

gaipiao=userwork.userwork_ui.pushButton_4
gaipiao.clicked.connect(seat.show)






# 显示
choose.show()
sys.exit(app.exec_())

#selectseat()




#selectseat()