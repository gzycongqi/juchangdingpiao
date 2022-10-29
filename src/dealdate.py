import datetime
import pymysql
connect = pymysql.connect(host='localhost',  # 本地数据库
                              user='root',
                              password='gzy158',
                              db='课程设计',
                              charset='utf8')  # 服务器名,账户,密码，数据库名称
cur = connect.cursor()
print(cur)






def work():
    global cur
    daylist=[]
    cur.execute("select date from seat")
    for row in cur.fetchall():
        daylist.append(row[0])
    today = datetime.date.today()
    day=today
    #day = today + datetime.timedelta(days=1)
    for i in range(7):
        if day in daylist:
            pass
        else:
            for i in range(0,24,3):
                time=str(i)+":00"
                val=(day,time,"[]",54)
                cur.execute("""INSERT INTO seat (date,time,seat,count)
                       VALUES
                       ( %s, %s,%s,%s )""",val)
        day=day + datetime.timedelta(days=1)

    connect.commit()

work()