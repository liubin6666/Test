#coding = utf-8
import unittest
import json
from yinyu.Interface.case import Case
from yinyu.conf import conf
class TestCase(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test001(self):
        #获取songs列表接口
        Case().case08()
        results =json.loads(Case().case08().text)
        print(results)
        self.assertEqual(Case().case08().status_code,conf.success)
    def test002(self):
        # 搜索songs接口,可搜索的歌曲
        Case().case09()
        results = json.loads(Case().case09().text)
        print(results)
        self.assertEqual(Case().case09().status_code,conf.success)
    def test003(self):
        # 搜索songs接口，搜索不到的歌曲
        Case().case10()
        results = json.loads(Case().case10().text)
        print(results)
        self.assertEqual(Case().case10().status_code,conf.success)
        self.assertEqual(results["has_more"],False)
