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
        self.assertEqual(Case().case08().status_code,conf.success)
    def test002(self):
        # 搜索songs接口,可搜索的歌曲
        self.assertEqual(Case().case09().status_code,conf.success)
    def test003(self):
        # 搜索songs接口，搜索不到的歌曲
        self.assertEqual(Case().case10().status_code,conf.success)
        self.assertEqual(Case().case10().json()["has_more"],False)
