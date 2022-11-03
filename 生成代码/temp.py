import pymysql
import random
listname=["玩偶之家","推销员之死","天边外","威尼斯商人","三姐妹","罗密欧与朱丽叶","仲夏夜之梦","霸王别姬","白蛇传","三打祝家庄"]
connect = pymysql.connect(host='localhost',  # 本地数据库
                          user='root',
                          password='gzy158',
                          db='课程设计',
                          charset='utf8')  # 服务器名,账户,密码，数据库名称
cur = connect.cursor()

discount=[0.6,0.8,0.9]
price=[50,100,150,200]
for i in listname:
    val=(i,random.choice(discount),random.choice(price),"0")
    cur.execute("""insert into opera(name,discount,price,count)
    values
    (%s,%s,%s,%s)
    """,val)


connect.commit()