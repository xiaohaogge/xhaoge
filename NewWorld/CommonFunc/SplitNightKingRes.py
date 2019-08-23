# 此方法用于分解 night-king的response 返回，以便于后期使用方便；

import json


class NightKingRes():

    def __init__(self,nightking):
        self.nightking = json.loads(nightking)


    def baseResponse(self,key):
        try:
            value = self.nightking['baseResponse'][key]
            if value or value == '':
                return value
            else:
                return "baseres something is woring"
        except Exception as e:
            return e

    def routing(self,key):
        try:
            value = self.nightking['routing'][key]
            if value or value == '':
                return value
            else:
                return "routing something is woring"
        except Exception as e:
            return e

    def traceSpans(self,key):
        try:
            value = self.nightking['traceSpans'][key]
            if value or value == '':
                return value
            else:
                return "traceSpans something is woring"
        except Exception as e:
            return e

    def traceTimes(self,key):
        try:
            value = self.nightking['traceTimes'][key]
            if value or value == '':
                return value
            else:
                return "traceTimes something is woring"
        except Exception as e:
            return e


