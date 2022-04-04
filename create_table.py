import sqlite3

# 1.创建数据库链接
# 2.创建数据库
conn = sqlite3.connect('sql.db') # 相对路径
# 3.创建游标
cursor = conn.cursor()
# 4.创建表
cursor.execute('create table Ranking(id integer primary key autoincrement,name text,score integer,timestamp integer)')
# timestamp 时间戳
# 5.关闭游标
cursor.close()
# 6.关闭数据库链接
conn.close()