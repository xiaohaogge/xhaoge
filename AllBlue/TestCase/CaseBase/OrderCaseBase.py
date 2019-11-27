

import random
from AllBlue.TestCase.CaseBase.AllCaseBase import CaseBase
from AllBlue.Source.OrderConfig import startReadOrder
from AllBlue.Common.NightKingSearchResponse import NightKingSearchRes


class OrderBase(CaseBase):

    def __init__(self):
        CaseBase.__init__(self)
        self.passengersList = startReadOrder() # {0:[passengers],1:[],2:[]}

          
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

    # 通过不同平台 统一发送请求
    def searchByCid(self,cid="ctrip"):
        pass

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


    # 从读取的配置文件中，随机的拿取相应的乘客类型信息；
    def filterOrderMan(self,adultNum=1,childNum=0,infantNum=0):
        orderManList = []
        # 随机的从列表中 选取相应人数的乘客类型；
        adult = random.sample(self.passengersList["0"],adultNum)
        child = random.sample(self.passengersList["1"],childNum)
        infant = random.sample(self.passengersList["2"],infantNum)
        for a in adult:
            orderManList.append(a)
        if len(child) != 0:
            for c in child:
                orderManList.append(c)
        if len(infant) != 0 :
            for i in infant:
                orderManList.append(i)
        return orderManList





