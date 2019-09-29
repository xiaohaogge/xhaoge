# 定义ctrip search response响应类


import random
import json


class CtripSearchResponse():

    def __init__(self,res):
        resp = json.loads(res)
        self.status = resp['status']
        self.msg = resp['msg']
        self.routings = resp['routings']


    def getRandomRouting(self):
        i = random.randint(0,len(self.routings)-1)
        routing = self.routings[i]
        print('routing:type',type(routing))
        return routing

    def getData(self):
        pass

