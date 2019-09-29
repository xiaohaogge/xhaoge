# 写个脚本，用于跑到测试生单步骤；
from selenium import webdriver


class Case_mairi_AllProcess_0001:

    def __init__(self):
        self.chrome = webdriver.Chrome()
        url = "https://mairi.gloryholiday.com/"
        r = self.chrome.get(url=url)



if __name__ == "__main__":
    rr = Case_mairi_AllProcess_0001()
