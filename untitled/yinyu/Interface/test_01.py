#coding = utf-8
import unittest
import requests
import json
from yinyu.conf import conf
from yinyu.Interface.tools import tools



class Testcase(unittest.TestCase):

    def setUp(self):
        pass
    def test001(self):
        #发送验证码
        data = {"phone":conf.phone1}
        r=requests.post(url=conf.domainname + "/v1/sms/verification_code",data=data)
        results = json.loads(r.text)
        print(results)
        self.assertEqual(r.status_code,conf.success)
    def test002(self):
        #发送验证码，空手机号
        data={"phone":""}
        r=requests.post(url=conf.domainname + "/v1/sms/verification_code",data=data)
        results = json.loads(r.text)
        print(results)
        self.assertEqual(r.status_code,conf.improper_requests)
        self.assertEqual(results["errcode"],conf.error)
    def test003(self):
        # 手机号注册（正确方式）
        data = {"phone":tools().tel()}
        r=requests.post(url=conf.domainname + "/v1/parttime/register",data=data)
        results = json.loads(r.text)
        print(results)
        self.assertEqual(r.status_code,201)
        self.assertEqual(results["data"]["status"],1)
    def test004(self):
        #手机号注册（已注册过的手机号）
        data = {"phone":conf.phone1}
        r= requests.post(url=conf.domainname + "/v1/parttime/register",data=data)
        print(r.text)
        self.assertEqual(r.status_code,500)
    def test005(self):
        #手机号注册接口（不合法手机号）
        data = {"phone":"123"}
        r= requests.post(url=conf.domainname + "/v1/parttime/register",data=data)
        results = json.loads(r.text)
        print(results)
        self.assertEqual(r.status_code,conf.improper_requests)
        self.assertEqual(results["errcode"],conf.error)
    def test006(self):
        #手机号注册接口（手机号传空）
        data = {"phone":""}
        r=requests.post(url=conf.domainname + "/v1/parttime/register",data=data)
        results = json.loads(r.text)
        print(results)
        self.assertEqual(r.status_code, conf.improper_requests)
        self.assertEqual(results["errcode"], conf.error)

    def tearDown(self):
        pass

