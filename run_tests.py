#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/4 18:30
# @Author : Administrator
# @Software: PyCharm

import time, sys

sys.path.append('./interface')
sys.path.append('./db_fixture')
import unittest
from db_fixture import test_data
import HTMLTestRunner


# 指定测试用例为当前文件夹下的interface目录
test_dir = './interface'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')

if __name__ == '__main__':
    test_data.init_data()  # 初始化接口测试数据

    now = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = './report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title='Guest Manage System Interface Test Report',
        description='Implementation Example with:'
    )
    runner.run(discover)
    fp.close()
