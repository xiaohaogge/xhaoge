'''Currency Rate
  此case用于测试nightking search 时返回的rule政策匹配涉及到的Currency-masterCurrency转换汇率是否有拿到；
'''


import json
import random
from AllBlue.TestCase.AllCaseBase import CaseBase


class Case_Currency_FromToRate_0004(CaseBase):

    def __init__(self):
        CaseBase.__init__(self)
        self.log.info("===Case_Currency_FromToRate_0004,测试开始===")


    def TestProcess(self):
        self.log.info('【Case_Currency_FromToRate_0004,进入测试步骤！】')

        self.log.info('【1.测试从night king中返回获取不同的provider(以平台qunarytb为例)】')
        res = self.sendRequest(method='POST',url=self.nkRequesturl,data=self.nkRequestdata)
        print(res)
        self.checkNkStatus(res)
        self.target_providers = self.Test_TargetProviders(res)
        self.log.info('target_provider:%s'%self.target_providers)

        self.log.info('【2.根据不同的供应商,rule当中涉及币种可能会不一样；】')
        for tar in self.target_providers:
            self.Test_RuleChange(provider=tar,routings=self.routingslist)

        self.log.info('【3.测试从night king中返回获取provider币种(以iwoflyCOM为例)】')
        self.nkRequestDataDict['Cid'] = 'iwoflyCOM'
        # #print(self.nkRequestDataDict)
        # sendData = json.dumps(self.nkRequestDataDict)
        # res = self.sendRequest(method='POST', url=self.nkRequesturl, data=sendData)
        # self.Test_TargetProviders(res)
        # self.log.info('【4.根据不同的供应商,不同的币种，进行检查是否拿到到本位币转换汇率】')
        # self.log.info('target_provider:%s' % self.target_providers)
        # for tar in self.target_providers:
        #     self.Test_Provider_Master(cid='', provider=tar, routings=self.routingslist, reqCurrency='CNY')

        self.flag = True


    def TestResult(self):
        self.log.info('===Case_Currency_FromToRate_0004,测试完毕===')
        if self.flag:
            self.log.info('=========Case_Currency_FromToRate_0004,测试通过')
            print("测试结果很成功，perfect！")
        else:
            self.log.info('=========Case_Currency_FromToRate_0004,测试失败')


    def Test_RuleChange(self,cid='',provider='',routings=''):
        pro_Routing_List = []
        for d in routings:
            if d['providerName'] == provider:
                pro_Routing_List.append(d)
        num = len(pro_Routing_List)
        if num == 0:
            return self.log.info('该供应商没有航线报出:%s'%provider)
        '''随机抽取其中一条航线，进行测试计算；'''
        testnum = random.randint(0, num - 1)
        self.log.info('%s总航线数目：%s,选择的是：%s' % (provider,num, testnum))
        test_Routing = pro_Routing_List[testnum]
        Rule_List_Currency = []
        Rule_All = test_Routing['rule']
        origin_Rule = Rule_All['originRuleFee']['currency']
        Rule_List_Currency.append(origin_Rule) if origin_Rule is not None else ''
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

        self.log.info('【2.1.check %s 的rule中是否有获取到Currency】' % provider)
        if len(Rule_List_Currency)!=0:
            for i in Rule_List_Currency:
                if i != mas_Currency:
                    result = self.getRoutingCurrencyConvs(conversions=cuyconversions,fromC=i,toC=mas_Currency)
                    if result:
                        self.log.info('政策中from %s to %s 有获取到汇率'%(i,mas_Currency))
                    else:
                        self.log.error('政策中from %s to %s 没有获取到汇率'%(i,mas_Currency))
