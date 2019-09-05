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

        self.log.info('测试ctrip的sscts,从USD到CNY的汇率是否拿到')
        self.Test_Currency(pro='sscts', cid='ctrip', ori="USD", tar='CNY')

        self.log.info('测试ctrip的sscts,从TWD到CNY的汇率是否拿到')
        self.Test_Currency(pro='sscts', cid='ctrip', ori="TWD", tar='CNY')

        self.log.info('测试ctrip的ttnet,从EUR到CNY的汇率是否拿到')
        self.Test_Currency(pro='ttnet', cid='ctrip', ori="EUR", tar='CNY')

        self.log.info('测试ctrip的ssgmt,从THB到CNY的汇率是否拿到')
        self.Test_Currency(pro='ssgmt', cid='ctrip', ori="THB", tar='CNY')

        self.log.info('测试ctrip的ssxm,从HKD到CNY的汇率是否拿到')
        self.Test_Currency(pro='ssgmt', cid='ctrip', ori="HKD", tar='CNY')

        self.log.info('测试ctrip的belair,从INR到CNY的汇率是否拿到')
        self.Test_Currency(pro='belair', cid='ctrip', ori="INR", tar='CNY')

        self.log.info('测试qunarytb的avia,从RUB到CNY的汇率是否拿到')
        self.Test_Currency(pro='avia', cid='qunarytb', ori="RUB", tar='CNY')

        self.log.info('测试ctrip的via,从SGD到CNY的汇率是否拿到')
        self.Test_Currency(pro='via', cid='ctrip', ori="SGD", tar='CNY')

        self.log.info('测试ctrip的ssact,从AUD到CNY的汇率是否拿到')
        self.Test_Currency(pro='ssact', cid='ctrip', ori="AUD", tar='CNY')

        self.log.info('测试ctrip的ssjdc,从CAD到CNY的汇率是否拿到')
        self.Test_Currency(pro='ssjdc', cid='ctrip', ori="CAD", tar='CNY')

        self.log.info('测试ctrip的sscts,从VND到CNY的汇率是否拿到')
        self.Test_Currency(pro='sscts', cid='ctrip', ori="VND", tar='CNY')

        self.flag = True


    def TestResult(self):
        self.log.info('Case_Currency_FromToRate_0001,测试完毕===')
        if self.flag:
            self.log.info('Case_Currency_FromToRate_0001,测试通过')
            print("测试结果很成功，perfect！")
        else:
            self.log.info('【Case_Currency_FromToRate_0001,测试失败】')

    # 定义公共方法，用于获取Cuurrncy；
    def Test_Currency(self,pro='sscts',cid='ctrip',ori="USD",tar='CNY'):
        strJoin = "?providerName={}&cid={}&originalCode={}&targetCode={}".format(pro,cid,ori,tar)
        sendUrl = self.PreProdRate+strJoin
        # print(sendUrl)
        # pre-prod-restful-api.gloryholiday.com/nightking/exchangeRate?providerName=sscts&cid=ctrip&originalCode=USD&targetCode=CNY
        resjson = self.sendRequest(method='GET',url=sendUrl)
        resdict = json.loads(resjson)
        try:
            if resdict['msg'] != "success":
                self.log.error('获取汇率%s,请检查；' % resdict['msg'])
        except Exception as e:
            self.log.error('获取汇率%s,报错：%s'%(resdict['msg'],e))
        self.log.info('from:%s to:%s rate:%s'%(ori,tar,resdict['exchange_rate']['exchange_rate']))
        print('from:%s to:%s rate:%s'%(ori,tar,resdict['exchange_rate']['exchange_rate']))



