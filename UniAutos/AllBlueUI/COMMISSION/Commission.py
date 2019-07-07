# coding=utf-8

# 使用selenium用于对于Allblue中政策的添加；减少手动添加的繁琐；

import time
from UniAutos.AllBlueUI.COMMISSION.CommissionData import ComsData
class Commission():
    def __init__(self,browser):
        self.browser = browser
        # 登录进去后，点击政策信息，窗口最大化，点击前返，并点击添加；
        time.sleep(2)
        try:
            self.browser.find_element_by_xpath('//span[contains(text(),"政策信息")]').click()
        except Exception as e:
            print("报错：",e)
        time.sleep(2)
        try:
            self.browser.find_element_by_xpath('//li[contains(text(),"前返政策")]').click()
        except Exception as e:
            print("报错：",e)
        time.sleep(2)
        try:
            self.browser.find_element_by_xpath('//span[contains(text(),"添加")]').click()
        except Exception as e:
            print("报错：",e)
        #开始进行添加,实例化对象参数再进行访问；
        data = ComsData()
        try:
            self.browser.find_element_by_xpath('//div/label[contains(text(),"政策编号")]/..//input').send_keys(data.number)
            time.sleep(1)
            self.browser.find_element_by_xpath('//div[@class="el-form-item el-form-item--mini"]/label[contains(text(),"备注")]/..//textarea').send_keys(data.remark)
            time.sleep(1)
            self.browser.find_element_by_xpath('//div/label[contains(text(),"开票航司")]/..//input[@placeholder="请输入"]').send_keys(data.validating)
            self.browser.find_element_by_xpath(
                "//div/label[contains(text(),'运价类型')]/..//span[contains(text(),%s)]" % ("'" + data.faretype + "'")).click()
            self.browser.find_element_by_xpath(
                "//span[@class='el-radio-button__inner' and contains(text(),%s)]" % ("'" + data.triptype + "'")).click()
            self.browser.find_element_by_xpath('//div[@class="el-form-item is-required el-form-item--mini"]/label[contains(text(),"出发")]/..//input').send_keys(data.fromCtiy)
            self.browser.find_element_by_xpath('//div/label[contains(text(),"出发排除")]/..//input').send_keys(data.fromExclude)
            self.browser.find_element_by_xpath('//div[@class="el-form-item is-required el-form-item--mini"]/label[contains(text(),"到达")]/..//input').send_keys(data.toCity)
            self.browser.find_element_by_xpath('//div/label[contains(text(),"到达排除")]/..//input').send_keys(data.toExclude)
            fbxpath = "//div/label[contains(text(),'fb一致性')]/..//span[contains(text(),%s)]"%("'"+data.fbCTcy+"'")
            print(fbxpath)
            self.browser.find_element_by_xpath("//div/label[contains(text(),'fb一致性')]/..//span[contains(text(),%s)]"%("'"+data.fbCTcy+"'")).click()

            self.browser.find_element_by_xpath("//div/label[contains(text(),'1/2RT')]/..//span[contains(text(),%s)]"%("'"+data.RT[0]+"'")).click()
            # 当RT选择适用时，需要选择取高，取低，平均
            windows = browser.window_handles
            self.browser.switch_to.window(windows[-1])
            if data.RT == "适用":
                self.browser.find_element_by_xpath(
                    "//span[contains(text(),%s)]" % ("'" + data.RT[1] + "'")).click()
            self.browser.find_element_by_xpath("//div/label[contains(text(),'Q值')]/..//span[contains(text(),%s)]"%("'"+data.Qvalue+"'")).click()
            # 添加小条目；
            for x in data.cabinclass:
                if x == "经济":
                    pass
                else:
                    self.browser.find_element_by_xpath(
                        "//div/label[contains(text(),'舱等')]/..//span[contains(text(),%s)]" % ("'" + x + "'")).click()
            if "经济" not in data.cabinclass:
                self.browser.find_element_by_xpath("//div/label[contains(text(),'舱等')]/..//span[contains(text(),'经济')]").click()

            self.browser.find_element_by_xpath("//div/label[contains(text(),'舱位')]/..//input").send_keys(data.cabin)
            self.browser.find_element_by_xpath("//div/label[contains(text(),'ADT%')]/..//input").clear()
            self.browser.find_element_by_xpath("//div/label[contains(text(),'ADT%')]/..//input").send_keys(data.ADT[0])
            self.browser.find_element_by_xpath("//div/label[contains(text(),'ADT$')]/..//input").clear()
            self.browser.find_element_by_xpath("//div/label[contains(text(),'ADT$')]/..//input").send_keys(data.ADT[1])
            self.browser.find_element_by_xpath("//div/label[contains(text(),'CHD%')]/..//input").clear()
            self.browser.find_element_by_xpath("//div/label[contains(text(),'CHD%')]/..//input").send_keys(data.CHD[0])
            self.browser.find_element_by_xpath("//div/label[contains(text(),'CHD$')]/..//input").clear()
            self.browser.find_element_by_xpath("//div/label[contains(text(),'CHD$')]/..//input").send_keys(data.CHD[1])
            self.browser.find_element_by_xpath("//div/label[contains(text(),'YQ%')]/..//input").clear()
            self.browser.find_element_by_xpath("//div/label[contains(text(),'YQ%')]/..//input").send_keys(data.tax[0])
            self.browser.find_element_by_xpath("//div/label[contains(text(),'YR%')]/..//input").clear()
            self.browser.find_element_by_xpath("//div/label[contains(text(),'YR%')]/..//input").send_keys(data.tax[1])
            self.browser.find_element_by_xpath("//div/label[contains(text(),'UO%')]/..//input").clear()
            self.browser.find_element_by_xpath("//div/label[contains(text(),'UO%')]/..//input").send_keys(data.tax[2])

        except Exception as e:
            print(e)
        time.sleep(1)





