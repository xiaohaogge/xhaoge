'''
    此文件用于一些parmesans的类的封装；
'''

class OTASearch:

    def __init__(self,paramete):
        self.adultNum = paramete['adultNum']  # 成人数；
        self.channel = paramete['channel']
        self.childNum = paramete['childNum']
        self.cid = paramete['cid']
        self.domain = paramete['domain']
        self.fromCity = paramete['fromCity']
        self.fromDate = paramete['fromDate']
        self.infantNum = paramete['infantNum']
        self.maxWaitTime = paramete['maxWaitTime']
        self.retDate = paramete['retDate']
        self.toCity = paramete['toCity']
        self.tripType = paramete['tripType']
        self.useCache = paramete['useCache']
        self.useFilter = paramete['useFilter']
        self.searchRatio = paramete['searchRatio']

    def searchKeyDict(self):
        searchKeyDict = {}
        searchKeyDict['adultNum'] = self.adultNum
        searchKeyDict['channel'] = self.channel
        searchKeyDict['childNum'] = self.childNum
        searchKeyDict['cid'] = self.cid
        searchKeyDict['domain'] = self.domain
        searchKeyDict['fromCity'] = self.fromCity
        searchKeyDict['fromDate'] = self.fromDate
        searchKeyDict['infantNum'] = self.infantNum
        searchKeyDict['maxWaitTime'] = self.maxWaitTime
        searchKeyDict['retDate'] = self.retDate
        searchKeyDict['toCity'] = self.toCity
        searchKeyDict['tripType'] = self.tripType
        searchKeyDict['useCache'] = self.useCache
        searchKeyDict['useFilter'] = self.useFilter
        searchKeyDict['searchRatio'] = self.searchRatio
        return searchKeyDict

d = '''
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
    } '''
