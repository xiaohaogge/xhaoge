# 定义程序的主入口


from AllBlue.Suite.Handler import Controler

class GodMain(Controler):

    def __init__(self):
        print('Hello World!')
        Controler.__init__(self)



    def HappyGo(self):
        print("What Should I Do?")





if __name__ == "__main__":
    GodRun = GodMain()
    GodRun.log.info('程序结束.........................')
