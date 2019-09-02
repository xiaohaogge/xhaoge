# 定义在测试用力run前的数据处理；

import importlib
from AllBlue.Source.ReadBaseConfig import BaseConfig


class Controler(BaseConfig):

    def __init__(self):
        BaseConfig.__init__(self)
        self.startRead()
        self.buildCase()

    def buildCase(self):
        self.runcase = ''
        for runner in self.caseList:
            print("Casename:"+runner["Casename"],"   Address:"+runner["Address"])
            try:
                caseModule = importlib.import_module(runner["Address"])
                ModuleClass = getattr(caseModule,runner["Casename"])
                self.caseRun = ModuleClass()
                self.caseRun.TestProcess()
                print('========================')
            except Exception as e:
                self.log.error('casename:',runner["Casename"]+"报错：",e)
                print(e)

                self.caseRun.TestResult()


# if __name__ == "__main__":
#     # caselist = [{"case": "Case_Search_KeyValue_0001", "Address": "AllBlue\TestCase\Search\Case_Search_KeyValue_0001"}]
#     rr = DealData()
#     rr.buildCase()