# coding=utf-8

'''
定义程序主入口
'''
import time
from selenium import webdriver
from UniAutos.AllBlueUI.COMMISSION.Commission import Commission
from UniAutos.AllBlueUI.CommonFunction import login
class Runc():
    # 绑定浏览器驱动器；
    browser = webdriver.Chrome()
    def __init__(self):
        pass


if __name__ == "__main__":
    runc = Runc()
    login(runc.browser)
    commission = Commission(runc.browser)

    # runc.browser.quit()

