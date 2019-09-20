# first case
# 此case 用于简单的发送请求，对于响应字段的对比；


import json
from AllBlue.Common.Base import AllBase
from AllBlue.Common.NightKingSearchResponse import NightKingSearchRes

class Case_Search_Test_0001(AllBase):

    def __init__(self):
        AllBase.__init__(self)
        self.log.info("nima,开始case的初始化")
        self.url = 'http://dev-api.gloryholiday.com/yuetu/search'
        self.data = ''' {
                          "Cid": "ctrip",
                            "TripType": "2",
                            "FromCity": "bjs",
                            "ToCity": "cts",
                            "FromDate": "20191211",
                            "RetDate": "20200109",
                            "AdultNumber": 1,
                            "ChildNumber": 0,
                            "InfantNumber":0,
                            "GodPerspective": false,
                            "Currency": "CNY"
                        }'''
        self.result1 = []


    def TestProcess(self):
        self.log.info("这是Case_Search_Test_0001")
        resp = self.sendRequest(method='POST',url=self.url,data=self.data)
        print(resp)
        rr = NightKingSearchRes(resp)
        self.FindFlight(rr.nkRouting)
        print(self.result1)
        cccc = []
        for xxxx in self.result1:
            for xx in xxxx:
                ruleR2 = xx['rule']['originRuleFee']['refundBeforeFee']
                ruleC2 = xx['rule']['originRuleFee']['changeBeforeFee']
                try:
                    for xxx in xxxx[1:]:
                        ruleR3 = xxx['rule']['originRuleFee']['refundBeforeFee']
                        ruleC3 = xxx['rule']['originRuleFee']['changeBeforeFee']
                        if ruleR2!=ruleR3 or ruleC2!=ruleC3:
                            cccc.append([xx['data'][73:-2],xxx['data'][73:-2]])
                except Exception:
                    pass

        print(cccc)
        self.log.info(cccc)


    def TestResult(self):
        self.log.info("测试结果很成功，perfect")


    def FindFlight(self,num):
        for i in num:
            listr = []
            fli = i['data'][73:-2]
            for x in num:
                cc = x['data'][73:-2]
                if fli == cc:
                    listr.append(x)
                    self.result1.append(listr)













