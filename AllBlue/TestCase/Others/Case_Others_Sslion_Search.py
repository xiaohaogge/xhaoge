# 此case用于筛选航线；

import json
import threading
from AllBlue.TestCase.CaseBase.SearchCaseBase import CaseBase

class Case_Others_Sslion_Search(CaseBase):

    def __init__(self):
        CaseBase.__init__(self)
        self.log.info("===Case_Others_Sslion_Search,测试开始===")


    def TestProcess(self):
        th = []
        for i in range(100):
            t = threading.Thread(target=self.nima())
            print(t)
            th.append(t)
        for h in th:
            h.start()


    def TestResult(self):
        self.log.info('===Case_Others_Monitor_Deduction,测试完毕===')
        pass

    def nima(self):
        url1 = "http://test-api.gloryholiday.com/yuetu/search"
        senddata = """
                           {
                                "Cid": "meituan",
                                "TripType": "1",
                                "FromCity": "bjs",
                                "ToCity": "lax",
                                "bypassCache": true,
                                "FromDate": "20191217",
                                "RetDate":"20200108",
                                "AdultNumber": 1, 
                                "ChildNumber": 0,
                                "InfantNumber":0,
                                "Currency":"CNY",
                                "GodPerspective": false,
                                "TargetProviders":["sslion"]
                            } """

        res = self.sendRequest(url=url1, data=senddata)
        return res





