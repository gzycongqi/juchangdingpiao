for i in range(55):
    if(i<10):
        a = """   
            def clickButton_0"""+str(i)+"""(self):
                global list
                global count
                    if """+str(i)+""" in list:
                        list.remove("""+str(i)+""")
                        self.pushButton_0"""+str(i)+""".setStyleSheet('''QPushButton{background:#42E61A;border-radius:5px;}QPushButton:hover{background:green;}''')
                        count=count-1
                        print(count)
                    else:
                        self.pushButton_0"""+str(i)+""".setStyleSheet('''QPushButton{background:##FFFF00;border-radius:5px;}QPushButton:hover{background:yellow;}''')
                        list.append(""" + str(i) + """)
                        print(list)
                        count=count+1
                        print(count)"""


    else:
        a = """   
            def clickButton_""" + str(i) + """(self):
                global list
                global count
                    if """+str(i) +""" in list:
                        list.remove("""+str(i)+""")
                        self.pushButton_""" + str(i) + """.setStyleSheet('''QPushButton{background:#42E61A;border-radius:5px;}QPushButton:hover{background:green;}''')
                        count=count-1
                        print(count)
                    else:
                        self.pushButton_""" + str(i) + """.setStyleSheet('''QPushButton{background:#FFFF00;border-radius:5px;}QPushButton:hover{background:yellow;}''')
                        list.append(""" + str(i) + """)
                        print(list)
                        count=count+1
                        print(count)"""
    print(a)