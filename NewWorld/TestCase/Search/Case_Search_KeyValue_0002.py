# masterCurrency case
# 此case用于测试环境简单的测试几个平台请求，以及检查本位币的取值情况；
# iwoflyCOM/wogo请求币种是HKD,本位币是HKD,其他币种请求，本位币是USD;
# 其他平台无论什么请求币种，本位币都是CNY;


import json
from NewWorld.CommonFunc.NightKingResponse import NightKingRes
from NewWorld.CommonFunc.Base import AllBase

class Case_Search_KeyValue_0002(AllBase):

    def __init__(self):
        AllBase.__init__(self)
        self.log.info("nima,开始case的初始化")
        self.url = 'http://dev-api.gloryholiday.com/yuetu/search'
        self.data = '''
                        {
                            "Cid": "ctrip",
                            "TripType": "1",
                            "FromCity": "SHA",
                            "ToCity": "HKG",
                            "FromDate": "20191023",
                            "RetDate": "20190921",
                            "AdultNumber": 1,
                            "ChildNumber": 0,
                            "InfantNumber":0,
                            "GodPerspective":false
                        }'''


    def TestProcess(self):
        print('我是case2')
        res = self.sendRequest(method='POST',url=self.url,data=self.data)
        if res:
            self.log.info('搜索成功，有返回')
            # print(res)
            cc = json.loads(res)
            print(cc)
            print(cc['baseResponse'])
            rr = NightKingRes(res)
            rr.baseResponse('cid')
            #print(res)
        else:
            print('case 2 nali')
            print(self.log.error('nothing'))


    def TestResult(self):
        print("测试结果很成功，perfect！")

