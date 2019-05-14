import requests
import json

class RunRequest:
    def __init__(self,method,url,data=None,header=None):
        self.method = method
        self.url = url
        self.data = data
        self.header = header

    def post_main(self,url,data,header=None):
          if header !=None:
             r = requests.post(url=url,data=data,headers=header)
          else:
             r = requests.post(url=url,data=data)
          return r.json()

    def get_main(self,url,data=None,header=None):
         if header !=None:
             r = requests.get(url=url,data=data,headers=header,verify=False)
         else:
             r = requests.get(url=url,data=data,verify=False)
         return r.json()

    def sendRequest(self):
         if self.method.upper() == 'POST':
             res = self.post_main(self.url,self.data,self.header)
         elif self.method.upper() == 'GET':
             res = self.get_main(self.url,self.data,self.header)
         else:
             res = '请求方式不正确或未定义，请重新确认；'
         return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)