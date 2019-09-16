# 此文件用于定于一些公共方法；
import json


def checkGetCurrency(res,source='BOC',fromC='USD',toC='CNY'):
    '''定义getCurrency 接口的返回check，res 类型为字符串，接口响应数据；'''
    resp = json.loads(res)
    try:
        if resp['original_code']==fromC and resp['target_code']==toC:
            currencylist = resp['currencies']
            for c in currencylist:
                if c['status_code']==200 and c['source']==source:
                    return c['exchange_rate']
                else:
                    raise 404
    except Exception as e:
        return e


def checkExchangeRate(method=1,fromC='USD',toC='CNY',res=''):
    '''定义exchangeRate接口返回的check，res 类型为字符串，接口的响应数据；'''
    resp = json.loads(res)


