# Currency Rate
# 此case用于并发进行监控余额扣款测试；


import json
from AllBlue.TestCase.AllCaseBase import CaseBase
import threading

class Case_Others_Monitor_Deduction(CaseBase):

    def __init__(self):
        CaseBase.__init__(self)
        self.log.info("===Case_Others_Monitor_Deduction,测试开始===")


    def TestProcess(self):
        th = []
        for i in range(10):
            t = threading.Thread(target=self.nima())
            print(t)
            th.append(t)
        for h in th:
            h.start()


    def TestResult(self):
        self.log.info('===Case_Others_Monitor_Deduction,测试完毕===')
        if self.flag:
            self.log.info('=========Case_Others_Monitor_Deduction,测试通过')
            print("测试结果很成功，perfect！")
        else:
            self.log.info('=========Case_Others_Monitor_Deduction,测试失败')

    def nima(self):
        url0 = 'http://39.105.118.191:18089/common/updatebalance'
        data0 = '''
                        {"balanceChange":50.15,"operateUser":"xhaoge","providerName":"myslcc","type":0}
                '''
        self.sendRequest(url=url0, data=data0)






