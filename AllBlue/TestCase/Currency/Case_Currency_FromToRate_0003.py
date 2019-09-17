'''Currency Rate
  此case用于测试nightking search 时返回的所有政策匹配涉及到的Currency-masterCurrency转换汇率是否有拿到；
'''


import json
from AllBlue.TestCase.AllCaseBase import CaseBase
from AllBlue.CommonFunc.NightKingSearchResponse import NightKingRes

class Case_Currency_FromToRate_0003(CaseBase):

    def __init__(self):
        CaseBase.__init__(self)
        self.log.info("===Case_Currency_FromToRate_0003,测试开始===")


    def TestProcess(self):
        self.log.info('【Case_Currency_FromToRate_0003,进入测试步骤！】')

        self.log.info('【1.测试从night king中返回获取provider币种(以qunarytb为例)】')
        res = self.sendRequest(method='POST',url=self.nkRequesturl,data=self.nkRequestdata)
        self.checkNkStatus(res)
        self.target_providers = self.Test_TargetProviders(res)
        self.log.info('target_provider:%s'%self.target_providers)

        self.log.info('【2.根据不同的供应商,不同的币种，进行检查是否拿到到本位币转换汇率】')
        for tar in self.target_providers:
            self.Test_Provider_Master(cid='',provider=tar,routings=self.routingslist,reqCurrency='CNY')

        self.log.info('【3.测试从night king中返回获取provider币种(以iwoflyCOM为例)】')
        self.nkRequestDataDict['Cid'] = 'iwoflyCOM'
        #print(self.nkRequestDataDict)
        sendData = json.dumps(self.nkRequestDataDict)
        res = self.sendRequest(method='POST', url=self.nkRequesturl, data=sendData)
        self.Test_TargetProviders(res)
        self.log.info('【4.根据不同的供应商,不同的币种，进行检查是否拿到到本位币转换汇率】')
        self.log.info('target_provider:%s' % self.target_providers)
        for tar in self.target_providers:
            self.Test_Provider_Master(cid='', provider=tar, routings=self.routingslist, reqCurrency='CNY')

        self.flag = True


    def TestResult(self):
        self.log.info('===Case_Currency_FromToRate_0003,测试完毕===')
        if self.flag:
            self.log.info('=========Case_Currency_FromToRate_0003,测试通过')
            print("测试结果很成功，perfect！")
        else:
            self.log.info('=========Case_Currency_FromToRate_0003,测试失败')

    def Test_TargetProviders(self,res):
        case_c2 = NightKingRes(res)
        self.routingslist = case_c2.nkRouting
        for i in case_c2.nkTraceSpans:
            try:
                pro = i['tags']['nk-wb-final-target-providers']
                providers = pro.split(',')
                return providers
            except Exception:
                pass















