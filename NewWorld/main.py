# 定义程序的主入口


from NewWorld.Handle.DataController import DataControl

class GodMain(DataControl):

    def __init__(self):
        DataControl.__init__(self)


    def HappyGo(self):
        pass





if __name__ == "__main__":
    GodRun = GodMain()
    print(GodRun.log.info("开始进入主流程了哦！"))
    print('Game Over')
