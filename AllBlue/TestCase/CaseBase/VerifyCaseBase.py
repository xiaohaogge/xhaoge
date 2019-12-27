
from AllBlue.TestCase.CaseBase.AllCaseBase import CaseBase


class VerifyBase(CaseBase):

    def __init__(self):
        CaseBase.__init__(self)
        self.flag = False


    def TestProcess(self):
        pass


    def TestResult(self):
        pass

    # 定义verify 响应回来是否为200，routing信息是否不为空，以及是否有重搜；
    def checkVerifyIsSuccess(self,status=200,**kwargs):
        try:
            if kwargs['baseResponse']['status'] != status or len(kwargs['routing']) == 0:
                return self.log.error("verify 报错：%s"%(kwargs['baseResponse']['message']))
        except Exception as e:
            return self.log.error("search 报错：%s"%e)







