import pymysql
# ---------连接--------------
def connect():
    connect = pymysql.connect(host='localhost',  # 本地数据库
                              user='root',
                              password='gzy158',
                              db='课程设计',
                              charset='utf-8')  # 服务器名,账户,密码，数据库名称
    cur = connect.cursor()
    return cur,connect