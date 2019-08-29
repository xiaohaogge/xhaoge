# first case
# 此case 用于简单的发送请求，对于响应字段的对比；


import json
from NewWorld.CommonFunc.Base import AllBase

class Case_Verify_KeyValue_0001(AllBase):

    def __init__(self):
        AllBase.__init__(self)
        self.log.info("nima,开始case的初始化")
        self.url = 'http://dev-api.gloryholiday.com/yuetu/search'
        self.data = '''
                        {
                            "Cid": "qunarytb",
                            "TripType": "1",
                            "FromCity": "hkg",
                            "ToCity": "icn",
                            "FromDate": "20190923",
                            "RetDate": "20190921",
                            "AdultNumber": 1,
                            "ChildNumber": 0,
                            "InfantNumber":0,
                            "GodPerspective":false
                        }'''


    def TestProcess(self):
        print('这是验价的 case1 ')

    def TestResult(self):
        print("测试结果很成功，perfect！")

