'''Currency Rate
  此case用于测试nightking search 时返回的所有政策匹配涉及到的Currency-masterCurrency转换汇率是否有拿到；
'''


import json
import random
from AllBlue.TestCase.AllCaseBase import CaseBase


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

        self.log.info('【1.1.根据不同的供应商,不同的币种，进行检查是否拿到到本位币转换汇率】')
        for tar in self.target_providers:
            self.Test_PolicyChange(provider=tar,routings=self.routingslist)

        self.log.info('【2.测试从night king中返回获取provider币种(以iwoflyCOM 请求币种是CNY为例)】')
        self.nkRequestDataDict['Cid'] = 'iwoflyCOM'
        self.nkRequestDataDict['Currency'] = 'CNY'
        sendData = json.dumps(self.nkRequestDataDict)
        resCOM = self.sendRequest(method='POST', url=self.nkRequesturl, data=sendData)
        self.target_providers = self.Test_TargetProviders(resCOM)
        self.log.info('【2.1.根据不同的供应商,不同的币种，进行检查是否拿到到本位币转换汇率】')
        self.log.info('target_provider:%s' % self.target_providers)
        for tar in self.target_providers:
            self.Test_Provider_Master(provider=tar, routings=self.routingslist)

        self.log.info('【3.测试从night king中返回获取provider币种(以iwoflyCOM 请求币种是HKD为例)】')
        self.nkRequestDataDict['Currency'] = 'HKD'
        sendData = json.dumps(self.nkRequestDataDict)
        resCOM2 = self.sendRequest(method='POST', url=self.nkRequesturl, data=sendData)
        self.target_providers = self.Test_TargetProviders(resCOM2)
        self.log.info('【2.1.根据不同的供应商,不同的币种，进行检查是否拿到到本位币转换汇率】')
        self.log.info('target_provider:%s' % self.target_providers)
        for tar in self.target_providers:
            self.Test_Provider_Master(provider=tar, routings=self.routingslist)

        self.log.info('【4.测试从night king中返回获取provider币种(以iwoflyCN 请求币种是HKD为例)】')
        self.nkRequestDataDict['Cid'] = 'iwoflyCN'
        self.nkRequestDataDict['Currency'] = 'HKD'
        sendData = json.dumps(self.nkRequestDataDict)
        resCN = self.sendRequest(method='POST', url=self.nkRequesturl, data=sendData)
        self.target_providers = self.Test_TargetProviders(resCN)
        self.log.info('【4.1.根据不同的供应商,不同的币种，进行检查是否拿到到本位币转换汇率】')
        self.log.info('target_provider:%s' % self.target_providers)
        for tar in self.target_providers:
            self.Test_Provider_Master(provider=tar, routings=self.routingslist)


        self.flag = True


    def TestResult(self):
        self.log.info('===Case_Currency_FromToRate_0003,测试完毕===')
        if self.flag:
            self.log.info('=========Case_Currency_FromToRate_0003,测试通过')
            print("测试结果很成功，perfect！")
        else:
            self.log.info('=========Case_Currency_FromToRate_0003,测试失败')


    def Test_PolicyChange(self,cid='',provider='',routings=''):
        pro_Routing_List = []
        for d in routings:
            if d['providerName'] == provider:
                pro_Routing_List.append(d)
        num = len(pro_Routing_List)
        if num == 0:
            return self.log.info('该供应商没有航线报出:%s'%provider)
        '''随机抽取其中一条航线，进行测试计算；'''
        testnum = random.randint(0, num - 1)
        self.log.info('总航线数目：%s,选择的是：%s' % (num, testnum))
        test_Routing = pro_Routing_List[testnum]
        pro_Currency = test_Routing['providerCurrency']
        mas_Currency = test_Routing['masterCurrency']
        out_Currency = test_Routing['currency']
        cuyconversions = test_Routing['currencyConversions']
        policy_Price_Changes = test_Routing['policyPriceChanges']
        self.log.info('【2.1.check %s是否有获取到policyPriceChanges】' % provider)
        if len(policy_Price_Changes)!=0:
            cnylist = self.Test_GetPolicyCurrecy(masterC=mas_Currency,policy=policy_Price_Changes)
            for i in cnylist:
                if i != mas_Currency:
                    self.getRoutingCurrencyConvs(conversions=cuyconversions,fromC=i,toC=mas_Currency)




    def Test_GetPolicyCurrecy(self,masterC='CNY',policy=''):
        po_Currency_List = []
        for c in policy:
            if c['adultChange']['totalChange']['currency']!=masterC:
                return '本位币需要check,masterCurrency:%s'%masterC
            try:
                addC = c['adultChange']['absChange']['currency']
                po_Currency_List.append(addC)
                if c['policyType']=='TICKET_FEE' or c['policyType']=='PLATFORM':
                    '''顺便check一下 婴儿加价'''
                    if not c.has_key("infantChange"):
                        self.log.error('%s政策中不存在婴儿计算'%c['policyType'])
            except Exception:
                pass
        return po_Currency_List


















