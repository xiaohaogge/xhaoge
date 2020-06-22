#!/usr/bin/python
 # -*- coding: utf-8 -*-
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

    def Search(self,cid="qunarytb",TripType="1",FromCity="BJS",ToCity="LAX",FromDate="20200223",RetDate="20200521",
                    AdultNumber=1,ChildNumber=0,InfatNumber=0):
        self.nkRequestDataDict["cid"] = cid
        self.nkRequestDataDict["TripType"] = TripType
        self.nkRequestDataDict["FromCity"] = FromCity
        self.nkRequestDataDict["ToCity"] = ToCity
        self.nkRequestDataDict["FromDate"] = FromDate
        self.nkRequestDataDict["RetDate"] = RetDate
        self.nkRequestDataDict["AdultNumber"] = AdultNumber
        self.nkRequestDataDict["ChildNumber"] = ChildNumber
        self.nkRequestDataDict["InfatNumber"] = InfatNumber
        self.log.info("nightking search request： ",self.nkRequestDataDict)
        sendD = self.dictToJson(self.nkRequestDataDict)
        result1 = self.sendRequest(url=self.nkRequesturl, data=sendD)
        result = self.jsonToDict(result1)
        return result

    def Verify(self,cid="",adultNum=1,childNum=0,infantNum=0,currency="CNY",routing=[]):
        self.nkVerifyReqDataDict["cid"] = cid
        self.nkVerifyReqDataDict["adultNum"] = adultNum
        self.nkVerifyReqDataDict["childNum"] = childNum
        self.nkVerifyReqDataDict["infantNum"] = infantNum
        self.nkVerifyReqDataDict["currency"] = currency
        self.nkVerifyReqDataDict["routing"] = routing
        self.log.info("nightking verify request： ",self.nkVerifyReqDataDict)
        sendD = self.dictToJson(self.nkVerifyReqDataDict)
        res = self.sendRequest(url=self.nkVerifyReqUrl,data=sendD)
        return res

    def Order(self,cid="qunarytb",locale=1,referredTraceId=0,routing="",passengers=[]):
        self.nkOrderReqData["cid"] = cid
        self.nkOrderReqData["locale"] = locale
        self.nkOrderReqData["referredTraceId"] = referredTraceId
        self.nkOrderReqData["routing"] = routing
        self.nkOrderReqData["passengers"] = passengers
        sendD = self.dictToJson(self.nkOrderReqData)
        resp = self.sendRequest(url=self.nkOrderReqUrl,data=sendD)
        return resp

    # 从search 返回的航线中，根据供应商不同，选择一条航线；
    def verifyByPid(self,routings,priceType=1,pid="mondee"):
        # priceType = 1 表示默认选择最低价；
        pidRouting = []
        for i in routings:
            if i['providerName'] == pid:
                if len(i["evictionMarks"]) == 0:
                    pidRouting.append(i)
        if len(pidRouting) == 0:
            return 0
        if priceType == 1:
           routing = pidRouting[0]
        else:
            num = random.randint(0,len(pidRouting)-1)
            routing = pidRouting[num]
            print("num",num)
            self.log.info("providerName:"+pid+" verify routing: "+routing[num])
        return routing

    # 将search 的routing结果筛选出可以进行verify的航线；
    def verifyAbleRoutings(self,res):
        routings = []
        # if not isinstance(res,dict):
        #     res = self.jsonToDict(res)
        #     print("res",type(res))
        # res = res["routing"]
        print("res",type(res))
        for i in res:
            if len(i["evictionMarks"]) != 0 :
                routings.append(i)
        return routings

