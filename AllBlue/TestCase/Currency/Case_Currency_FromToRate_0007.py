'''Currency Rate
  此case用于测试；
'''

import json
import random
from AllBlue.TestCase.CaseBase.CommonFunc import CheckListOnly
from AllBlue.TestCase.CaseBase.SearchCaseBase import CaseBase


class Case_Currency_FromToRate_0007(CaseBase):

    def __init__(self):
        CaseBase.__init__(self)
        self.log.info("===Case_Currency_FromToRate_0007,测试开始===")


    def TestProcess(self):
        self.log.info('【Case_Currency_FromToRate_0007,进入测试步骤！】')

        self.log.info('【1.测试从night king中返回获取不同的provider(以平台qunarytb为例)】')
        self.log.info('qunarytb请求参数：%s' % self.nkRequestdata)
        res = self.sendRequest(method='POST',url=self.nkRequesturl,data=self.nkRequestdata)
        self.checkNkStatus(res)
        self.target_providers = self.Test_TargetProviders(res=res)
        self.log.info('target_provider:%s'%self.target_providers)

        self.log.info('【1.1.根据不同的供应商,rule当中涉及币种可能会不一样；】')
        for tar in self.target_providers:
            self.Test_RuleChange(provider=tar,routings=self.routingslist)

        self.log.info('【2.测试从night king中返回获取provider币种(以iwoflyCOM,请求为CNY为例)】')
        self.nkRequestDataDict['Cid'] = 'iwoflyCOM'
        self.sendData = json.dumps(self.nkRequestDataDict)
        self.log.info('iwofly请求参数：%s' % self.sendData)
        res = self.sendRequest(method='POST', url=self.nkRequesturl, data=self.sendData)
        self.checkNkStatus(res)
        self.target_providers = self.Test_TargetProviders(res=res)
        self.log.info('target_provider:%s' % self.target_providers)
        self.log.info('【2.1.根据不同的供应商,rule当中涉及币种可能会不一样；】')
        for tar in self.target_providers:
            self.Test_RuleChange(provider=tar,routings=self.routingslist)

        self.log.info('【3.测试从night king中返回获取provider币种(以iwoflyCOM,请求为USD为例)】')
        self.nkRequestDataDict['Currency'] = 'USD'
        self.sendData = json.dumps(self.nkRequestDataDict)
        self.log.info('iwofly请求参数：%s' % self.sendData)
        res = self.sendRequest(method='POST', url=self.nkRequesturl, data=self.sendData)
        self.checkNkStatus(res)
        self.target_providers = self.Test_TargetProviders(res=res)
        self.log.info('target_provider:%s' % self.target_providers)
        self.log.info('【3.1.根据不同的供应商,rule当中涉及币种可能会不一样；】')
        for tar in self.target_providers:
            self.Test_RuleChange(provider=tar, routings=self.routingslist)

        self.log.info('【4.测试从night king中返回获取provider币种(以iwoflyCOM,请求为HKD为例)】')
        self.nkRequestDataDict['Currency'] = 'HKD'
        self.sendData = json.dumps(self.nkRequestDataDict)
        self.log.info('iwofly请求参数：%s' % self.sendData)
        res = self.sendRequest(method='POST', url=self.nkRequesturl, data=self.sendData)
        self.checkNkStatus(res)
        self.target_providers = self.Test_TargetProviders(res=res)
        self.log.info('target_provider:%s' % self.target_providers)
        self.log.info('【4.1.根据不同的供应商,rule当中涉及币种可能会不一样；】')
        for tar in self.target_providers:
            self.Test_RuleChange(provider=tar, routings=self.routingslist)

        self.flag = True


    def TestResult(self):
        self.log.info('===Case_Currency_FromToRate_0007,测试完毕===')
        if self.flag:
            self.log.info('=========Case_Currency_FromToRate_0007,测试通过')
            print("测试结果很成功，perfect！")
        else:
            self.log.error('=========Case_Currency_FromToRate_0007,测试失败')


    def Test_RuleChange(self,provider='',routings=''):
        pro_Routing_List = []
        for d in routings:
            if d['providerName'] == provider:
                pro_Routing_List.append(d)
        num = len(pro_Routing_List)
        if num == 0:
            return self.log.info('该供应商没有航线报出:%s'%provider)
        '''随机抽取其中一条航线，进行测试计算；'''
        testnum = random.randint(0, num - 1)
        self.log.info('%s总航线数目：%s,选择的是：%s进行测试；' % (provider,num, testnum))
        test_Routing = pro_Routing_List[testnum]
        Rule_List_Currency = []
        Rule_All = test_Routing['rule']
        origin_Rule = Rule_All['originRuleFee']['currency']
        Rule_List_Currency.append(origin_Rule)
        try:
            manual_Rule = Rule_All['manualFareRule']['currency']
        except Exception:
            manual_Rule = 0
        Rule_List_Currency.append(manual_Rule) if manual_Rule !=0 else ''

        try:
            Rule_By_Policy = Rule_All['changeDetail']['ruleChangeByPolicy']['currency']
        except Exception:
            Rule_By_Policy = 0
        Rule_List_Currency.append(Rule_By_Policy) if Rule_By_Policy != 0 else ''
        mas_Currency = test_Routing['masterCurrency']
        out_Currency = test_Routing['currency']
        cuyconversions = test_Routing['currencyConversions']

        self.log.info('【check[%s]的rule中是否有获取到Currency】' % provider)
        if len(Rule_List_Currency)!=0:
            Rule_List_Currency = CheckListOnly(dataList=Rule_List_Currency)
            for i in Rule_List_Currency:
                if i != mas_Currency:
                    result,rate = self.getRoutingCurrencyConvs(conversions=cuyconversions,fromC=i,toC=mas_Currency)
                    if result:
                        self.log.info('政策中from %s to %s 有获取到汇率:%s'%(i,mas_Currency,rate))
                    else:
                        self.log.error('政策中from %s to %s 没有获取到汇率,错误：%s'%(i,mas_Currency,test_Routing))
