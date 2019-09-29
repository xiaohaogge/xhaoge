# Ctrip case
# 此case用于测试ctrip 单程和往返是否能正常verify；

import json
from AllBlue.TestCase.Verify.Ctrip.SearchResp import CtripSearchResponse
from AllBlue.TestCase.Verify.Ctrip.CtripCaseBase import CtripCase


class Case_Ctrip_Verify_0001(CtripCase):

    def __init__(self):
        CtripCase.__init__(self)
        self.log.info("===Case_Ctrip_Verify_0001,测试开始===")


    def TestProcess(self):
        self.log.info('测试ctrip单程的verify，准备参数数据；')
        sendSearch = json.dumps(self.ctripSearchData)
        self.log.info('---search 参数---：%s'%sendSearch)
        self.log.info('测试ctrip单程的verify，发送POST请求，得到search响应；')
        searchRes = self.sendRequest(method='POST',url=self.ctripSearchUrl, data=sendSearch)
        # todo 响应结果判断；
        rr = CtripSearchResponse(searchRes)
        routing = rr.getRandomRouting()
        self.ctripVerifyData['routing']['data'] = routing['data']
        self.ctripVerifyData['routing']['fromSegments'] = routing['fromSegments']
        self.ctripVerifyData['routing']['retSegments'] = routing['retSegments']
        sendVerify = json.dumps(self.ctripVerifyData)
        self.log.info('---verify 参数---：%s' % sendVerify)
        self.log.info('测试ctrip单程的verify，发送POST请求，得到verify响应；')
        res = self.sendRequest(url=self.ctripVerifyUrl,data=sendVerify)
        self.log.info(('---Verify response---:%s')%res)
        self.log.info('测试ctrip单程的verify成功；')

        self.log.info('测试ctrip往返的verify，准备参数数据；')
        self.ctripSearchData['tripType'] = '2'
        sendSearch = json.dumps(self.ctripSearchData)
        self.log.info('---search 参数---：%s' % sendSearch)
        self.log.info('测试ctrip往返的verify，发送POST请求，得到search响应；')
        searchRes = self.sendRequest(method='POST', url=self.ctripSearchUrl, data=sendSearch)
        rr = CtripSearchResponse(searchRes)
        routing = rr.getRandomRouting()
        self.ctripVerifyData['tripType'] = '2'
        self.ctripVerifyData['routing']['data'] = routing['data']
        self.ctripVerifyData['routing']['fromSegments'] = routing['fromSegments']
        self.ctripVerifyData['routing']['retSegments'] = routing['retSegments']
        sendVerify = json.dumps(self.ctripVerifyData)
        self.log.info('---verify 参数---：%s' % sendVerify)
        self.log.info('测试ctrip往返的verify，发送POST请求，得到verify响应；')
        res = self.sendRequest(url=self.ctripVerifyUrl, data=sendVerify)
        self.log.info(('---Verify response---:%s') % res)
        self.log.info('测试ctrip往返的verify成功；')
        self.flag = True


    def TestResult(self):
        self.log.info('===Case_Ctrip_Verify_0001,测试完毕===')
        if self.flag:
            self.log.info('=========Case_Ctrip_Verify_0001,测试通过')
            print("测试结果很成功，perfect！")
        else:
            self.log.error('=========Case_Ctrip_Verify_0001,测试失败')


