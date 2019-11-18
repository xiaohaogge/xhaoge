

import random
from AllBlue.Common.Base import AllBase
from AllBlue.Common.NightKingSearchResponse import NightKingSearchRes


class CaseBase(AllBase):

    def __init__(self):
        AllBase.__init__(self)
        self.flag = False
        # 测试环境的night king请求的url，data参数；
        self.nkRequesturl = 'http://test-api.gloryholiday.com/yuetu/search'
        self.nkVerifyReqUrl = 'http://test-api.gloryholiday.com/yuetu/verify'
        self.nkOrderReqUrl = "http://test-api.gloryholiday.com/yuetu/order"
        self.nkRequestdata = '''
                    {
                            "Cid": "qunarytb",
                            "TripType": "2",
                            "FromCity": "HKG",
                            "ToCity": "LAX",
                            "FromDate": "20200223",
                            "RetDate": "20200521",
                            "AdultNumber": 1,
                            "ChildNumber": 1,
                            "InfantNumber":0,
                            "Currency":"CNY",
                            "BypassCache": true,
                            "GodPerspective":false
                    }'''
        self.nkVerifyReqData ='''
                    {       "Cid": "qunarytb",
                            "adultNum": 1,
                            "childNum": 1,
                            "infantNum":0,
                            "currency": "CNY",
                            "routing":""
                    }'''

        self.nkRequestDataDict = self.jsonToDict(self.nkRequestdata) # 将search请求参数从str转为dict；
        self.nkVerifyReqDataDict = self.jsonToDict(self.nkVerifyReqData) # 将verify请求参数从str 转换为dict；
        # 汇率的几个接口地址，测试、生产；
        self.PreProdExchangeRate = 'http://pre-prod-restful-api.gloryholiday.com/nightking/exchangeRate'
        self.ProdExchangeRate = 'http://prod-restful-api.gloryholiday.com/nightking/exchangeRate'
        self.devExchangeRate = 'http://dev-restful-api.gloryholiday.com/nightking/exchangeRate'
        self.get25Hours = 'http://dev-restful-api.gloryholiday.com/currencyservice/getCurrencyListOfLatest25Hour'
        self.getCurrency = 'http://dev-restful-api.gloryholiday.com/currencyservice/getCurrency'
        self.quotaCurrency = 'http://dev-restful-api.gloryholiday.com/marineford/currency/manualquota'
        self.getCurrencyList = 'http://dev-restful-api.gloryholiday.com/currencyservice/getCurrencyList'


    def TestProcess(self):
        pass


    def TestResult(self):
        pass

    def searchByCid(self,cid="ctrip"):
        self.nkRequestDataDict["Cid"] = cid
        sendData = self.dictToJson(self.nkRequestDataDict)
        res = self.sendRequest(url=self.nkRequesturl,data=sendData)
        return res

    def verifyByPid(self,routings,pid="mondee"):
        pidRouting = []
        for i in routings:
            if i['providerName'] == pid:
                if len(i["evictionMarks"]) == 0:
                    pidRouting.append(i)
        if len(pidRouting) == 0:
            return 0
        num = random.randint(0,len(pidRouting)-1)
        sdata = self.nkVerifyReqDataDict["routing"] = pidRouting[num]
        res = self.sendRequest(url=self.nkVerifyReqUrl,data=sdata)
        if len(res["routing"]) == 0:
            return 1
        return res

    def verify(self):
        pass





