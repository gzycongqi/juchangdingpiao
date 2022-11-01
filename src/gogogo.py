import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QDialog
import PyQt5.QtWidgets


from src import seat
from src import chooseuse
from src import userlog
import managerlog

import managerwork
import userwork
from chooseuse import Ui_Dialog as choose_Ui # 选择界面的库
from userlog import   Ui_Dialog as log_Ui # 登录界面的库
from seat import Ui_Dialog as seat_Ui
from src import dealdate
dealdate.work()
list=seat.list




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





if __name__ == '__main__':
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



    managerjinru=managerlog.managerlog_ui.pushButton
    managerjinru.clicked.connect(managerwork.show)
    managerjinru.clicked.connect(managerlog.close)

    userjinru = userlog.userlog_ui.pushButton
    userjinru.clicked.connect(userwork.show)
    userjinru.clicked.connect(userlog.close)

    selectseat=userwork.userwork_ui.pushButton
    selectseat.clicked.connect(seat.show)
    clo1=seat.seat_ui.pushButton
    clo1.clicked.connect(seat.close)






    # 显示
    choose.show()
    sys.exit(app.exec_())

#selectseat()




#selectseat()