#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/5 14:15
# @Author : Administrator
# @Software: PyCharm

import requests
import unittest
import os,sys
from db_fixture import test_data
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
class AddEventTest(unittest.TestCase):
    '''添加发布会'''
    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/api/add_event'

    def tearDown(self):
        print(self.result)

    def test_add_event_all_null(self):
        '''所有哦参数为空'''
        playroad = {'eid':'','':'','limit':'','address':'','start_time':''}
        r = requests.post(self.base_url,data=playroad)
        self.result = r.json()
        self.assertEqual(self.result['status'],10021)
        self.assertEqual(self.result['message','parameter error'])

