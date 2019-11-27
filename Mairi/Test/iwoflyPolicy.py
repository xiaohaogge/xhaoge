
import requests
import json
import math

# 例如B端的价格为X，Y 为搜索时需要加的费用，
# 公式为：（X+Y）*（Commission的百分比+预收支付成本的百分比）+（Commission的数值金额+预收支付成本的数值金额）=Y
# Xp 票面价 Xt 税费；searchC 搜索币种，payC 支付币种；numP 人数
numP = 1
searchC = "KRW"
payC = "KRW"
Xp = 233320
Xt = 234858
X = Xp+Xt  
# 1014  5050.62677
# ===================platform policy============= 
# currency1 = from政策 commission数值币种 
# currency2 = from政策 预收支付数值币种
# comP=Commission的百分比; comV=Commission的数值金额;
comP = 0.018
comV = 0
currency1 = 'USD'
# receiveP=预收支付成本的百分比; receiveV=预收支付成本的数值金额;
receiveP = 0.01
receiveV = 0
currency2 = 'USD'

# ===================currency policy============= 
currencyP = 0
currencyV = 0
currency3 = "USD"

# ===================Pay policy============= 
# Y platform =加价值；
# payP 支付网关加价百分比 orderP 生单费用百分比； ratelossP 汇损百分比；
payP = 0.0431
orderP = 0
orderV = 0
currency4 = "USD"
ratelossP = 0.017
ratelossV = 0
currency5 = "USD"

def getcurrencyrate(fromC="USD",toC="USD"):
	url = "http://dev-restful-api.gloryholiday.com/nightking/exchangeRate?providerName=%22%22&cid=iwoflyCOM&originalCode={}&targetCode={}".format(fromC,toC)
	res = requests.get(url=url)
	rr = res.json()
	rate = rr["exchange_rate"]["exchange_rate"]
	print("from:%s to:%s 获取汇率为%s："%(fromC,toC,rate))
	return rate

def countCurrencyPolicy():
	rate = getcurrencyrate(fromC=searchC,toC=payC)
	print("例如B端的总价格为：",X)
	x1 = X * rate
	comV1 = comV * getcurrencyrate(fromC=currency1,toC=payC)
	receiveV1 = receiveV * getcurrencyrate(fromC=currency2,toC=payC)
	currencyV1 = currencyV * getcurrencyrate(fromC=currency3,toC=payC)
	
	# Y platform =加价值；
	Y = (x1*(comP+receiveP+currencyP)+numP*(comV1+receiveV1+currencyV1)) / (1-comP-receiveP-currencyP)
	# 最终search 对外报价；
	platformFinal = x1 + Y
	print("-------------------------------------")
	print("币种政策加价值为：",math.ceil(Y),"\n") 
	print("最终对外报价总计：",round(platformFinal,2),payC,"\n")
	print("-----------server policy-------------")
	orderV1 = orderV *getcurrencyrate(fromC=currency4,toC=payC)
	ratelossV1  = ratelossV *getcurrencyrate(fromC=currency5,toC=payC)
	
	# 总的加价值；
	Yall = (x1*(comP+currencyP+orderP+ratelossP+payP)+numP*(comV1+currencyV1+orderV1+ratelossV1))/(1-comP-currencyP-orderP-ratelossP-payP)
	# server服务费；
	Yserver = Yall - Y
	YserverCny = Yserver * getcurrencyrate(fromC=payC,toC=searchC)
	print("\n"+"总的加价值为：",round(Yall,2),payC,"\n")
	print("服务费用 为(支付币种)：",round(Yserver,2),payC,"\n")
	print("服务费用 为(搜索币种)：",round(YserverCny,2),searchC,"\n")
	print("生单以后总的对外报价为：",round(platformFinal+Yserver,2),payC,"\n")
	print("-------------------------------------")


countCurrencyPolicy()


