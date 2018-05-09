#coding = utf-8
import unittest
import json
import requests
from yinyu.conf import conf
class TestCase(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test001(self):
        #获取songs列表接口
        r=requests.get(url=conf.domainname + "/v1/parttime/songs",headers = conf.headers_yuliao)
        results =json.loads(r.text)
        print(results)
        self.assertEqual(r.status_code,conf.success)
    def test002(self):
        #搜索songs接口,可搜索的歌曲
        r= requests.get(url = conf.domainname + "/v1/parttime/songs?q=%e5%85%84%e5%bc%9f",headers = conf.headers_yuliao)
        results = json.loads(r.text)
        print(results)
        self.assertEqual(r.status_code,conf.success)
    def test003(self):
        #搜索songs接口，搜索不到的歌曲
        r= requests.get(url = conf.domainname + "/v1/parttime/songs?q=爱要去哪里",headers = conf.headers_yuliao)
        results = json.loads(r.text)
        print(results)
        self.assertEqual(r.status_code,conf.success)
        self.assertEqual(results["has_more"],False)
