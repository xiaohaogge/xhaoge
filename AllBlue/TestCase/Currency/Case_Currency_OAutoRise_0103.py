'''Currency Rate
   此case用于测试汇率自动升汇的简单玩法；
'''

import json
from AllBlue.TestCase.CaseBase.CommonFunc import GetTimeCurrency
from AllBlue.TestCase.CaseBase.SearchCaseBase import SearchBase

class Case_Currency_OAutoRise_0103(SearchBase):

    def __init__(self):
        SearchBase.__init__(self)
        self.log.info("===Case_Currency_OAutoRise_0103,测试开始===")


    def TestProcess(self):
        self.log.info('【Case_Currency_OAutoRise_0103,进入测试步骤！】')

        self.log.info('1.拿到汇率政策，确认其内容;')
        # todo 暂不实现；
        reqC = {"pro":"sscts","cid":"ctrip","from":"USD","to":"CNY","displayNumber":"XXX"}
        self.Test_AuToRise(**reqC)



    def TestResult(self):
        self.log.info('===Case_Currency_OAutoRise_0103,测试完毕===')
        if self.flag:
            self.log.info('=========Case_Currency_OAutoRise_0103,测试通过')
            print("测试结果很成功，perfect！")
        else:
            self.log.error('=========Case_Currency_OAutoRise_0103,测试失败')


    def Test_AuToRise(self,method=1,targetS='BOC',persentage=0.001,auto=True,**d):
        '''定义整体逻辑实时汇率，method=1，汇率为系统获取，method=2，汇率为人工录入；
        '''
        strJoin = "?providerName={}&cid={}&originalCode={}&targetCode={}".format(d['pro'], d['cid'], d['from'],d['to'])
        sendUrl = self.devExchangeRate + strJoin
        res = self.sendRequest(url=sendUrl,method='GET')
        self.log.info("返回的汇率信息：%s" % res)
        # 将返回的信息从字符串变为字典；
        resDict = json.loads(res)
        # todo check 是否有汇率返回；
        if resDict['exchange_rate']['source'] == targetS:
            return '原始和参考汇率源一致'
        if method == 2:
            pass
        if method == 1:
            pass


    def get_CountAfter(self,nowC,oriC,percentage):
        '''定义计算方式，result=（现市场汇率-原指定汇率）*升汇百分比+原指定汇率'''
        if isinstance(nowC,float) and isinstance(oriC,float) and isinstance(percentage,float):
            result = (nowC-oriC)*percentage + oriC
            return result
        return '参数有误，请检查！'







