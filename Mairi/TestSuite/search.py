#只是用于简单的search搜索；
import time
from selenium import webdriver



class Search():

    def __init__(self):
        self.browser = webdriver.Chrome("./Source/chromedriver.exe")

