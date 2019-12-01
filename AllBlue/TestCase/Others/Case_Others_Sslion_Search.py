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
        for i in range(10,30):
            for p in ["ANA","EST","JAL_EXP"]:
                t = threading.Thread(target=self.nima(i,p))
                t1 = threading.Thread(target=self.nimaCA(i,p))
                t2 = threading.Thread(target=self.nimanh(i, p))
                print(t)
                th.append(t)
                th.append(t1)
                th.append(t2)

        for h in th:
            h.start()


    def TestResult(self):
        self.log.info('===Case_Others_Monitor_Deduction,测试完毕===')
        pass

    def nima(self,day,pid):
        url1 = "http://dev-restful-api.gloryholiday.com/dressrosa/search"
        senddata = """
                           {
                            "yuetu_search_request": {
                                "base_request": {
                                    "cid": "TEST",
                                    "trace_id": "abcde-1234789012-ab12-TEST"
                                },
                                "trip": [
                                    {
                                        "departure_code": "OKA",
                                        "arrival_code": "OSA",
                                        "departure_date": "2020-01-%dT00:00:00.123Z"
                                    }
                                ],
                                "cabin": "E",
                                "adult_num": 1,
                                "child_num": 0,
                                "infant_num": 0,
                                "use_mock_data": false,
                                "stress_test": false
                            },
                            "tripType": "2",
                            "airline": "%s"
                        } """%(day,pid)

        print(senddata)
        try:
            self.res = self.sendRequest(url=url1, data=senddata)
        except Exception as e:
            print(e)
        print(self.res)
        return self.res

    def nimaCA(self,day,pid):
        url1 = "http://dev-restful-api.gloryholiday.com/dressrosa/search"
        senddata = """
                           {
                            "yuetu_search_request": {
                                "base_request": {
                                    "cid": "TEST",
                                    "trace_id": "abcde-1234789012-ab12-TEST"
                                },
                                "trip": [
                                    {
                                        "departure_code": "TYO",
                                        "arrival_code": "OSA",
                                        "departure_date": "2020-03-%dT00:00:00.123Z"
                                    }
                                ],
                                "cabin": "E",
                                "adult_num": 1,
                                "child_num": 0,
                                "infant_num": 0,
                                "use_mock_data": false,
                                "stress_test": false
                            },
                            "tripType": "2",
                            "airline": "%s"
                        } """%(day,pid)

        print(senddata)
        try:
            self.res = self.sendRequest(url=url1, data=senddata)
        except Exception as e:
            print(e)
        print(self.res)
        return self.res

    def nimanh(self,day,pid):
        url1 = "http://dev-restful-api.gloryholiday.com/dressrosa/search"
        senddata = """
                           {
                            "yuetu_search_request": {
                                "base_request": {
                                    "cid": "TEST",
                                    "trace_id": "abcde-1234789012-ab12-TEST"
                                },
                                "trip": [
                                    {
                                        "departure_code": "OKA",
                                        "arrival_code": "TYO",
                                        "departure_date": "2020-04-%dT00:00:00.123Z"
                                    }
                                ],
                                "cabin": "E",
                                "adult_num": 1,
                                "child_num": 0,
                                "infant_num": 0,
                                "use_mock_data": false,
                                "stress_test": false
                            },
                            "tripType": "2",
                            "airline": "%s"
                        } """%(day,pid)

        print(senddata)
        try:
            self.res = self.sendRequest(url=url1, data=senddata)
        except Exception as e:
            print(e)
        print(self.res)
        return self.res





