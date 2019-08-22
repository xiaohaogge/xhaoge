# first case

from NewWorld.CommonFunc.Base import AllBase

class CaseSearch0001(AllBase):

    def __init__(self):
        AllBase.__init__(self)
        self.log.info("nima,开始case的初始化")
        self.url = 'http://dev-api.gloryholiday.com/yuetu/search'
        self.data = '''
                        {
                            "Cid": "qunarytb",
                            "TripType": "1",
                            "FromCity": "hkg",
                            "ToCity": "icn",
                            "FromDate": "20190923",
                            "RetDate": "20190921",
                            "AdultNumber": 1,
                            "ChildNumber": 0,
                            "InfantNumber":0,
                            "GodPerspective":false
                        }'''


    def TestProcess(self):
        res = self.sendRequest(method='POST',url=self.url,data=self.data)
        if res:
            self.log.info('搜索成功，有返回')
            print(res)
        else:
            print(self.log.error('nothing'))

