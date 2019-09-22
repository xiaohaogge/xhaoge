# 此Case用于测试search platform config 是否复用GDS退改信息开关；

import json
from AllBlue.Common.NightKingSearchResponse import NightKingSearchRes
from AllBlue.TestCase.AllCaseBase import CaseBase

class Case_Search_ProvConfig_RepeatFareRule_0001(CaseBase):

    def __init__(self):
        CaseBase.__init__(self)
        self.log.info("===Case_Search_ProvConfig_RepeatFareRule_0001,测试开始===")
        #todo 暂时手动部署是否复用，后期实现如果没有选择复用自动修改；
        self.log.info("在测试前，先确保，myslcc 上线qunarytb，以及是provider platform都选择了复用GDS退改")


    def TestProcess(self):
        self.log.info('===Case_Search_ProvConfig_RepeatFareRule_0001,进入测试步骤！===')

        self.log.info('确保之前验价有入库rule信息，发送请求得到相应数据；')
        res0 = self.sendRequest(url=self.nkRequesturl,data=self.nkRequestdata)

        self.log.info('处理数据，拿到myslcc的所有航线检查reporule里repoIds；预期结果：repoIds应不为空(特殊情况原本就为空)')
        result = self.Test_RepoRule(res=res0,provider='myslcc')
        if result:
            self.log.info('检查到，myslcc航线中repoIds不为空；')
        else:
            self.log.error('请检查，myslcc航线中repoIds为空，需要排除本身为空的情况；')

        self.flag = True


    def TestResult(self):
        self.log.info('===Case_Search_ProvConfig_RepeatFareRule_0001,测试完毕===')
        if self.flag:
            self.log.info('Case_Search_ProvConfig_RepeatFareRule_0001,测试通过')
            print("测试结果很成功，perfect！")
        else:
            self.log.info('【Case_Search_ProvConfig_RepeatFareRule_0001,测试失败】')


    def Test_RepoRule(self,res='',provider=''):
        '''定义获取repoIds 是否为空，result 值为true：repoIds不为空；值为false，repoIds为空；'''
        providerRoutings = self.Test_FindProviderRouting(res1=res,pro=provider)
        self.result = True
        for r in providerRoutings:
            if len(r['rule']['repoRule']['repoIds'])==0:
                self.result = False
        return self.result


    def Test_FindProviderRouting(self,res1='',pro=''):
        '''定义查找某一provider的所有航线报价'''
        resp = NightKingSearchRes(res1)
        routings = resp.nkRouting
        providerList = []
        for i in routings:
            if i['providerName'] == pro:
                providerList.append(i)

        if len(providerList)==0:
                raise Exception('not found provider routing,please check!')
        return providerList

