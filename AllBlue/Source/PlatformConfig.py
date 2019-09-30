# 此模块用于读取xml文件中的信息；

import os
import xml.etree.ElementTree as ET


def startReadPlatform():
    basedir = os.path.dirname(__file__)
    Dom = ET.parse(basedir+'\Platform.xml')
    caseList = []
    Dom.getroot()
    try:
        for i in range(10000):
            case = {}
            caseId = Dom.findall('./RunCase/case/id')[i]
            caseAddr = Dom.findall('./RunCase/case/Address')[i]
            case['Casename'] = caseId.text
            case['Address'] = caseAddr.text
            caseList.append(case)

    except Exception:
        print("caseList:",caseList)
        return caseList

