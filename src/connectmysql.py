import pymysql
# ---------连接--------------
connect = pymysql.connect(host='localhost',   # 本地数据库
                          user='root',
                          password='gzy158',
                          db='课程设计',
                          charset='utf8') #服务器名,账户,密码，数据库名称
cur = connect.cursor()
print(cur)

# 执行的都是原生SQL语句
cur.execute("show tables")

for row in cur.fetchall():
    print(row[0])

connect.close()