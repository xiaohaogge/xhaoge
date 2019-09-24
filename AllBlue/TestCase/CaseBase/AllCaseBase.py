

import json
import random
from AllBlue.Common.Base import AllBase
from AllBlue.Common.NightKingSearchResponse import NightKingSearchRes


class CaseBase(AllBase):

    def __init__(self):
        AllBase.__init__(self)
        self.flag = False
        # 测试环境的night king请求的url，data参数；
        self.nkRequesturl = 'http://dev-api.gloryholiday.com/yuetu/search'
        self.nkRequestdata = '''
                    {
                            "Cid": "qunarytb",
                            "TripType": "2",
                            "FromCity": "HKG",
                            "ToCity": "LAX",
                            "FromDate": "20191123",
                            "RetDate": "20191221",
                            "AdultNumber": 1,
                            "ChildNumber": 0,
                            "InfantNumber":0,
                            "Currency":"CNY",
                            "BypassCache": true,
                            "GodPerspective":false
                    }'''

        self.nkRequestDataDict = json.loads(self.nkRequestdata) # 将请求参数从str转为dict，方便修改参数；
        # 汇率的几个接口地址，测试、生产；
        self.PreProdExchangeRate = 'http://pre-prod-restful-api.gloryholiday.com/nightking/exchangeRate'
        self.ProdExchangeRate = 'http://prod-restful-api.gloryholiday.com/nightking/exchangeRate'
        self.devExchangeRate = 'http://dev-restful-api.gloryholiday.com/nightking/exchangeRate'
        self.get25Hours = 'http://dev-restful-api.gloryholiday.com/currencyservice/getCurrencyListOfLatest25Hour'
        self.getCurrency = 'http://dev-restful-api.gloryholiday.com/currencyservice/getCurrency'
        self.quotaCurrency = 'http://dev-restful-api.gloryholiday.com/marineford/currency/manualquota'
        self.getCurrencyList = 'http://dev-restful-api.gloryholiday.com/currencyservice/getCurrencyList'


    def TestProcess(self):
        pass


    def TestResult(self):
        pass











    # todo 对响应状态进行判断；low
    def checkNkStatus(self,nk):
        res = json.loads(nk)
        try:
            res_Status = res['baseResponse']['status']
        except Exception as e:
            return e
        if res_Status == 500:
            self.log.error('status:%s,message:%s' % (res['baseResponse']['status'], res['baseResponse']['message']))
            raise Exception(500)
        elif res_Status == 200:
            if len(res['routing']) == 0:
                self.log.error('status:200,routing信息为null；')
                raise Exception(204)
            else:
                self.log.info('status:200,返回报价无错误；')
        else:
            self.log.error('checkNKStatus: unknow error ')
            raise Exception(404)


    def Test_Currency(self,method=1,env='dev',pro='sscts',cid='ctrip',ori="USD",tar='CNY'):
        '''定义公共方法，用于获取Cuurrncy rate；
            method=1,表示check 是否有获取到汇率，method=2,表示return currency；
        '''
        strJoin = "?providerName={}&cid={}&originalCode={}&targetCode={}".format(pro,cid,ori,tar)
        sendUrl = self.devExchangeRate+strJoin if env=='dev' else self.ProdExchangeRate+strJoin
        # pre-prod-restful-api.gloryholiday.com/nightking/exchangeRate?providerName=sscts&cid=ctrip&originalCode=USD&targetCode=CNY
        resjson = self.sendRequest(method='GET',url=sendUrl)
        resdict = json.loads(resjson)
        if resdict['msg'] == "success":
            self.log.info('获取汇率%s；from:%s to:%s rate:%s' % (resdict['msg'], ori, tar, resdict['exchange_rate']['exchange_rate']))
            print('获取汇率%s；from:%s to:%s rate:%s' % (resdict['msg'], ori, tar, resdict['exchange_rate']['exchange_rate']))
        else:
            return 404
        if method==2:
            return resdict['exchange_rate']['exchange_rate']
        return 200


    def Test_Provider_Master(self,provider='',routings=''):
        '''定义方法，测试从provider 币种到本位币，再到报价币种的测试；'''
        prolist = []
        for d in routings:
            if d["providerName"] == provider:
                prolist.append(d)

        num = len(prolist)
        if num == 0:
            return self.log.info('该供应商没有航线报出:%s'%provider)
        '''随机抽取其中一条航线，进行测试计算；'''
        testnum = random.randint(0,num-1)
        self.log.info('%s总航线数目：%s,选择的是：%s'%(provider,num,testnum))
        testrouting = prolist[testnum]
        proCurrency = testrouting['providerCurrency']
        masCurrency = testrouting['masterCurrency']
        outcurrency = testrouting['currency']
        cuyconversions = testrouting['currencyConversions']
        self.log.info('【2.1.%s是否有获取到provider 到master currency】'%provider )
        pro_res = self.getRoutingCurrencyConvs(method=1,conversions=cuyconversions,
                                         fromC=proCurrency,toC=masCurrency)
        if pro_res:
            self.log.info('汇率转化存在；%s'% pro_res)
        else:
            self.log.error('转化汇率不存在；from %s to %s')%(proCurrency,masCurrency)
        # if cid=='iwoflyCOM':
        #     if reqCurrency != 'USD' and reqCurrency !='HKD':
        #         out_res = self.getRoutingCurrencyConvs(method=1,conversions=cuyconversions,
        #                                                fromC=masCurrency,toC=outcurrency)
        #         if out_res:
        #             self.log.info('汇率转化有获取；')
        #         else:
        #             self.log.error('不存在转化汇率；from %s to %s') % (proCurrency, masCurrency)



    def getRoutingCurrencyConvs(self,method=1,conversions=None,fromC='',toC=''):
        '''
        目前提供2种方式：
            1是代码查询是否有这个汇率，返回bool值；
            2是拿取汇率，返回rate，以及source，和policyid
        '''
        if len(conversions)==0:
            self.log.error('conversions is null，big problem；')
            # todo 需要主动抛异常；
        for n in conversions:
            if n['from']==fromC and n['to']==toC:
                if method==1:
                    return True,n['rate']
                if method==2:
                    return n['rate'],n['source'],n['policyId']
        return False,"汇率 from %s to %s nothing"%(fromC,toC)

    def Test_TargetProviders(self,res):
        case_c2 = NightKingSearchRes(res)
        self.routingslist = case_c2.nkRouting
        for i in case_c2.nkTraceSpans:
            try:
                pro = i['tags']['nk-wb-final-target-providers']
                providers = pro.split(',')
                return providers
            except Exception:
                pass






