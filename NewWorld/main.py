# 定义程序的主入口


from NewWorld.TestCase.Search.CaseSearch import CaseSearch0001

class GodMain(CaseSearch0001):

    def __init__(self):
        CaseSearch0001.__init__(self)
        pass





if __name__ == "__main__":
    IamGod = GodMain()
    IamGod.log.info("开始进入主阶段了哦！")
    IamGod.TestProcess()
    print('Game Over')
