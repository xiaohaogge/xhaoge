# 此模块用于读取xml文件中的信息；

import xml.etree.ElementTree as ET


class Readxml():


    def __init__(self):
        self.Dom = ET.ElementTree(file='BasicConfig.xml')
        pass


    def startRead(self):
        self.Dom.getroot()
        pass



