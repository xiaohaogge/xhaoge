'''
    Case Common Function 定义case 中使用的公共函数，以供调用；
'''
import json
import time
import random
from datetime import datetime
from AllBlue.Common.SendMethod import RunRequest
from AllBlue.Common.NightKingSearchResponse import NightKingSearchRes

# search case
def Test_RepoRule(res='', provider=''):
    '''定义获取repoIds 是否为空，result 值为true：repoIds不为空；值为false，repoIds为空；'''
    providerRoutings = Test_FindProviderRouting(res1=res, pro=provider)
    result = True
    for r in providerRoutings:
        if len(r['rule']['repoRule']['repoIds']) == 0:
            result = False
    return result


def Test_FindProviderRouting(res1='', pro=''):
    '''定义查找某一provider的所有航线报价'''
    resp = NightKingSearchRes(res1)
    routings = resp.nkRouting
    if pro == '':
        return routings
    providerList = []
    for i in routings:
        if i['providerName'] == pro:
            providerList.append(i)

    if len(providerList) == 0:
        raise Exception('not found provider routing,please check!')
    return providerList

# verify case




# order case



# currency case
def CheckListOnly(dataList):
    '''定义函数，传参一个list，return list中只含唯一值并且不为空字符串；'''
    result = []
    for i in dataList:
        if i != '' and i not in result:
            result.append(i)
    return result


def GetTimeCurrency(method=1, fromC='USD', toC='CNY', source='BOC',timeC='2019-09-26T00:00:00.123Z'):
    '''定义获取某个节点的汇率
        method=1，获取当前时间节点的某个汇率；method=2，获取某个时间的汇率；
    '''
    s = RunRequest()
    dt = datetime.now()
    cc =dt.isoformat()
    url = 'http://dev-restful-api.gloryholiday.com/currencyservice/getCurrency'
    data = {"originalCode": "USD", "targetCode": "CNY", "publishTimestamp": "2019-00-00T00:00:00.123Z"}
    data['originalCode'] = fromC
    data['targetCode'] = toC
    if method == 1:
        data['publishTimestamp'] = cc+"Z"
    if method == 2:
        data['publishTimestamp'] = timeC

    data = json.dumps(data)
    res = s.sendRequest(method='POST',url=url, data=data)
    resp = json.loads(res)
    sourcelist = resp['currencies']
    for s in sourcelist:
        if s['source'] == source and s['status_code']==200:
            return True,s
    return False,resp


# nothing
def GetRandomRoutingToVerify(cid='ctrip',resp=''):
    '''随机的最多拿5条航线去进行verify，return routing list'''
    result = []
    numlist = []
    if cid == 'ctrip':
        if resp['status'] != 0 and resp['msg'] != 'success':
            return  'response is fail status:%s,msg:%s'%(resp['status'],resp['msg'])
        try:
            for i in range(5):
                num = random.randint(0,len(resp['routings'])-1)
                numlist.append(num)
        except Exception:
            pass
        for n in numlist:
            result.append(resp['routings'][n])
    return result



