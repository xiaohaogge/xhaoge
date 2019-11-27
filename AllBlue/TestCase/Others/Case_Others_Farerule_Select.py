# 此case用于筛选航线；

import json
from AllBlue.TestCase.CaseBase.SearchCaseBase import CaseBase

class Case_Others_Farerule_Select(CaseBase):

    def __init__(self):
        CaseBase.__init__(self)
        self.log.info("===Case_Others_Monitor_Deduction,测试开始===")


    def TestProcess(self):
        url1 = "http://dev-api.gloryholiday.com/yuetu/search"
        senddata = """
                   {
                        "Cid": "ctrip",
                        "TripType": "1",
                        "FromCity": "bjs",
                        "ToCity": "lax",
                        "FromDate": "20191226",
                        "RetDate":"20200108",
                        "AdultNumber": 1, 
                        "ChildNumber": 0,
                        "InfantNumber":0,
                        "Currency":"CNY",
                        "GodPerspective": false,
                        "TargetProviders":[]
                    } """
        res = self.sendRequest(url=url1,data=senddata)
        print(type(res))
        res = json.loads(res)
        print(type(res))
        routings = res["routing"]
        # self.log.info(routings)
        listp = []
        quest = []
        final = []
        for i in routings:
            if i["rule"]["refundBeforeDep"] == 1:
                listp.append(i["data"])
            if i["rule"]["changeBeforeDep"] == 1 and i["rule"]["refundBeforeDep"] == 1:
                final.append(i["data"])
            if i["rule"]["changeBeforeDep"] == 0:
                quest.append(i["data"])


        # listp = []
        # repor = []
        # for i in routings:
        #     if i["providerName"] == "mondee":
        #         listp.append(i)
        #         if len(i["rule"]["repoRule"]["repoIds"]) == len(i["itinerary"]["segment"]):
        #             repor.append(i)

        print(len(listp), listp)
        print(len(final), final)
        print(len(quest),quest)
        self.log.info(listp)
        self.log.info(final)
        self.log.info(quest)

    def TestResult(self):
        self.log.info('===Case_Others_Monitor_Deduction,测试完毕===')
        pass






