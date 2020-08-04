#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/4 18:36
# @Author : Administrator
# @Software: PyCharm

from pymysql import connect, cursors
from pymysql.err import OperationalError
import os
import configparser as cparser


# =====读取数据库配置文件======
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\', '/')  # 用 / 替换 \\
file_path = base_dir + '/db_config.ini'

cf = cparser.ConfigParser()
cf.read(file_path)

host = cf.get('mysqlconf', 'host')
port = cf.get('mysqlconf', 'port')
db = cf.get('mysqlconf', 'db_name')
user = cf.get('mysqlconf', 'user')
passwrod = cf.get('mysqlconf', 'password')


# =====封装MySQL基本操作=====
class DB:
    def __init__(self):
        try:
            # 连接数据库
            self.conn = connect(
                host=host,
                user=user,
                passwrod=passwrod,
                db=db,
                charset='uft8mb4',
                cursorclass=cursors.DictCursor
            )
        except OperationalError as e:
            print('Mysql Error %d:%s' % (e.args[0], e.args[1]))

    # 清楚表数据
    def clear(self, table_name):
        real_sql = 'truncate table' + table_name + ';'
        with self.conn.cursor() as cursor:
            cursor.execute('SET FOREIGN_KEY_CHECKS=0;')
            cursor.execute(real_sql)
        self.conn.commit()

    # 插入表数据
    def insert(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'" + str(table_data[key]) + "'"
        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = 'insert into' + table_name + '(' + key + ') values (' + value + ')'
        with self.conn.cursor() as cursor:
            cursor.execute(real_sql)
        self.conn.commit()

    # 关闭数据库
    def close(self):
        self.conn.close()


if __name__ == '__main__':
    db = DB()
    table_name = 'sign_event'
    data = {'id': 12, 'name': 'Lenovo', 'limit': 2000, 'status': 1, 'address': 'beijing',
            'start_time': '2020-08-03 08:00:00'}
    db.clear()
    db.insert()
    db.close()
