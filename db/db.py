import pymysql

# 此文件包含数据库相关操作


# 连接数据库，取得数据库中所有信息
def info():
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='888888',
                           db='学生数据库',
                           cursorclass=pymysql.cursors.DictCursor)
    cursor = conn.cursor()
    a = 'select * from 学生数据库.交大社团, 学生数据库.选课;'
    cursor.execute(a)
    a = cursor.fetchall()
    return a


#  查询数据库
def query(sql):
    try:
        conn = pymysql.connect(host='localhost',
                               port=3306,
                               user='root',
                               password='888888',
                               db='学生数据库',
                               cursorclass=pymysql.cursors.DictCursor)
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        return result
    except:
        return False





