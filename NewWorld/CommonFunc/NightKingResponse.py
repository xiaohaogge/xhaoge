# 此方法用于分解 night-king的response 返回，以便于后期使用方便；
# return 对象实例，以及可使用的相关属性，提取信息；

import json


class NightKingRes():

    def __init__(self,nightkingRes):

        self.nightkingResponse = json.loads(nightkingRes)
        self.nkBaseResponse = self.nightkingResponse['baseResponse']
        self.nkRouting = self.nightkingResponse['routing']
        self.nkTraceSpans = self.nightkingResponse['traceSpans']
        self.nkTraceTimes = self.nightkingResponse['traceTimes']


    def baseResponse(self,key):
        try:
            value = self.nkBaseResponse[key]
            if value or value == '':
                return value
            else:
                return "baseres something is woring"
        except Exception as e:
            return e


    def routing(self,key):
        try:
            value = self.nkRouting[key]
            if value or value == '':
                return value
            else:
                return "routing something is woring"
        except Exception as e:
            return e


    def traceSpans(self,key):
        try:
            value = self.nkTraceSpans[key]
            if value or value == '':
                return value
            else:
                return "traceSpans something is woring"
        except Exception as e:
            return e


    def traceTimes(self,key):
        try:
            value = self.nkTraceTimes[key]
            if value or value == '':
                return value
            else:
                return "traceTimes something is woring"
        except Exception as e:
            return e


    def routingBaseInfo(self,key):
        try:
            value = []
            for baseinfo in self.nkRouting[key]:
                value.append(baseinfo)

            if len(value) == 0:
                return 'routing 里面没有这个信息，或者为null，值：%s' % value
            return value
        except Exception as e:
            return e


    def routingItineraryInfo(self,key):
        self.routingIt
        try:
            value = []
            for baseinfo in self.nkRouting[key]:
                value.append(baseinfo)

            if len(value) == 0:
                return 'routing 里面没有这个信息，或者为null，值：%s' % value
            return value
        except Exception as e:
            return e

