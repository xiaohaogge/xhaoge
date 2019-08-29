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
        url = self.Dom.findall('./switch/item/nkReq_url')[0]
        nkRequrl = url.text
        self.nkReqData["url"]=nkRequrl
        path = self.Dom.findall('./logAddress')[0]
        self.logPath['path']=path.text

        print(self.ParaCollection)



if __name__ == "__main__":
    readme = ReadBaseConfig()
    readme.startRead()



