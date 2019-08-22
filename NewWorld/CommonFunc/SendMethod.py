import requests
import json

class RunRequest:

    def post_main(self,url,data,header=None):
          if header !=None:
                res = requests.post(url=url,data=data,headers=header)
          else:
                res = requests.post(url=url,data=data)

          if res.status_code == 200:
              return res.json()
          else:
              return "search post response %s" % res.status_code

    def get_main(self,url,data=None,header=None):
         if header !=None:
             res = requests.get(url=url,data=data,headers=header,verify=False)
         else:
             res = requests.get(url=url,data=data,verify=False)
         if res.status_code == 200:
            return res.json()
         else:
            return "search get response %s" % res.status_code

    def sendRequest(self,method='POST',url=None,data=None,header=None):
         if method.upper() == 'POST':
             res = self.post_main(url,data,header)
         else:
             res = self.get_main(url,data,header)
         return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)