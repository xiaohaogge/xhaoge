# 定义程序的主入口


from AllBlue.Handle.Control import Controler

class GodMain(Controler):

    def __init__(self):
        print('Hello World!')
        Controler.__init__(self)



    def HappyGo(self):
        pass





if __name__ == "__main__":
    print('程序入口')
    GodRun = GodMain()
    print('程序结束.........................')
    GodRun.log.info('程序结束.........................')
