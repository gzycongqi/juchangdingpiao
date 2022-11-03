import datetime
import pymysql
import random
def connect():
    connect = pymysql.connect(host='localhost',  # 本地数据库
                              user='root',
                              password='gzy158',
                              db='课程设计',
                              charset='utf8')  # 服务器名,账户,密码，数据库名称
    cur = connect.cursor()
    return cur,connect
cur,connect=connect()


def work():
    global cur
    daylist=[]
    cur.execute("select date from seat")
    for row in cur.fetchall():
        daylist.append(row[0])

    today = datetime.date.today()
    listname=["玩偶之家","推销员之死","天边外","威尼斯商人","三姐妹","罗密欧与朱丽叶","仲夏夜之梦","霸王别姬","白蛇传","三打祝家庄"]
    day=today

    for i in range(7):
        if str(day) not in daylist:
            for i in range(0,24,3):
                time=str(i)+":00"
                val=(day,time,"[]",54,listname[random.randint(0,9)])
                cur.execute("""INSERT INTO seat (date,time,seat,count,name)
                       VALUES
                       ( %s, %s,%s,%s,%s )""",val)
        day=day + datetime.timedelta(days=1)
    connect.commit()

work()