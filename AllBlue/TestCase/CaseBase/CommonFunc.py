''' Case Common
    定义case 中使用的公共函数，以供调用；
'''

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
    result = []
    for i in dataList:
        if i != '' and i not in result:
            result.append(i)
    return result