import unittest
import requests
from UniAutos.src.CommonFunc.runRequest import RunRequest
from UniAutos.src.ParameteCollection.SearchParamete import nima
'''
    进行测试用例的编写；
'''

class Mysearch(unittest.TestCase):
    def setUp(self):
        self.method = 'post'
        self.base_url = "http://39.105.118.191:18089/tpnan/search"
        self.base_data = '''
                            {
                                "adultNum":1,
                                "channel":"F",
                                "childNum":1,
                                "cid":"ctrip",
                                "domain":"tpnan",
                                "fromCity":"SAO",
                                "fromDate":"20200106",
                                "infantNum":0,
                                "maxWaitTime":60000,
                                "retDate":"20200108",
                                "toCity":"YVR",
                                "tripType":"2",
                                "useCache":1,
                                "useFilter":true,
                                "searchRatio":false
                            }
                        '''
        self.testcase = RunRequest()

    def test01(self):
        print('测试开始了哟')
        print('正在进行测试')

        # r = requests.post(self.base_url, data=self.base_data)
        # result = r.json()
        # print(result)
        # if r.status_code != 200:
        #     for i in range(2):
        #         r = requests.post(self.base_url, data=self.base_data)
        #         result = r.json()
        #         print(result)
        s = 'ssss'
        print('他大舅都是他舅',s)
        print('2333333333333333333333333333333333333333333333333333')
        self.assertEqual(3,3,msg='nima')


    def test02(self):
        print('进行第二次测试')
        self.assertEqual(4,4)
        nima()
        result = self.testcase.sendRequest(self.method,self.base_url,self.base_data)
        print(result)

    def tearDown(self):
        print('环境销毁；')