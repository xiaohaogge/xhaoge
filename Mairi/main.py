# 2019-08-19



from selenium import webdriver
import time
from Mairi.TestSuite.search import Search

if __name__ == '__main__':
    mybrowser = webdriver.Chrome("./Source/chromedriver.exe")
    url = 'https://mairi.gloryholiday.com/'
    print("nima")
    try:
        mybrowser.get(url)
    except Exception as e:
        print("报错：", e)
    time.sleep(5)
    mybrowser.quit()