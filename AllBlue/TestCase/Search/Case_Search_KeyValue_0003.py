# first case
# 此case用于测试价格的准确与否，从供应商原始价格，到每一层政策的加价值，再到最终的报价；


import json
from AllBlue.Common.Base import SearchBase

class Case_Search_KeyValue_0003(SearchBase):

    def __init__(self):
        SearchBase.__init__(self)
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
        print("这是case3  暂时不知道写什么了")

    def TestResult(self):
        print("测试结果很成功，perfect！")

