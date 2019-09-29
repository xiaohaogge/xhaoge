

import json
import random
from AllBlue.TestCase.CaseBase.AllCaseBase import CaseBase
from AllBlue.Common.NightKingSearchResponse import NightKingSearchRes


class CtripCase(CaseBase):

    def __init__(self):
        CaseBase.__init__(self)
        self.ctripSearchUrl = 'http://test-api.gloryholiday.com/ctrip/search'
        self.ctripSearchData = {"cid":"ctrip","tripType":"1","adultNumber":1,"childNumber":0,"infantNumber":0,"fromCity":"BJS","toCity":"SIN","fromDate":"20191103","retDate":"20191214","createTime":0,"waitTime":0}
        self.ctripVerifyUrl = 'http://test-api.gloryholiday.com/ctrip/verify'
        self.ctripVerifyData = {"cid":"ctrip","tripType":"1","adultNumber":1,"childNumber":0,"infantNumber":0, "referenceId":"023282f6878d4c66", "requesttype":"1", "routing":{}}


    def TestProcess(self):
        pass


    def TestResult(self):
        pass

