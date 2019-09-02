# 定义在测试用力run前的数据处理；

import importlib
from AllBlue.Source.ReadBaseConfig import BaseConfig


class Controler(BaseConfig):

    def __init__(self):
        BaseConfig.__init__(self)
        self.buildCase()

    def buildCase(self):
        self.runcase = ''
        for runner in self.caseList:
            print(runner["Casename"])
            print(runner["Address"])
            try:
                r = importlib.import_module(runner["Address"])
                rr = getattr(r,runner["Casename"])
                rrr = rr()
                rrr.TestProcess()
                rrr.TestResult()
                print('========================')
            except Exception as e:
                print(e)


# if __name__ == "__main__":
#     # caselist = [{"case": "Case_Search_KeyValue_0001", "Address": "AllBlue\TestCase\Search\Case_Search_KeyValue_0001"}]
#     rr = DealData()
#     rr.buildCase()