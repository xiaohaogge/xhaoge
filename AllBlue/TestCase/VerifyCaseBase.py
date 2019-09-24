

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
        self.nkRequestdata = '''
                    {
                            "Cid": "qunarytb",
                            "TripType": "2",
                            "FromCity": "HKG",
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

        self.nkRequestDataDict = json.loads(self.nkRequestdata) # 将请求参数从str转为dict，方便修改参数；
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

    def search(self):
        res = self.sendRequest(url=self.nkRequesturl,data=self.nkRequestdata)

        pass


    def verify(self):
        pass





