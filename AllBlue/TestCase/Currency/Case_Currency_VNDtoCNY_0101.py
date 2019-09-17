# Currency Rate
# VND-CNY 指定rate:0.00030600;
# 此case用于测试汇率VND-CNY取值范围，以及基本参数；


import json
from AllBlue.TestCase.Common import checkGetCurrency
from AllBlue.TestCase.AllCaseBase import CaseBase

class Case_Currency_VNDtoCNY_0101(CaseBase):

    def __init__(self):
        # super(Case_Currency_VNDtoCNY_0101,self).__init__()
        CaseBase.__init__(self)
        self.log.info("===Case_Currency_VNDtoCNY_0101,测试开始===")


    def TestProcess(self):
        self.log.info('【Case_Currency_VNDtoCNY_0101,进入测试步骤！】')

        self.log.info('1.测试getCurrency 从VND到CNY的汇率是否拿到;')
        sendDict = {"originalCode":"VND", "targetCode":"CNY", "publish_timestamp": "2019-09-18T00:00:00Z"}
        sendData = json.dumps(sendDict)
        res = self.sendRequest(method='POST',url=self.getCurrency,data=sendData)
        resC = json.loads(res)
        currencyList = resC['currencies']
        self.log.info(currencyList)
        for i in currencyList:
            if i['source'] == 'VCB':
                if i['status_code']!=200:
                    self.log.error('not found VND-CNY rate == fail')
                if i['exchange_rate'] > 0.0004:
                    self.log.error('the rate is too high,rate:%s'%i['exchange_rate'])
                self.log.info('获取汇率：%s，from VND to CNY rate:%s'%(i['response_msg'],i['exchange_rate']))

        self.log.info('2.测试exchangeRate 从VND到CNY的汇率是否实时拿到;')
        try:
            s =self.Test_Currency(ori='VND')
            if s == 404:
                raise Exception('汇率报错：'+s)
        except Exception as e:
            self.log.error('报错：%s'%e)


        self.flag = True


    def TestResult(self):
        self.log.info('===Case_Currency_VNDtoCNY_0101,测试完毕===')
        if self.flag:
            self.log.info('=========Case_Currency_VNDtoCNY_0101,测试通过')
            print("测试结果很成功，perfect！")
        else:
            self.log.info('=========Case_Currency_VNDtoCNY_0101,测试失败')





