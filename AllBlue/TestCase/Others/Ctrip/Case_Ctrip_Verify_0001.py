# Currency Rate
# 此case用于并发进行监控余额扣款测试；
import json

from AllBlue.TestCase.Others.Ctrip.SearchResp import CtripSearchResponse
from AllBlue.TestCase.Others.Ctrip.CtripCaseBase import CtripCase

class Case_Ctrip_Verify_0001(CtripCase):

    def __init__(self):
        CtripCase.__init__(self)
        self.log.info("===Case_Ctrip_Verify_0001,测试开始===")


    def TestProcess(self):
        res = self.sendRequest(method='POST',url=self.ctripSearchUrl, data=self.ctripSearchData)
        print(res)
        print(type(res))
        rr = CtripSearchResponse(res)



        self.flag = True

    def TestResult(self):
        self.log.info('===Case_Ctrip_Verify_0001,测试完毕===')
        if self.flag:
            self.log.info('=========Case_Ctrip_Verify_0001,测试通过')
            print("测试结果很成功，perfect！")
        else:
            self.log.error('=========Case_Ctrip_Verify_0001,测试失败')


