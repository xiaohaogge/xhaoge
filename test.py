
import re

f = {"data": "039885ad-70a5-4fc7-9af4-16a21a648fad#e147456b-d03d-46c2-8ba0-7f4e8927e23a#KE854_E_KE795_E_KE766_E_KE859_E#1"}

str1 = f['data'][73:-2]

print(str1)



import time
from datetime import datetime
from AllBlue.TestCase.CaseBase.CommonFunc import GetTimeCurrency

t = time.time()
r = time.localtime()
c = time.asctime()
dt = datetime.now()
dd = dt.date()
de = str(dt.month)
print(type(de))
cc = dt.isoformat()
print(cc)

print(t)
print(r)
print(c)
print(dt)
print(dd)
print(de)

GetTimeCurrency(method=2)
