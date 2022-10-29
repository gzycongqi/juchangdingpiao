import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from src import seat
list=seat.list
def selectseat():
    global list
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui =seat.Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    # print(list)
    sys.exit(app.exec_())



selectseat()