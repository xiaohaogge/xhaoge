# 定义一个所有测试用例的基类


import time
import logging
from AllBlue.CommonFunc.SendMethod import RunRequest

class AllBase(RunRequest):


    def __init__(self):
        self.log = logging
        myformat = '%(asctime)s---%(levelname)s-[line:%(lineno)d]---"message":%(message)s'
        timename = time.strftime("%Y-%m-%d-%I-%M-%S", time.localtime()) + "-MairiLog"
        filename = r'D:\program\logging\python\%s.txt' % timename

        self.log.basicConfig(
            # 设置告警级别为INFO
            # 自定义打印的格式
            # 将日志输出到指定的文件中
            # 以追加的方式将日志写入文件中，w是以覆盖写的方式哟
            level=logging.INFO,
            format=myformat,
            filename=filename,
            filemode='a'
        )

