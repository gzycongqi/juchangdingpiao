
for i in range(55):
    if(i<10):
        a = """   
        self.pushButton_0"""+str(i)+""".setStyleSheet(
            '''QPushButton{background:#42E61A;border-radius:5px;}QPushButton:hover{background:green;}''')
            """

    else:
        a = """   
        self.pushButton_"""+str(i)+""".setStyleSheet(
            '''QPushButton{background:#42E61A;border-radius:5px;}QPushButton:hover{background:green;}''')
            """
    print(a)




