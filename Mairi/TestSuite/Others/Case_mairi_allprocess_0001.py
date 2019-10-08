# 写个脚本，用于跑到测试生单步骤；
from selenium import webdriver
from Mairi.TestSuite.Common.SearchCase import CaseBase

class Case_mairi_AllProcess_0001(CaseBase):

    def __init__(self):
        CaseBase.__init__(self)
        r = self.chrome.get(url=self.url)



if __name__ == "__main__":
    rr = Case_mairi_AllProcess_0001()
