# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lib/managerwork.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import *
import pymysql
from PyQt5.QtGui import QStandardItemModel, QStandardItem


class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(827, 775)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 20, 91, 51))
        self.label1 = QtWidgets.QLabel(Dialog)
        self.label1.setGeometry(QtCore.QRect(150, 50, 91, 51))
        self.label.setObjectName("label")
        self.label1.setObjectName("label1")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(120, 110, 151, 41))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 120, 72, 15))
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(120, 180, 151, 41))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_3.setGeometry(QtCore.QRect(120, 250, 151, 41))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 200, 72, 15))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 270, 72, 15))
        self.label_4.setObjectName("label_4")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 390, 121, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.clickbutton)

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 340, 121, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.clickbutton2)


        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 440, 121, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.clickbutton3)


        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(510, 40, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")





        connect = pymysql.connect(host='localhost',  # ???????????????
                                  user='root',
                                  password='gzy158',
                                  db='????????????',
                                  charset='utf8')  # ????????????,??????,????????????????????????
        cur = connect.cursor()
        user = []
        cur.execute("select * from seachorder")



        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(440, 100, 256, 221))
        self.tableView.setObjectName("tableView")
        self.model = QStandardItemModel(0, 3)
        self.model.setHorizontalHeaderLabels(['?????????', '??????', '??????','??????'])
        self.tableView.setModel(self.model)

        for row in cur.fetchall():
            user.append((row[0], row[1], row[2], row[3]))
            self.model.appendRow([QStandardItem(row[0]),QStandardItem(row[1]),QStandardItem(row[2]),QStandardItem(row[3])])
        connect.commit()



        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(490, 350, 161, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.clickbutton5)



        self.tableView_2 = QtWidgets.QTableView(Dialog)
        self.tableView_2.setGeometry(QtCore.QRect(440, 420, 256, 192))
        self.tableView_2.setObjectName("tableView_2")
        self.model2 = QStandardItemModel(0, 2)
        self.model2.setHorizontalHeaderLabels(['??????', '?????????'])
        self.tableView_2.setModel(self.model2)



        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "?????????"))
        self.label.setText(_translate("Dialog", "??????????????????"))
        self.label1.setText(_translate("Dialog", "??????"))
        self.label_2.setText(_translate("Dialog", "?????????"))
        self.label_3.setText(_translate("Dialog", "??????"))
        self.label_4.setText(_translate("Dialog", "????????????"))
        self.pushButton.setText(_translate("Dialog", "???????????????"))
        self.pushButton_2.setText(_translate("Dialog", "??????????????????"))
        self.pushButton_3.setText(_translate("Dialog", "??????????????????"))
        self.pushButton_4.setText(_translate("Dialog", "????????????"))
        self.pushButton_5.setText(_translate("Dialog", "??????????????????"))

    #?????????
    def clickbutton2(self):
        connect = pymysql.connect(host='localhost',  # ???????????????
                                  user='root',
                                  password='gzy158',
                                  db='????????????',
                                  charset='utf8')  # ????????????,??????,????????????????????????
        cur = connect.cursor()
        username=self.textEdit.toPlainText()
        user=[]
        cur.execute("select * from user")
        for row in cur.fetchall():
            user.append((row[0], row[1],row[2],row[3]))
        connect.commit()
        for i in user:
            if i[0]==username:
                self.textEdit_2.setText(i[1])
                self.textEdit_3.setText(i[2])
                self.label1.setText("????????????")

    #?????????
    def clickbutton(self):
        connect = pymysql.connect(host='localhost',  # ???????????????
                                  user='root',
                                  password='gzy158',
                                  db='????????????',
                                  charset='utf8')  # ????????????,??????,????????????????????????
        cur = connect.cursor()
        username=self.textEdit.toPlainText()
        user=[]
        cur.execute("select * from user")
        for row in cur.fetchall():
            user.append((row[0], row[1],row[2],row[3]))
        connect.commit()
        a=0
        for i in user:
            if i[0]==username:
                self.label1.setText('??????????????????')
                a=1
        if a==0:
            val=(self.textEdit.toPlainText(),self.textEdit_2.toPlainText(),self.textEdit_3.toPlainText())
            cur.execute("""INSERT INTO user (username,password,vip,ticket)
                                   VALUES
                                   ( %s, %s,%s ,"[]")""", val)
            self.label1.setText("????????????")
            connect.commit()



    #?????????
    def clickbutton3(self):
        connect = pymysql.connect(host='localhost',  # ???????????????
                                  user='root',
                                  password='gzy158',
                                  db='????????????',
                                  charset='utf8')  # ????????????,??????,????????????????????????
        cur = connect.cursor()
        username=self.textEdit.toPlainText()
        password=self.textEdit_2.toPlainText()
        vip=self.textEdit_3.toPlainText()
        val=(username,password,vip,username)
        cur.execute("""
        update user
        set username=%s,password=%s,vip=%s
        where username=%s        
        """,val)
        connect.commit()
        self.label1.setText("????????????")

    def clickbutton5(self):
        connect = pymysql.connect(host='localhost',  # ???????????????
                                  user='root',
                                  password='gzy158',
                                  db='????????????',
                                  charset='utf8')  # ????????????,??????,????????????????????????
        cur = connect.cursor()



        cur.execute("""select * from opera""")

        for row in cur.fetchall():
            name=row[0]
            price=float(row[1])*int(row[2])*int(row[3])
            self.model2.appendRow([QStandardItem(str(name)),QStandardItem(str(price))])




        connect.commit()

