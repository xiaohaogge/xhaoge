# 此模块用于读取xml文件中的信息；

import xml.etree.ElementTree as ET
from NewWorld.CommonFunc.Base import AllBase

class BaseConfig(AllBase):

    def __init__(self):
        AllBase.__init__(self)
        self.Dom = ET.parse('F:\Program\python\yueTu\\NewWorld\Source\BasicConfig.xml')
        self.nkReqData = {"url":""}
        self.nkResData = {"url":""}
        self.logPath = {"path":""}
        self.caseList = []
        # 定义统一的数据读取集合；按照id区分类型，data中存取有效数据；
        self.ParaCollection = [
                            {"id":"nightKingReq","data": self.nkReqData},
                            {"id":"nightkingRes","data":self.nkResData},
                            {"id":"logPath","data":self.logPath},
                            {"id":"case","data":self.caseList}]
        self.startRead()


    def startRead(self):
        self.Dom.getroot()
        nkRequrl = self.Dom.findall('./switch/item/nkReq_url')[0]
        self.nkReqData["url"]=nkRequrl.text
        path = self.Dom.findall('./logAddress')[0]
        self.logPath['path']=path.text

        try:
            for i in range(10000):
                case = {}
                caseId = self.Dom.findall('./RunCase/case/id')[i]
                caseAddr = self.Dom.findall('./RunCase/case/Address')[i]
                case['Casename'] = caseId.text
                case['Address'] = caseAddr.text
                self.caseList.append(case)

        except Exception as e:
            print(e)
        print(self.ParaCollection)






