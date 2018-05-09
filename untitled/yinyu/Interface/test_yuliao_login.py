#coding = utf-8
import unittest
import requests
import json
from yinyu.conf import conf
from yinyu.Interface.tools import tools
class TestCase(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test001(self):
        #语料发送登录验证码，正确手机号
        data = {"phone":conf.phone1}
        r= requests.post(url = conf.domainname + "/v1/sms/verification_code",headers=conf.headers_yuliao,data=data)
        results = json.loads(r.text)
        print(results)
        self.assertEqual(r.status_code,conf.success)
    def test002(self):
        #语料发送登录验证码，空手机号
        r= requests.post(url =conf.domainname + "/v1/sms/verification_code",headers=conf.headers_yuliao,data ={"phone":""})
        results = json.loads(r.text)
        print(results)
        self.assertEqual(r.status_code,conf.improper_requests)
        self.assertEqual(results["errcode"],conf.error)
    def test003(self):
        #语料发送登录验证码，错误手机号
        data = {"phone":tools().random_digit()}
        r= requests.post(url= conf.domainname + "/v1/sms/verification_code",headers=conf.headers_yuliao,data= data)
        results = json.loads(r.text)
        print(results)
        self.assertEqual(r.status_code,conf.improper_requests)
        self.assertEqual(results["errcode"],conf.error)
    def test004(self):
        #语料登录接口，空手机号，空验证码
        data = {"phone":"","verification_code":""}
        r= requests.post(url= conf.domainname + "/v1/parttime/login",headers=conf.headers_yuliao,data= data)
        results = json.loads(r.text)
        print(results)
        self.assertEqual(r.status_code,conf.improper_requests)
        self.assertEqual(results["errcode"],conf.error)
    def test005(self):
        #语料登录接口，正确手机号，空验证码
        r = requests.post(url=conf.domainname + "/v1/parttime/login", headers=conf.headers_yuliao,
                          data={"phone": conf.phone2, "verification_code": ""})
        results = json.loads(r.text)
        print(results)
        self.assertEqual(r.status_code, conf.improper_requests)
        self.assertEqual(results["errcode"],conf.error)
    def test006(self):
        #语料登录接口，错误手机号，空验证码
        r = requests.post(url=conf.domainname + "/v1/parttime/login",headers = conf.headers_yuliao,
                          data = {"phone":tools().random_digit(),"verification_code":""})
        results = json.loads(r.text)
        print(results)
        self.assertEqual(r.status_code,conf.improper_requests)
        self.assertEqual(results["errcode"],conf.error)
    def test007(self):
        #语料登录接口，正确手机号，错误验证码
        r= requests.post(url=conf.domainname + "/v1/parttime/login",headers = conf.headers_yuliao,
                         data = {"phone":conf.phone1,"verification_code":tools().random_digit()})
        results = json.loads(r.text)
        print(results)
        self.assertEqual(r.status_code,401)
        self.assertEqual(results["errcode"],10201)