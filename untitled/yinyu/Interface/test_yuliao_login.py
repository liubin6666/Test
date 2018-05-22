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
        self.assertEqual(Case().case01().status_code,conf.success)
    def test002(self):
        #语料发送登录验证码，空手机号
        self.assertEqual(Case().case02().status_code,conf.improper_requests)
        self.assertEqual(Case().case02().json()["errcode"],conf.error)
    def test003(self):
        #语料发送登录验证码，错误手机号
        self.assertEqual(Case().case03().status_code,conf.improper_requests)
        self.assertEqual(Case().case03().json()["errcode"],conf.error)
    def test004(self):
        self.assertEqual(Case().case04().status_code,conf.improper_requests)
        self.assertEqual(Case().case04().json()["errcode"],conf.error)
    def test005(self):
        #语料登录接口，正确手机号，空验证码
        self.assertEqual(Case().case05().status_code, conf.improper_requests)
        self.assertEqual(Case().case05().json()["errcode"],conf.error)
    def test006(self):
        #语料登录接口，错误手机号，空验证码
        self.assertEqual(Case().case06().status_code,conf.improper_requests)
        self.assertEqual(Case().case06().json()["errcode"],conf.error)
    def test007(self):
        #语料登录接口，正确手机号，错误验证码
        self.assertEqual(Case().case07().status_code,401)
        self.assertEqual(Case().case07().json()["errcode"],10201)