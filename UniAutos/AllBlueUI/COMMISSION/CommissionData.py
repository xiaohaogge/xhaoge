# conding = utf-8

#定义一个类，用于前返政策中的参数准备；

class ComsData():
    def __init__(self):
        self.number = '007'
        self.remark = "nothing"
        self.provider = "sabre-1list"
        self.validating = "MU,CA,MF,VJ,DL"
        self.faretype = "公布"
        self.triptype = "单程"
        self.fromCtiy = "US,BJS,JFK,HOU,WAS"
        self.toCity = "CN,HKG,TWD,SHA"
        self.fromExclude = "HOU,LAX"
        self.toExclude = "BJS,CKG,CAN"
        self.fromsegment = ""  # 去程航段
        self.tosegment = ""    # 回程航段
        self.transfer = ""     # 中转
        self.connection = ""   # 联运
        self.codeshare = ""    # 共享
        self.saledate = ['2019-07-23','2019-10-21']
        self.fromdate = []     # 去程日期
        self.todate = []       # 回程日期
        self.fblimit = ""      # farebasis 限制
        self.fbCTcy = "不限制"           # fb一致性
        self.RT = ["不适用"]        # 1/2RT   ["不适用","取高"]
        self.Qvalue = "包含"             # Q值包含
        self.cabinclass = ["商务","头等"]
        self.cabin = "*"
        self.ADT = [10,5]               # 成人百分比和数额
        self.CHD = [0,0]
        self.tax = [5,1,3]      # YQ,YR,UO


    pass
