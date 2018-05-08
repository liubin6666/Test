#coding =utf-8
import random
#随机生成手机号
class tools():

    def tel(self):
        for _ in range(1):
           phone=('13' + str(random.randrange(1,10))+ ''.join( str(random.choice(range(10))) for _ in range(8) ))
        return phone