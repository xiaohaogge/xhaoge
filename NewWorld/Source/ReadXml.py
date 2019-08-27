# 此模块用于读取xml文件中的信息；

import xml.etree.cElementTree as ET


class Readxml():


    def __init__(self):
        self.Dom = ET.parse('BasicConfig.xml')
        print(self.Dom)
        self.Data = {"url":""}
        self.Parameter = {"id": "nightKingReq", "data": self.Data}


    def startRead(self):
        self.Dom.getroot()
        pass



if __name__ == "__main__":
    readme = Readxml()
