# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'log.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

from src import seat
import userwork

username=""
pas=""

def change(a):
    global success1
    success1=a
def getusername():
    return username
class Ui_Dialog(object):
    success1=0
    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(322, 657)
        #self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)




        # 登录
        self.pushButton_1 = QtWidgets.QPushButton(Dialog)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 350, 101, 32))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_1.clicked.connect(self.clickButton)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 100, 111, 51))
        self.label.setObjectName("label")


        self.user = QtWidgets.QTextEdit(Dialog)
        self.user.setGeometry(QtCore.QRect(110, 210, 171, 31))
        self.user.setObjectName("user")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 220, 101, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 290, 72, 15))
        self.label_3.setObjectName("label_3")

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(110, 280, 171, 31))
        self.lineEdit.setText("")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "请登录"))
        self.label.setText(_translate("Dialog", "用户登录"))
        self.label_2.setText(_translate("Dialog", "请输入用户名"))
        self.label_3.setText(_translate("Dialog", "密码"))

        self.pushButton_1.setText(_translate("Dialog", "登录"))

    def clickButton(self):
            global pas
            global username
            global success1
            username=self.user.toPlainText()
            print(username)

            pas=self.lineEdit.text()
            print(pas)
            key=[]
            connect = pymysql.connect(host='localhost',  # 本地数据库
                                      user='root',
                                      password='gzy158',
                                      db='课程设计',
                                      charset='utf8')  # 服务器名,账户,密码，数据库名称
            cur = connect.cursor()
            cur.execute("select * from user")
            for row in cur.fetchall():
                key.append((row[0], row[1]))
            connect.commit()
            print(key)
            if (username, pas) in key:

                self.success1=1


                seat.change(username)
                userwork.change(username)
                self.label.setText( "登录成功")
                print("ok")
            else:

                self.success1=0
                self.label.setText("登录失败")

