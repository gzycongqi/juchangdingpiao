for i in range(55):
    if(i<10):
        a = """   
        if """+str(i)+ """ in list: 
            self.pushButton_0"""+str(i)+""".setStyleSheet('''QPushButton{background:#FF0000;border-radius:5px;}QPushButton:hover{background:red;}''')
        else:
            self.pushButton_0"""+str(i)+""".clicked.connect(self.clickButton_0"""+str(i)+""")
            """

    else:
        a = """   
        if """+str(i)+ """ in list: 
            self.pushButton_"""+str(i)+""".setStyleSheet('''QPushButton{background:#FF0000;border-radius:5px;}QPushButton:hover{background:red;}''')
        else:
            self.pushButton_"""+str(i)+""".clicked.connect(self.clickButton_"""+str(i)+""")
            """
    print(a)