# 定义程序的主入口


from NewWorld.TestCase.Search.Case_Search_KeyValue_0001 import Case_Search_KeyValue_0001

class GodMain(Case_Search_KeyValue_0001):

    def __init__(self):
        Case_Search_KeyValue_0001.__init__(self)





if __name__ == "__main__":
    GodRun = GodMain()
    print(GodRun.log.info("开始进入主流程了哦！"))
    GodRun.TestProcess()
    print('Game Over')
