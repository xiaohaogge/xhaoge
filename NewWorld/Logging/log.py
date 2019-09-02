# logging模块定义

import time
import logging
import logging.handlers

myformat = '%(asctime)s---%(levelname)s-[line:%(lineno)d]---"message":%(message)s'
timename = time.strftime("%Y-%m-%d-%I-%M-%S", time.localtime())+"-MairiLog"
filename = r'F:\Program\Logging\yuetu\%s.txt' % timename

logging.basicConfig(
    #设置告警级别为INFO
    #自定义打印的格式
    #将日志输出到指定的文件中
    #以追加的方式将日志写入文件中，w是以覆盖写的方式哟
    level=logging.INFO,
    format=myformat,
    filename=filename,
    filemode='a'
)


logging.info("这是一个info的log")
logging.error("这是一个error的log")
logging.info("这又是一个info的log")

class Mylog():

    def __init__(self,name):
        timename = time.strftime("%Y-%m-%d-%I-%M-%S", time.localtime()) + "-mairilog"
        self.path = r'F:\Program\Logging\yuetu\%s.txt' % timename
        self.name = name
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(logging.INFO)
        self.ch = logging.StreamHandler()
        gs = logging.Formatter('%(asctime)s---%(levelname)s-[line:%(lineno)d]---"message":%(message)s')
        self.ch.setLevel(gs)
        self.fh = logging.handlers.TimedRotatingFileHandler
        self.format = logging
        pass