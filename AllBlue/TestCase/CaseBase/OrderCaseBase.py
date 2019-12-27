

import random
from AllBlue.TestCase.CaseBase.AllCaseBase import CaseBase
from AllBlue.Source.OrderConfig import startReadOrder


class OrderBase(CaseBase):

    def __init__(self):
        CaseBase.__init__(self)
        self.passengersList = startReadOrder() # {0:[passengers],1:[],2:[]}


    # 通过不同平台 统一发送请求
    def searchByCid(self,cid="ctrip"):
        pass


    # 从读取的配置文件中，随机的拿取相应的乘客类型信息；
    def filterOrderMan(self,adultNum=1,childNum=0,infantNum=0):
        orderManList = []
        # 随机的从列表中 选取相应人数的乘客类型；
        adult = random.sample(self.passengersList["0"],adultNum)
        child = random.sample(self.passengersList["1"],childNum)
        infant = random.sample(self.passengersList["2"],infantNum)
        for a in adult:
            orderManList.append(a)
        if len(child) != 0:
            for c in child:
                orderManList.append(c)
        if len(infant) != 0 :
            for i in infant:
                orderManList.append(i)
        return orderManList


    # 定义判断从order 响应回来是否未200 并且routing 不为空；
    def checkOrderIsSuccess(self):
        pass





