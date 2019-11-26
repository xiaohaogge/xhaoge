# nothing

from AllBlue.TestCase.CaseBase.OrderCaseBase import CaseBase

class Case_Order_KeyValue_0001(CaseBase):

    def __init__(self):
        CaseBase.__init__(self)


    def TestProcess(self):
    	# 选择测试平台进行搜索，对返回的不能进行verify的航线 进行筛选；
        searchAllRouting = self.Search(cid="qunarytb",TripType="1",FromCity="BJS",ToCity="SIN",FromDate="20200223",
        	RetDate="20200521",AdultNumber=1,ChildNumber=0,InfatNumber=0)
        ableVerifyRouting = self.verifyAbleRoutings(searchAllRouting["routing"])
        pidVerifyRouting = self.verifyByPid(routings=ableVerifyRouting)
        respVerify = self.Verify(cid="qunarytb",adultNum=1,childNum=0,infantNum=0,currency="CNY",routing=pidVerifyRouting)


    def TestResult(self):
        pass



