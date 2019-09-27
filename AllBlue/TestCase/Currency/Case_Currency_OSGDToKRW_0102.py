# Currency Rate
# VND-CNY 指定rate:0.00030600;
# 此case用于测试汇率VND-CNY取值范围，以及基本参数；


import json
from AllBlue.TestCase.CaseBase.SearchCaseBase import CaseBase

class Case_Currency_SGDToKRW_0102(CaseBase):

    def __init__(self):
        # super(Case_Currency_VNDtoCNY_0101,self).__init__()
        CaseBase.__init__(self)
        self.log.info("===Case_Currency_SGDToKRW_0102,测试开始===")


    def TestProcess(self):
        self.log.info('【Case_Currency_SGDToKRW_0102,进入测试步骤！】')

        self.log.info('1.测试getCurrency 从VND到CNY的汇率是否拿到;')
        res = self.sendRequest(url=self.get25Hours)
        print(res)
        print(type(res))
        resp = json.loads(res)
        print(type(resp))
        source = resp['source_currency_list']
        for reu in source:
            if reu['source'] == 'REUTERS':
                l = reu['source']['currencies']
                for i in l:
                    if i['original_code'] == 'SGD' and i['target_code']=='KRW':
                        print('from SGD to KRW rate:%s')%i['original_number']

        self.flag = True


    def TestResult(self):
        self.log.info('===Case_Currency_SGDToKRW_0102,测试完毕===')
        if self.flag:
            self.log.info('=========Case_Currency_SGDToKRW_0102,测试通过')
            print("测试结果很成功，perfect！")
        else:
            self.log.info('=========Case_Currency_SGDToKRW_0102,测试失败')





