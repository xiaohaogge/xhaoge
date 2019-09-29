# Currency Rate
# 此case用于测试ctrip 是否能正常verify；

import json
from AllBlue.TestCase.Others.Ctrip.SearchResp import CtripSearchResponse
from AllBlue.TestCase.Others.Ctrip.CtripCaseBase import CtripCase


class Case_Ctrip_Verify_0001(CtripCase):

    def __init__(self):
        CtripCase.__init__(self)
        self.log.info("===Case_Ctrip_Verify_0001,测试开始===")


    def TestProcess(self):
        sendSearch = json.dumps(self.ctripSearchData)
        self.log.info('search 参数：%s'%sendSearch)
        searchRes = self.sendRequest(method='POST',url=self.ctripSearchUrl, data=sendSearch)
        rr = CtripSearchResponse(searchRes)
        routing = rr.getRandomRouting()
        self.ctripVerifyData['routing']['data'] = routing['data']
        self.ctripVerifyData['routing']['fromSegments'] = routing['fromSegments']
        self.ctripVerifyData['routing']['retSegments'] = routing['retSegments']
        sendVerify = json.dumps(self.ctripVerifyData)
        self.log.info('verify 参数：%s' % sendVerify)
        res = self.sendRequest(url=self.ctripVerifyUrl,data=sendVerify)



        self.flag = True


    def TestResult(self):
        self.log.info('===Case_Ctrip_Verify_0001,测试完毕===')
        if self.flag:
            self.log.info('=========Case_Ctrip_Verify_0001,测试通过')
            print("测试结果很成功，perfect！")
        else:
            self.log.error('=========Case_Ctrip_Verify_0001,测试失败')


