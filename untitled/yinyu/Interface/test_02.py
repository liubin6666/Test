# coding = utf-8
import requests
import unittest
import json
from yinyu.conf import conf

class TestCase(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def testcase001(self):
        # Discovery接口
        r = requests.get(url=conf.domainname + "/v1/discovery")
        results = json.loads(r.text)
        print(results)
        self.assertEqual(r.status_code, conf.success)
    def testcase002(self):
        # 获取大厅信息接口
        r = requests.get(url=conf.domainname + "/v1/lobby", headers=conf.headers)
        results = json.loads(r.text)
        print(results)
        self.assertEqual(results["data"]["responder_channel"]["user_count"], 100)
    def testcase003(self):
        # 获取songs列表
        r = requests.get(url=conf.domainname + "/v1/parttime/songs", headers=conf.headers)
        results = json.loads(r.text)
        print(results)
        self.assertEqual(r.status_code, conf.success)
    def testcase004(self):
        #获取今日最佳歌词
        r= requests.get(url=conf.domainname + "/v1/hottest/lyrics",headers=conf.headers)
        results = json.loads(r.text)
        print(results)
        self.assertEqual(results["data"]["sub_lyrics"],"你是我的眼，带我领略四季的变幻")
