import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QDialog
import PyQt5.QtWidgets


from src import seat
from src import chooseuse
from src import userlog
import managerlog
from chooseuse import Ui_Dialog as choose_Ui # 选择界面的库
from userlog import   Ui_Dialog as log_Ui # 登录界面的库
from seat import Ui_Dialog as seat_Ui
from src import dealdate
dealdate.work()
list=seat.list

def selectseat():
    global list
    seat.list=list
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui =chooseuse.Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    # print(list)
    sys.exit(app.exec_())


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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    choose = chooseWindow()
    userlog = userlogWindow()
    managerlog=managerlogWindow()
    # 通过toolButton将两个窗体关联
    choosego = choose.choose_ui.pushButton
    choosego.clicked.connect(managerlog.show)
    choosego.clicked.connect(choose.close)
    userloggo = choose.choose_ui.pushButton_2
    userloggo.clicked.connect(userlog.show)
    userloggo.clicked.connect(choose.close)
    managertijiao=managerlog.managerlog_ui.pushButton
    managertijiao.clicked.connect(managerlog.close)

    # 显示
    choose.show()
    sys.exit(app.exec_())

#selectseat()




#selectseat()