#coding = utf-8
import requests
from yinyu.conf import conf
from yinyu.Interface.tools import tools
class Case():
    def case01(self):
    # 语料发送登录验证码，正确手机号
        r = requests.post(url=conf.domainname + "/v1/sms/verification_code", headers=conf.headers_yuliao,
                          data={"phone": conf.phone1})
        return r
    def case02(self):
    # 语料发送登录验证码，空手机号
        r = requests.post(url=conf.domainname + "/v1/sms/verification_code", headers=conf.headers_yuliao,
                          data={"phone": ""})
        return r
    def case03(self):
    # 语料发送登录验证码，错误手机号
        r = requests.post(url=conf.domainname + "/v1/sms/verification_code", headers=conf.headers_yuliao,
                          data={"phone": tools().random_digit()})
        return r
    def case04(self):
    # 语料登录接口，空手机号，空验证码
        r = requests.post(url=conf.domainname + "/v1/parttime/login", headers=conf.headers_yuliao,
                          data={"phone": "", "verification_code": ""})
        return r
    def case05(self):
    # 语料登录接口，正确手机号，空验证码
        r = requests.post(url=conf.domainname + "/v1/parttime/login", headers=conf.headers_yuliao,
                          data={"phone": conf.phone2, "verification_code": ""})
        return r
    def case06(self):
    # 语料登录接口，错误手机号，空验证码
        r = requests.post(url=conf.domainname + "/v1/parttime/login", headers=conf.headers_yuliao,
                          data={"phone": tools().random_digit(), "verification_code": ""})
        return r
    def case07(self):
    # 语料登录接口，正确手机号，错误验证码
        r = requests.post(url=conf.domainname + "/v1/parttime/login", headers=conf.headers_yuliao,
                          data={"phone": conf.phone1, "verification_code": tools().random_digit()})
        return r
    def case08(self):
    # 获取songs列表接口
        r = requests.get(url=conf.domainname + "/v1/parttime/songs", headers=conf.headers_yuliao)
        return r
    def case09(self):
    # 搜索songs接口,可搜索的歌曲
        r = requests.get(url=conf.domainname + "/v1/parttime/songs?q=%e5%85%84%e5%bc%9f", headers=conf.headers_yuliao)
        return r
    def case10(self):
    # 搜索songs接口，搜索不到的歌曲
        r = requests.get(url=conf.domainname + "/v1/parttime/songs?q=爱要去哪里", headers=conf.headers_yuliao)
        return r