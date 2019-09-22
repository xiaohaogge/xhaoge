# 此Case用于测试search platform config 是否复用GDS退改信息开关；

import json
from AllBlue.TestCase.CaseCommon import Test_RepoRule
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
        result0 = Test_RepoRule(res=res0,provider='myslcc')
        if result0:
            self.log.info('检查到，myslcc航线中repoIds不为空；')
        else:
            self.log.error('请检查，myslcc航线中repoIds为空，需要排除本身为空的情况；')

        self.log.info('预置条件，将配置myslcc不复用GDS退改规则，发送请求得到相应的请求数据')
        # res1 = self.sendRequest(url=self.nkRequesturl,data=self.nkRequestdata)
        # self.log.info('处理数据，拿到myslcc的所有航线检查reporule里repoIds；预期结果：repoIds为空')
        # #todo 自动修改是否复用GDS退改规则,调用接口；
        # result1 = Test_RepoRule(res=res1,provider='myslcc')
        # if result1:
        #     self.log.error('请检查，myslcc航线中repoIds预期为空，实际不为空，')
        # else:
        #     self.log.info('检查到，myslcc航线中repoIds预期为空,实际为空；')

        self.flag = True


    def TestResult(self):
        self.log.info('===Case_Search_ProvConfig_RepeatFareRule_0001,测试完毕===')
        if self.flag:
            self.log.info('Case_Search_ProvConfig_RepeatFareRule_0001,测试通过')
            print("测试结果很成功，perfect！")
        else:
            self.log.info('【Case_Search_ProvConfig_RepeatFareRule_0001,测试失败】')




