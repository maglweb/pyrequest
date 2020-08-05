#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/5 11:41
# @Author : Administrator
# @Software: PyCharm

import sys

sys.path.append('../db_fixture')
from db_fixture.mysql_db import DB

# 创建测试数据
datas = {
    # 发布会表数据
    'sign_event': [
        {'`' + 'id' + '`': 1, '`' + 'name' + '`': 'Lenovo', '`' + 'limit' + '`': 2000, '`' + 'status' + '`': 1,
         '`' + 'address' + '`': 'beijing',
         '`' + 'start_time' + '`': '2020-08-03 08:00:00'},
        {'`' + 'id' + '`': 2, '`' + 'name' + '`': '当前关闭状态', '`' + 'limit' + '`': 1000, '`' + 'status' + '`': 0,
         '`' + 'address' + '`': 'shangdi',
         '`' + 'start_time' + '`': '2020-08-01 11:00:00'},
        {'`' + 'id' + '`': 3, '`' + 'name' + '`': 'Huawei', '`' + 'limit' + '`': 2000, '`' + 'status' + '`': 1,
         '`' + 'address' + '`': 'beijing',
         '`' + 'start_time' + '`': '2020-07-03 08:00:00'},
        {'`' + 'id' + '`': 4, '`' + 'name' + '`': '可参加人数为0', '`' + 'limit' + '`': 0, '`' + 'status' + '`': 1,
         '`' + 'address' + '`': 'beijing',
         '`' + 'start_time' + '`': '2020-08-04 08:00:00'},
    ],

    # 嘉宾表数据
    'sign_guest': [
        {'`' + 'id' + '`': 1, '`' + 'realname' + '`': 'alen', '`' + 'phone' + '`': 13511001100,
         '`' + 'email' + '`': 'alen@mail.com', '`' + 'sign' + '`': 1,
         '`' + 'event_id' + '`': 3},
        {'`' + 'id' + '`': 2, '`' + 'realname' + '`': 'has sign', '`' + 'phone' + '`': 13511001101,
         '`' + 'email' + '`': 'sign@mail.com', '`' + 'sign' + '`': 1,
         '`' + 'event_id' + '`': 1},
        {'`' + 'id' + '`': 3, '`' + 'realname' + '`': 'tom', '`' + 'phone' + '`': 13511001102,
         '`' + 'email' + '`': 'tom@mail.com', '`' + 'sign' + '`': 1,
         '`' + 'event_id' + '`': 5},
    ],
}


# 将测试数据插入表
def init_data():
    db = DB()
    for table, data in datas.items():
        db.clear(table)
        for d in data:
            db.insert(table, d)
    db.close()


if __name__ == '__main__':
    init_data()
