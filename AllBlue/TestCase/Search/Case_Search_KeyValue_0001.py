# first case
# 此case 用于简单的发送请求，对于响应字段的对比；


from AllBlue.TestCase.CaseBase.SearchCaseBase import CaseBase

class Case_Search_KeyValue_0001(CaseBase):

    def __init__(self):
        CaseBase.__init__(self)
        self.log.info("nima,开始case的初始化")


    def TestProcess(self):
        res = self.sendRequest(method='POST',url=self.nkRequesturl,data=self.nkRequestdata)
        print(res)
        if res:
            self.log.info('搜索成功，有返回')
            print(type(res))
            print('这是case1 的if 条件语句中；')
        else:
            print(self.log.error('nothing'))

    def TestResult(self):
        print("测试结果很成功，perfect！")

