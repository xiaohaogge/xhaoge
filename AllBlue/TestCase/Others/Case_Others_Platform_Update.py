# Currency Rate
# 此case用于并发进行监控余额扣款测试；

import json
from AllBlue.TestCase.AllCaseBase import CaseBase


class Case_Others_Platform_Update(CaseBase):

    def __init__(self):
        CaseBase.__init__(self)
        self.log.info("===Case_Others_Platform_Update,测试开始===")


    def TestProcess(self):
        name = '去哪儿商旅哈哈'.encode('GBK')
        url0 = 'https://allblue.gloryholiday.com/api/marineford/ppConfig/platform/update'
        data0 = '''
                {"ticketDeadline":[{"beforeDepartureAtLeast":0,"beforeDepartureAtMost":0,"ticketDeadline":0}],
                "verifyPriceChanges":[{"minChange":0,"maxChange":0,"returnType":"ORIGINAL_PRICE"},{"minChange":0,"maxChange":0,"returnType":"NEW_PRICE"},{"minChange":0,"maxChange":0,"returnType":"FAILED"}],
                "orderPriceChanges":[{"minChange":0,"maxChange":0,"returnType":"ORIGINAL_PRICE"},{"minChange":0,"maxChange":0,"returnType":"NEW_PRICE"},{"minChange":0,"maxChange":0,"returnType":"FAILED"}],
                "payPriceChanges":[{"minChange":0,"maxChange":0,"returnType":"ORIGINAL_PRICE"},{"minChange":0,"maxChange":0,"returnType":"NEW_PRICE"},{"minChange":0,"maxChange":0,"returnType":"FAILED"}],
                "recentFlightFilters":[{"blockingTimes":["1300/1400","1700/1800"],"timeBeforeDeparture":24},{"blockingTimes":["1550/1600"],"timeBeforeDeparture":96},{"blockingTimes":["0800/1900"],"timeBeforeDeparture":48}],"aircraftFilters":[],
                "baseInfo":{"id":"5d3fee6db8d7ea000165e374","revision":27,"displayNumber":"PFC1907306359","archived":false,"enabled":true,"creator":"root","createdAt":"2019-09-22 17:17","traceId":"","policyNumber":""},"platformInfo":{"name":"去哪儿商旅哈哈","subsite":"qunarytb","cid":"qunarytb"},
                "description":"","priceComment":"","ticketInvoiceType":"OVERSEAS_ELECTRONIC_ITINERARY","segmentSplicing":false,"itinerarySplicing":false,"departureTimeFilter":0,"minConnectionMinute":90,"ruleInconsistent":"INTERCEPT",
                "baggageInconsistent":"INTERCEPT","searchTimeLimit":30,"childPriceHigherThanAdultPrice":true,"reuseFareRule":false,"verifyTimeLimit":0,"orderTimeLimit":0,"status":"ONLINE","id":"5d3fee6db8d7ea000165e374","revision":27,
                "displayNumber":"PFC1907306359","archived":false,"enabled":true,"creator":"root","createdAt":"2019-09-22 17:17","traceId":"","policyNumber":""}
                '''.encode('GBK')

        rr = self.sendRequest(url=url0, data=data0)
        print("rr:",rr)
        self.log.info(rr)

    def TestResult(self):
        self.log.info('===Case_Others_Platform_Update,测试完毕===')
        if self.flag:
            self.log.info('=========Case_Others_Platform_Update,测试通过')
            print("测试结果很成功，perfect！")
        else:
            self.log.error('=========Case_Others_Platform_Update,测试失败')








