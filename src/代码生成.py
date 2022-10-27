for i in range(55):
    if(i<10):
        a = """   
            def clickButton_0"""+str(i)+"""(self):
                global list
                    if """+str(i)+""" in list:
                        list.remove("""+str(i)+""")
                        self.pushButton_0"""+str(i)+""".setStyleSheet('''QPushButton{background:#42E61A;border-radius:5px;}QPushButton:hover{background:green;}''')
                    else:
                        self.pushButton_0"""+str(i)+""".setStyleSheet('''QPushButton{background:#FF0000;border-radius:5px;}QPushButton:hover{background:red;}''')
                        list.append(""" + str(i) + """)
                        print(list)"""

    else:
        a = """   
            def clickButton_""" + str(i) + """(self):
                global list
                    if """+str(i) +""" in list:
                        list.remove("""+str(i)+""")
                        self.pushButton_""" + str(i) + """.setStyleSheet('''QPushButton{background:#42E61A;border-radius:5px;}QPushButton:hover{background:green;}''')
                    else:
                        self.pushButton_""" + str(i) + """.setStyleSheet('''QPushButton{background:#FF0000;border-radius:5px;}QPushButton:hover{background:red;}''')
                        list.append(""" + str(i) + """)
                        print(list)"""
    print(a)