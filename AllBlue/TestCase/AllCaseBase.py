

import json
from AllBlue.Source.ReadBaseConfig import BaseConfig


class CaseBase(BaseConfig):

    def __init__(self):
        BaseConfig.__init__(self)
        self.nkRequesturl = 'http://dev-api.gloryholiday.com/yuetu/search'
        data = '''
                                {
                                    "Cid": "ctrip",
                                    "TripType": "1",
                                    "FromCity": "TPE",
                                    "ToCity": "HKG",
                                    "FromDate": "20191123",
                                    "RetDate": "20191221",
                                    "AdultNumber": 1,
                                    "ChildNumber": 0,
                                    "InfantNumber":0,
                                    "Currency":"CNY",
                                    "BypassCache": true,
                                    "GodPerspective":false
                                }'''
        self.nkRequestData = json.loads(data)


    def TeseProcess(self):
        pass


    def TestResult(self):
        pass

