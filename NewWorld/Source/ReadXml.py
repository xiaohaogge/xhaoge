# 此模块用于读取xml文件中的信息；

import xml.etree.ElementTree as ET


class Readxml():


    def __init__(self):
        self.Dom = ET.parse('BasicConfig.xml')
        print(self.Dom)
        self.Data = {"url":""}
        self.Parameter = {"id": "nightKingReq", "data": self.Data}
        #self.nextdom = self.Dom.documentElement


    def startRead(self):
        self.Dom.getroot()
        self.url = self.Dom.findall('./switch/item/nkReq_url')[0]
        url = self.url.text
        self.Data["url"]=url
        print(type(self.url))
        print(self.url.text)
        print(self.Data)
        print(self.Parameter)
        pass



if __name__ == "__main__":
    readme = Readxml()
    readme.startRead()



# https://blog.csdn.net/weixin_42547344/article/details/81097633