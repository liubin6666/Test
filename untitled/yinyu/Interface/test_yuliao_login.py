#coding = utf-8
import unittest
import json
from yinyu.conf import conf
from yinyu.Interface.case import Case
class TestCase(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test001(self):
        #语料发送登录验证码，正确手机号
        Case().case01()
        results = json.loads(Case().case01().text)
        print(results)
        self.assertEqual(Case().case01().status_code,conf.success)
    def test002(self):
        #语料发送登录验证码，空手机号
        Case().case02()
        results = json.loads(Case().case02().text)
        print(results)
        self.assertEqual(Case().case02().status_code,conf.improper_requests)
        self.assertEqual(results["errcode"],conf.error)
    def test003(self):
        #语料发送登录验证码，错误手机号
        Case().case03()
        results = json.loads(Case().case03().text)
        print(results)
        self.assertEqual(Case().case03().status_code,conf.improper_requests)
        self.assertEqual(results["errcode"],conf.error)
    def test004(self):
        #语料登录接口，空手机号，空验证码
        Case().case04()
        results = json.loads(Case().case04().text)
        print(results)
        self.assertEqual(Case().case04().status_code,conf.improper_requests)
        self.assertEqual(results["errcode"],conf.error)
    def test005(self):
        #语料登录接口，正确手机号，空验证码
        Case().case05()
        results = json.loads(Case().case05().text)
        print(results)
        self.assertEqual(Case().case05().status_code, conf.improper_requests)
        self.assertEqual(results["errcode"],conf.error)
    def test006(self):
        #语料登录接口，错误手机号，空验证码
        Case().case06()
        results = json.loads(Case().case06().text)
        print(results)
        self.assertEqual(Case().case06().status_code,conf.improper_requests)
        self.assertEqual(results["errcode"],conf.error)
    def test007(self):
        #语料登录接口，正确手机号，错误验证码
        Case().case07()
        results = json.loads(Case().case07().text)
        print(results)
        self.assertEqual(Case().case07().status_code,401)
        self.assertEqual(results["errcode"],10201)