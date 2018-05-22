#coding =utf-8
import random
import requests
import json
from yinyu.conf import conf

class tools():

    def tel(self):
        # 随机生成手机号
        for _ in range(1):
           phone=('13' + str(random.randrange(1,10))+ ''.join( str(random.choice(range(10))) for _ in range(8) ))

           return phone
    def random_digit(self):
        #随机生成错误手机号
        for i in range(1):
            random_phone1= ( str(random.randrange(1,10))+ ''.join( str(random.choice(range(10)))for i in range(8) ) )
            return random_phone1



