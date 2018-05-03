#coding = utf-8
import unittest
import requests
import json
from yinyu.conf.conf import improper_requests
from yinyu.conf.conf import error
from yinyu.conf.conf import success
from yinyu.conf.conf import phone1
from yinyu.Interface.tools import phone
from yinyu.conf.conf import domainname

class Testcase(unittest.TestCase):
    def setUp(self):
        pass
    def test001(self):
        #发送验证码
        data = {"phone":phone1}
        r=requests.post(url=domainname + "/v1/sms/verification_code",data=data)
        results = json.loads(r.text)
        print(results)
        self.assertEqual(r.status_code,success)
    def test002(self):
        #发送验证码，空手机号
        data={"phone":""}
        r=requests.post(url=domainname + "/v1/sms/verification_code",data=data)
        results = json.loads(r.text)
        print(results)
        self.assertEqual(r.status_code,improper_requests)
        self.assertEqual(results["errcode"],error)
    def test003(self):
        # 手机号注册（正确方式）
        data = {"phone":phone}
        r=requests.post(url=domainname + "/v1/parttime/register",data=data)
        results = json.loads(r.text)
        print(results)
        self.assertEqual(r.status_code,201)
        self.assertEqual(results["data"]["status"],1)
    def test004(self):
        #手机号注册（已注册过的手机号）
        data = {"phone":phone1}
        r= requests.post(url=domainname + "/v1/parttime/register",data=data)
        print(r.text)
        self.assertEqual(r.status_code,500)
    def test005(self):
        #手机号注册接口（不合法手机号）
        data = {"phone":"123"}
        r= requests.post(url=domainname + "/v1/parttime/register",data=data)
        results = json.loads(r.text)
        print(results)
        self.assertEqual(r.status_code,improper_requests)
        self.assertEqual(results["errcode"],error)
    def test006(self):
        #手机号注册接口（手机号传空）
        data = {"phone":""}
        r=requests.post(url=domainname + "/v1/parttime/register",data=data)
        results = json.loads(r.text)
        print(results)
        self.assertEqual(r.status_code, improper_requests)
        self.assertEqual(results["errcode"], error)


    def tearDown(self):
        pass

