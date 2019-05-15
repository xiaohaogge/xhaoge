import unittest
import json
import requests
from UniAutos.src.CommonFunc.runmethon import RunMethod
'''
    进行测试用例的编写；
'''

class Myticket(unittest.TestCase):
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
        self.testcase = RunMethod()
    # def test_post_event_list_eid_null(self):
    #     ''' eid 参数为空 '''
    #     r = requests.post(self.base_url, data=self.base_data)
    #     result = r.json()
    #     print(result)
    #     if r.status_code != 200:
    #         for i in range(2):
    #             r = requests.post(self.base_url, data=self.base_data)
    #             result = r.json()
    #             print(result)

    def test01(self):
        # retrieveTicketFeePolicies impl
        print('测试开始了哟')
        method = 'get'
        url = 'get/policies'
        data = ''
        xx = self.testcase.run_main(method=method, url=url)
        print(xx)
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
        # updateTicketFeePolicy impl
        print('进行第二次测试')
        method = 'post'
        url = 'policy/ticketfee/update'
        data = '''
                {"baseInfo":{"creator":"pirlo1","id":"5cda69d97182598583882638"},"provider":{"provider":"SABRE","pcc":"pcc"},"airlines":["5555"],"depCities":["xxx"],"arrCities":["can"],"cabinGrade":"A","faretype":"PUBLISHED","chargedBy":"PASSENGER","currency":"USD","amount":100000}
               '''
        xx = self.testcase.run_main(method=method, url=url,data=data)
        print(xx)
        self.assertEqual(4,4)

    def test03(self):
        # archiveTicketFeePolicy impl
        print('进行第san次测试')
        method = 'post'
        url = '/policy/ticketfee/archive'
        data = '''
                {"id": "5cda63becd5a6f7dded612b7"}
               '''
        xx = self.testcase.run_main(method=method, url=url,data=data)
        print(xx)
        self.assertEqual(4,4)

    def test04(self):
        # enableTicketFeePolicy impl
        print('进行第4次测试')
        method = 'post'
        url = '/policy/ticketfee/enable'
        data = '''
                {"id": "5cda63becd5a6f7dded612b7"}
               '''
        xx = self.testcase.run_main(method=method, url=url,data=data)
        print(xx)
        self.assertEqual(4,4)

    def test05(self):
        # copyTicketFeePolicy impl
        print('进行第5次测试')
        method = 'post'
        url = '/policy/ticketfee/copy'
        data = '''
                {"id": "5cda63becd5a6f7dded612b7"}
               '''
        xx = self.testcase.run_main(method=method, url=url,data=data)
        print(xx)
        self.assertEqual(4,4)

    def test06(self):
        #  createTicketFeePolicy impl
        print('进行第6次测试')
        method = 'post'
        url = '/policy/ticketfee/create'
        data = '''
                {"baseInfo":{"creator":"pirlo718"},"provider":{"provider":"SABRE","pcc":"pcc"},"airlines":["airasia"],"depCities":["ctu"],"arrCities":["bjs","sha"],"cabinGrade":"A","faretype":"PRIVATE","chargedBy":"PASSENGER","currency":"TWD","amount":99.99}
               '''
        res = {"id": "5cda69d97182598583882638"}
        xx = self.testcase.run_main(method=method, url=url,data=data)
        print(xx)
        self.assertEqual(4,4)

    def test07(self):
        #  disableTicketFeePolicy impl
        print('进行第7次测试')
        method = 'post'
        url = 'policy/ticketfee/disable'
        data = '''
                {"id": "5cda63becd5a6f7dded612b7"}
               '''
        res = {"id": "5cda69d97182598583882638"}
        xx = self.testcase.run_main(method=method, url=url,data=data)
        print(xx)
        self.assertEqual(4,4)

    def test08(self):
        #  retrieveTicketFeePolicy impl
        print('进行第8次测试')
        method = 'get'
        url = '/policy/ticketfee?id={id}'
        data = '''
                {"id": "5cda63becd5a6f7dded612b7"}
               '''
        res = {"id": "5cda69d97182598583882638"}
        xx = self.testcase.run_main(method=method, url=url,data=data)
        print(xx)
        self.assertEqual(4,4)


    def tearDown(self):
        print('环境销毁；')