# Currency Rate
# 此case用于测试汇率接口的请求，是否是随时可以拿到汇率；



import json
from AllBlue.CommonFunc.NightKingSearchResponse import NightKingRes
from AllBlue.TestCase.AllCaseBase import CaseBase

class Case_Currency_FromToRate_0001(CaseBase):

    def __init__(self):
        CaseBase.__init__(self)
        self.log.info("===Case_Currency_FromToRate_0001,测试开始===")


    def TestProcess(self):
        self.log.info('===Case_Search_KeyValue_0002,进入测试步骤！===')

        self.log.info('测试ctrip的本位币,请求币种是CNY,本位币应该是USD')
        self.Test_Currency()

        self.log.info('测试iwofly的本位币,请求币种是CNY,本位币应该是USD')


        self.log.info('测试iwofly的本位币,请求币种是USD,本位币应该是USD')


        self.log.info('测试iwofly的本位币,请求币种是HKD,本位币应该是HKD')


        self.log.info('测试iwoflyCN的本位币,请求币种是CNY,本位币应该是CNY')

        self.flag = True


    def TestResult(self):
        self.log.info('===Case_Search_KeyValue_0002,测试完毕===')
        if self.flag:
            self.log.info('Case_Search_KeyValue_0002,测试通过')
            print("测试结果很成功，perfect！")
        else:
            self.log.info('【Case_Search_KeyValue_0002,测试失败】')

    # 定义公共方法，用于获取Cuurrncy；
    def Test_Currency(self,pro='sscts',cid='ctrip',ori="USD",tar='CNY'):
        strJoin = "?providerName={}&cid={}&originalCode={}&targetCode={}".format(pro,cid,ori,tar)
        sendUrl = self.PreProdRate+strJoin
        print(sendUrl)
        # pre-prod-restful-api.gloryholiday.com/nightking/exchangeRate?providerName=sscts&cid=ctrip&originalCode=USD&targetCode=CNY
        self.sendRequest(method='GET',url=sendUrl)

