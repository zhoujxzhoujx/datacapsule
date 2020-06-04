# coding = utf-8

import pymysql
from DBUtils.PooledDB import PooledDB


# 创建数据量连接池
def create_pool():
    pool = PooledDB(pymysql, 5,
                    host='localhost',
                    user='root',
                    password='123456',
                    database='airspace',
                    charset='utf8',
                    cursorclass=pymysql.cursors.DictCursor)
    db = pool.connection()
    return db
