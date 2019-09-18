# 此模块用于读取xml文件中的信息；

import xml.etree.ElementTree as ET
# from AllBlue.Common.Base import AllBase

class BaseConfig():

    def startRead(self):
        self.Dom = ET.parse(r'.\Source\BasicConfig.xml')
        self.nkReqData = {"id": "nightKingReq", "search_url": ""}
        self.nkResData = {"id": "nightkingRes", "search_url": ""}
        self.logPath = {"id": "logPath", "log_path": ""}
        self.caseList = []
        # 定义统一的数据读取集合；按照id区分类型，data中存取有效数据；
        self.ParaCollection = [
            self.nkReqData, self.nkResData, self.logPath,
            {"id": "case", "data": self.caseList}]

        self.Dom.getroot()
        nkRequrl = self.Dom.findall('./switch/item/nkReq_url')[0]
        self.nkReqData["search_url"]=nkRequrl.text
        path = self.Dom.findall('./logAddress')[0]
        self.logPath['log_path']=path.text

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


    def getData(self,searKey,dataValue):
        for i in self.ParaCollection:
            searId = i["id"]
            if searId == searKey:
                return i[dataValue]




