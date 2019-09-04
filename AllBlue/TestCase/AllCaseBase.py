

import json
from AllBlue.CommonFunc.Base import AllBase


class CaseBase(AllBase):

    def __init__(self):
        AllBase.__init__(self)
        self.flag = False
        self.nkRequesturl = 'http://dev-api.gloryholiday.com/yuetu/search'
        data = '''
                    {
                            "Cid": "ctrip",
                            "TripType": "1",
                            "FromCity": "BJS",
                            "ToCity": "LAX",
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

        self.PreProdRate = 'http://pre-prod-restful-api.gloryholiday.com/nightking/exchangeRate'
        self.ProdRate = 'http://prod-restful-api.gloryholiday.com/nightking/exchangeRate'


    def TeseProcess(self):
        pass


    def TestResult(self):
        pass



