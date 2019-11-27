

import json
import random
from AllBlue.Common.Base import AllBase
from AllBlue.Common.NightKingSearchResponse import NightKingSearchRes


class CaseBase(AllBase):

    def __init__(self):
        AllBase.__init__(self)
        self.flag = False
        # 测试环境的night king请求的url，data参数；
        self.nkRequesturl = 'http://dev-api.gloryholiday.com/yuetu/search'
        self.nkVerifyReqUrl = 'http://dev-api.gloryholiday.com/yuetu/verify'
        self.nkOrderReqUrl = "http://dev-api.gloryholiday.com/yuetu/order"
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
                    {       "cid": "qunarytb",
                            "adultNum": 1,
                            "childNum": 1,
                            "infantNum":0,
                            "currency": "CNY",
                            "routing":""
                    }'''
        self.nkOrderReqData = {"cid": "qunarytb",
                                "contact": {"email":"jun_6245@hotmail.com",
                                                "mobile":"60122540349",
                                                "name":"jun"},
                                "locale": 1,
                                "referredTraceId":0,
                                "passengers": [],
                                "routing":""}
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


