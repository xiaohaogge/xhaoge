# 此case用于测试部分的api供应商能正常生单流程；

from AllBlue.TestCase.CaseBase.OrderCaseBase import OrderBase

class Case_Order_KeyValue_0001(OrderBase):

    def __init__(self):
        OrderBase.__init__(self)


    def TestProcess(self):
        self.log.info("选择测试平台进行搜索，对返回的不能进行verify的航线 进行筛选；")
        searchAllRouting = self.Search(cid="ctrip",TripType="1",FromCity="BJS",ToCity="SIN",FromDate="20200223",
        	RetDate="20200521",AdultNumber=1,ChildNumber=0,InfatNumber=0)
        if len(searchAllRouting["routing"]) == 0:
            self.log.info(searchAllRouting)
            return searchAllRouting
        ableVerifyRouting = self.verifyAbleRoutings(searchAllRouting["routing"])
        orderProviderList = ["mondee","myslcc","ttnet","unififi","avia","qunarf","skypker"]
        pidVerifyRouting = self.verifyByPid(routings=ableVerifyRouting,pid="mondee")
        respVerify = self.Verify(cid="ctrip",adultNum=1,childNum=0,infantNum=0,currency="CNY",routing=pidVerifyRouting)

        self.log.info("开始进行order，verify航线为：%s"%respVerify)
        print("order")
        res = self.filterOrderMan(adultNum=1,childNum=1,infantNum=1)
        self.log.info("乘客信息为：%s"%res)

    def TestResult(self):
        pass



