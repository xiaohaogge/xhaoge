# 定义一个所有测试用例的基类


import os
import time
import logging
from AllBlue.Common.SendMethod import RunRequest
from AllBlue.Source.BaseConfig import BaseReadConfig

class AllBase(RunRequest,BaseReadConfig):


    def __init__(self):
        self.buildLog()


    def buildLog(self):
        self.startRead()
        self.log = logging
        myformat = '%(asctime)s--%(levelname)s--[%(funcName)s-line:%(lineno)d]---"message":%(message)s'
        timename = time.strftime("%Y-%m-%d-%I-%M-%S", time.localtime()) + "-AllBlueLog"
        filename = r'%s%s' % (self.logPath['log_path'],timename)+'.txt'

        if not os.path.exists(self.logPath['log_path']):
            os.makedirs(self.logPath['log_path'])

        self.log.basicConfig(
            # 设置告警级别为INFO
            # 自定义打印的格式
            # 将日志输出到指定的文件中
            # 以追加的方式将日志写入文件中，w是以覆盖写的方式哟
            level=logging.INFO,
            format=myformat,
            datefmt='%Y-%m/%d-%H:%M:%S',
            filename=filename,
            filemode='a'
        )

