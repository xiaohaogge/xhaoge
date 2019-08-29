# 此模块用于读取xml文件中的信息；

import xml.etree.ElementTree as ET


class ReadBaseConfig():

    def __init__(self):
        self.Dom = ET.parse('BasicConfig.xml')
        self.nkReqData = {"url":""}
        self.nkResData = {"url":""}
        self.logPath = {"path":""}
        self.ParaCollection = [{"id":"nightKingReq","data": self.nkReqData},
                          {"id":"nightkingRes","data":self.nkResData},
                          {"id":"logPath","data":self.logPath}]
        #self.nextdom = self.Dom.documentElement


    def startRead(self):
        self.Dom.getroot()
        nkRequrl = self.Dom.findall('./switch/item/nkReq_url')[0]
        self.nkReqData["url"]=nkRequrl.text
        path = self.Dom.findall('./logAddress')[0]
        self.logPath['path']=path.text

        self.caseList = []
        case = {}
        self.caseId = self.Dom.findall('./RunCase/case/id')[0]
        self.caseAddr = self.Dom.findall('./RunCase/case/Address')[0]
        case['id']=self.caseId.text
        case['Address']=self.caseAddr.text
        self.caseList.append(case)
        print(self.caseList)
        print(self.ParaCollection)



if __name__ == "__main__":
    readme = ReadBaseConfig()
    readme.startRead()



