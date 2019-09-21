# masterCurrency case
# 此case用于测试rule加价的准确与否，从原始退改，退改加价和复用退改到最后的报价rule


import json
from AllBlue.Common.NightKingSearchResponse import NightKingSearchRes
from AllBlue.TestCase.AllCaseBase import CaseBase

class Case_Search_KeyValue_0006(CaseBase):

    def __init__(self):
        CaseBase.__init__(self)
        self.log.info("===Case_Search_KeyValue_0006,测试开始===")


    def TestProcess(self):
        self.log.info('===Case_Search_KeyValue_0006,进入测试步骤！===')

        self.log.info('测试ctrip的本位币,请求币种是CNY,本位币应该是USD')
        self.Test_Master_Currency(plat='ctrip', reqC='CNY', MstCurrecy='CNY')

        self.log.info('测试iwofly的本位币,请求币种是CNY,本位币应该是USD')
        self.Test_Master_Currency(plat='iwoflyCOM', reqC='CNY', MstCurrecy='USD')

        self.log.info('测试iwofly的本位币,请求币种是USD,本位币应该是USD')
        self.Test_Master_Currency(plat='iwoflyCOM', reqC='USD', MstCurrecy='USD')

        self.log.info('测试iwofly的本位币,请求币种是HKD,本位币应该是HKD')
        self.Test_Master_Currency(plat='iwoflyCOM', reqC='HKD', MstCurrecy='HKD')

        self.log.info('测试iwoflyCN的本位币,请求币种是CNY,本位币应该是CNY')
        self.Test_Master_Currency(plat='iwoflyCN', reqC='CNY', MstCurrecy='CNY')
        self.flag = True


    def TestResult(self):
        self.log.info('===Case_Search_KeyValue_0006,测试完毕===')
        if self.flag:
            self.log.info('Case_Search_KeyValue_0006,测试通过')
            print("测试结果很成功，perfect！")
        else:
            self.log.info('【Case_Search_KeyValue_0006,测试失败】')

    # 定义公共方法，用于判断masterCuurrncy；
    def Test_Master_Currency(self,plat='ctrip',reqC='CNY',MstCurrecy='CNY'):
        self.nkRequestDataDict['Cid'] = plat
        self.nkRequestDataDict['Currency'] = reqC
        print(self.nkRequestDataDict)
        sendData = json.dumps(self.nkRequestDataDict)
        self.log.info(sendData)
        res = self.sendRequest(method='POST', url=self.nkRequesturl, data=sendData)
        if res:
            self.log.info('搜索成功，有返回')
            print('res:',res)
            case2_nk = NightKingSearchRes(res)
            ms_currency = case2_nk.routingFirstBaseInfo('masterCurrency')
            if ms_currency != MstCurrecy:
                self.log.error('%s 请求币种为 %s 时，mastercurrencty为：%s' % (plat,reqC,ms_currency))
            self.log.info('%s 请求币种为 %s 时，mastercurrencty为：%s' % (plat,reqC,ms_currency))
        else:
            self.log.error('搜索无返回，或者返回信息为null；')

