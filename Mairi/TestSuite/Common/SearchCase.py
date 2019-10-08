'''
定义一个基本类；
'''

import json
import random
from selenium import webdriver


class CaseBase():

    def __init__(self):
        self.chrome = webdriver.Chrome()
        self.url = "https://mairi.gloryholiday.com/"
        self.flag = False



    def TestProcess(self):
        pass


    def TestResult(self):
        pass


