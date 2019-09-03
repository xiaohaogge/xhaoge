# 此模块用于读取xml文件中的信息；

import xml.etree.ElementTree as ET
from AllBlue.CommonFunc.Base import AllBase

class BaseConfig(AllBase):

    def __init__(self):
        AllBase.__init__(self)
        self.Dom = ET.parse('D:\program\Python\yueTu\AllBlue\Source\BasicConfig.xml')
        self.nkReqData = {"search_url":""}
        self.nkResData = {"search_url":""}
        self.logPath = {"log_path":""}
        self.caseList = []
        # 定义统一的数据读取集合；按照id区分类型，data中存取有效数据；
        self.ParaCollection = [
                            {"id":"nightKingReq","data": self.nkReqData},
                            {"id":"nightkingRes","data":self.nkResData},
                            {"id":"logPath","data":self.logPath},
                            {"id":"case","data":self.caseList}]
        #self.startRead()


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

        except Exception:
            pass
        print(self.ParaCollection)






