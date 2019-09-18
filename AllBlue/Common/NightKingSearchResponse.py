# 此方法用于分解 night-king的response 返回，以便于后期使用方便；
# return 对象实例，以及可使用的相关属性，提取信息；

import json
from AllBlue.Common.Base import AllBase

class NightKingRes():

    def __init__(self,nightkingRes):
        # self.log.info('开始进行nightkingres的初始化')
        self.nightkingResponse = json.loads(nightkingRes)
        self.nkBaseResponse = self.nightkingResponse['baseResponse']
        self.nkRouting = self.nightkingResponse['routing']
        self.nkTraceSpans = self.nightkingResponse['traceSpans']
        self.nkTraceTimes = self.nightkingResponse['traceTimers']


    # 定义获取response中的基本信息，return value
    def baseResponse(self,key):
        try:
            print('是不是进来了,baseresponse')
            basevalue = self.nkBaseResponse[key]
            if basevalue or basevalue == '':
                return basevalue
            else:
                return "baseres something is woring"
        except Exception as e:
            print('nima   获取失败了')

    # 定义获取routing中某个字段的信息；return value
    def routing(self):
        pass
        try:
            routingvalue = self.nkRouting
            if routingvalue or routingvalue == '':
                return routingvalue
            else:
                return "routing something is woring"
        except Exception as e:
            return e

    # 定义获取tracespans的基本信息；return list
    def traceSpans(self,key):
        try:
            Spansvalue = self.nkTraceSpans[key]
            if Spansvalue or Spansvalue == '':
                return Spansvalue
            else:
                return "traceSpans something is woring"
        except Exception as e:
            return e

    # 定义获取tracetimes中的基本信息，return list
    def traceTimers(self,key):
        try:
            Timesvalue = self.nkTraceTimes[key]
            if Timesvalue or Timesvalue == '':
                return Timesvalue
            else:
                return "traceTimes something is woring"
        except Exception as e:
            return e

    # 定义获取routing中的基本信息；return value list
    def routingBaseInfo(self,key):
        try:
            RouBasevalue = []
            for baseinfo in self.nkRouting:
                valueInfo = baseinfo[key]
                RouBasevalue.append(valueInfo)

            if len(RouBasevalue) == 0:
                return 'routing 里面没有这个信息，或者为null，值：%s' % RouBasevalue
            return RouBasevalue
        except Exception as e:
            return e

    # 定义一个函数，方便获取routing中第一个航线信息；
    def routingFirstBaseInfo(self,key):
        try:
            firstInfo = self.nkRouting[0]
            val = firstInfo[key]
            return val
        except Exception as e:
            return e

    # 定义获取Itinerary中的信息；return value list
    def routingItineraryBaseInfo(self,key):
        self.Itinerary = self.nkRouting['itinerary']
        try:
            RouItinevalue = []
            for Itineinfo in self.Itinerary[key]:
                RouItinevalue.append(Itineinfo)

            if len(RouItinevalue) == 0:
                return 'routing 里面没有这个信息，或者为null，值：%s' % RouItinevalue
            return RouItinevalue
        except Exception as e:
            return e

    # 定义获取currencyConversions list信息；return value list
    def routingCurrencyConversionsInfo(self):
        self.CurrencyConversion = self.nkRouting['currencyConversions']
        pass

    # 定义从segment中获取flight信息；return value list
    def routingItinerarySegmentInfo(self):
        pass

