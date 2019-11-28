'''Currency Rate
  此case用于测试nightking search 时返回的供应商原始价格，经过政策最后报出去的价格，是否计算无误；
'''
import json
import random
from AllBlue.TestCase.CaseBase.SearchCaseBase import SearchBase


class Case_Currency_FromToRate_0005(SearchBase):

    def __init__(self):
        SearchBase.__init__(self)
        self.log.info("===Case_Currency_FromToRate_0005,测试开始===")


    def TestProcess(self):
        self.log.info('【Case_Currency_FromToRate_0005,进入测试步骤！】')

        self.log.info('【1.测试从night king中返回获取不同的provider(以平台qunarytb为例)】')
        self.log.info('qunarytb请求参数：%s' % self.nkRequestdata)
        res = self.sendRequest(method='POST',url=self.nkRequesturl,data=self.nkRequestdata)
        self.checkNkStatus(res)
        self.target_providers = self.Test_TargetProviders(res=res)
        self.log.info('target_provider:%s'%self.target_providers)

        self.log.info('【1.1.根据不同的供应商,来进行不同的原始-对外报价计算；】')
        for tar in self.target_providers:
            self.Test_CountPrice(provider=tar,routings=self.routingslist)

        self.log.info('【2.测试从night king中返回获取provider币种(以iwoflyCOM,请求为CNY为例)】')
        self.nkRequestDataDict['Cid'] = 'iwoflyCOM'
        self.sendData = json.dumps(self.nkRequestDataDict)
        self.log.info('iwofly请求参数：%s' % self.sendData)
        res = self.sendRequest(method='POST', url=self.nkRequesturl, data=self.sendData)
        self.checkNkStatus(res)
        self.target_providers = self.Test_TargetProviders(res=res)
        self.log.info('target_provider:%s' % self.target_providers)
        self.log.info('【2.1.根据不同的供应商,来进行不同的原始-对外报价计算；】')
        for tar in self.target_providers:
            self.Test_CountPrice(provider=tar,routings=self.routingslist)

        self.log.info('【3.测试从night king中返回获取provider币种(以iwoflyCOM,请求为USD为例)】')
        self.nkRequestDataDict['Currency'] = 'USD'
        self.sendData = json.dumps(self.nkRequestDataDict)
        self.log.info('iwofly请求参数：%s' % self.sendData)
        res = self.sendRequest(method='POST', url=self.nkRequesturl, data=self.sendData)
        self.checkNkStatus(res)
        self.target_providers = self.Test_TargetProviders(res=res)
        self.log.info('target_provider:%s' % self.target_providers)
        self.log.info('【3.1.根据不同的供应商,来进行不同的原始-对外报价计算；】')
        for tar in self.target_providers:
            self.Test_CountPrice(provider=tar, routings=self.routingslist)

        self.log.info('【4.测试从night king中返回获取provider币种(以iwoflyCOM,请求为HKD为例)】')
        self.nkRequestDataDict['Currency'] = 'HKD'
        self.sendData = json.dumps(self.nkRequestDataDict)
        self.log.info('iwofly请求参数：%s' % self.sendData)
        res = self.sendRequest(method='POST', url=self.nkRequesturl, data=self.sendData)
        self.checkNkStatus(res)
        self.target_providers = self.Test_TargetProviders(res=res)
        self.log.info('target_provider:%s' % self.target_providers)
        self.log.info('【4.1.根据不同的供应商,来进行不同的原始-对外报价计算；】')
        for tar in self.target_providers:
            self.Test_CountPrice(provider=tar, routings=self.routingslist)

        self.flag = True


    def TestResult(self):
        self.log.info('===Case_Currency_FromToRate_0005,测试完毕===')
        if self.flag:
            self.log.info('=========Case_Currency_FromToRate_0005,测试通过')
            print("Case_Currency_FromToRate_0005测试结果很成功，perfect！")
        else:
            self.log.error('=========Case_Currency_FromToRate_0005,测试失败')
            print("Case_Currency_FromToRate_0005测试结果很失败，so bad！")


    def Test_CountPrice(self,provider='',routings=''):
        pro_Routing_List = []
        for d in routings:
            if d['providerName'] == provider:
                pro_Routing_List.append(d)
        num = len(pro_Routing_List)
        if num == 0:
            return self.log.info('该供应商没有航线报出:%s'%provider)
        '''随机抽取其中一条航线，进行测试计算；'''
        testnum = random.randint(0, num-1)
        self.log.info('%s总航线数目:%s,选择的是第:%s条航线进行测试；' % (provider,num, testnum))
        testRouting = pro_Routing_List[testnum]
        self.log.info('先获取供应商原始价格，再去拿到每个政策中的加价值；')
        oriAult_Price = testRouting['oriAdultPrice']
        oriAdult_Tax = testRouting['oriAdultTax']
        oriChild_Price = testRouting['oriChildPrice']
        oriChild_Tax = testRouting['oriChildPrice']
        mas_Currency = testRouting['masterCurrency']
        out_Currency = testRouting['currency']
        pro_Currency = testRouting['providerCurrency']
        curconversions = testRouting['currencyConversions']
        policyChanges = testRouting['policyPriceChanges']
        adultPrice = testRouting['adultPrice']
        self.log.info('policyChanges:%s；'%policyChanges)
        if pro_Currency != mas_Currency:
            rate,source,idply = self.getRoutingCurrencyConvs(method=2,conversions=curconversions,
                                                             fromC=pro_Currency,toC=mas_Currency)
            oriAult_Price = oriAult_Price * rate

        amountMasCur = self.Test_CountAdultPrice(oriprice=oriAult_Price,policyList=policyChanges)
        amountOutCur = amountMasCur
        if mas_Currency != out_Currency:
            rate,source,idply = self.getRoutingCurrencyConvs(method=2,conversions=curconversions,
                                                             fromC=mas_Currency,toC=out_Currency)
            amountOutCur = amountMasCur * rate
        self.log.info('原始价格(币种:%s):%d，本位币报价(本位币:%s):%d，计算对外报价(报价币:%s):%d；'%(pro_Currency,oriAult_Price,
                                                                   mas_Currency,amountMasCur,out_Currency,amountOutCur))
        result = adultPrice-amountOutCur
        print('ori:', oriAult_Price, 'amountMasCur', amountMasCur)
        if result >2 or result < -2:
            raise Exception('计算值%s和对外报价值%s差值%s大于2，请检查；'%(amountOutCur,adultPrice,result))

        self.log.info('计算值%s和对外报价值%s差值%s；'%(amountOutCur,adultPrice,result))


    def Test_CountAdultPrice(self,oriprice='',policyList=[]):
        for i in policyList:
            try:
                pri = i['adultChange']['totalChange']['amount']
                display = i['displayNumber']
                self.log.info('%s policy 加价值:%d' %(display,pri))
                oriprice += pri
            except Exception:
                pass
        return oriprice