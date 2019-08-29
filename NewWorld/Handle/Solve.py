# 定义在测试用力run前的数据处理；

import importlib

from NewWorld.Source.ReadXml import Readxml


class DealData():
    # l = [{"case":"Case_Search_KeyValue_0001","address":"NewWorld\TestCase\Search\Case_Search_KeyValue_0001"}]
    def buildCase(self,l):
        self.runcase = ''
        for runner in l:
            print(runner["case"])
            print(runner["address"])
            try:
                self.r = importlib.import_module('NewWorld\TestCase\Search\Case_Search_KeyValue_0001.Case_Search_KeyValue_0001')
                self.r.TestProcess()
            except Exception as e:
                return e
        pass


if __name__ == "__main__":
    l = [{"case": "Case_Search_KeyValue_0001", "address": "NewWorld\TestCase\Search\Case_Search_KeyValue_0001"}]
    rr = DealData()

    rr.buildCase(l)