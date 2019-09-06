

import json
from AllBlue.CommonFunc.Base import AllBase


class CaseBase(AllBase):

    def __init__(self):
        AllBase.__init__(self)
        self.flag = False
        self.nkRequesturl = 'http://dev-api.gloryholiday.com/yuetu/search'
        data = '''
                    {
                            "Cid": "qunarytb",
                            "TripType": "1",
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
        self.nkRequestData = json.loads(data)

        self.PreProdRate = 'http://pre-prod-restful-api.gloryholiday.com/nightking/exchangeRate'
        self.ProdRate = 'http://prod-restful-api.gloryholiday.com/nightking/exchangeRate'


    def TestProcess(self):
        pass


    def TestResult(self):
        pass


    # 定义公共方法，用于获取Cuurrncy；
    def Test_Currency(self,pro='sscts',cid='ctrip',ori="USD",tar='CNY'):
        strJoin = "?providerName={}&cid={}&originalCode={}&targetCode={}".format(pro,cid,ori,tar)
        sendUrl = self.ProdRate+strJoin
        # print(sendUrl)
        # pre-prod-restful-api.gloryholiday.com/nightking/exchangeRate?providerName=sscts&cid=ctrip&originalCode=USD&targetCode=CNY
        resjson = self.sendRequest(method='GET',url=sendUrl)
        resdict = json.loads(resjson)
        print(resdict)
        try:
            if resdict['msg'] == "success":
                self.log.info('获取汇率%s；' % resdict['msg'])
            else:
                self.log.error('获取汇率%s；' % resdict['msg'])
        except Exception as e:
            self.log.error('获取汇率:%s,报错：%s'%(resdict,e))
        self.log.info('from:%s to:%s rate:%s'%(ori,tar,resdict['exchange_rate']['exchange_rate']))
        print('from:%s to:%s rate:%s'%(ori,tar,resdict['exchange_rate']['exchange_rate']))



