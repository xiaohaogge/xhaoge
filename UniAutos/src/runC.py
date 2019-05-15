'''
    此文件作为该测试的程序入口，其余简述待完善；
'''

import time
import unittest
from UniAutos.src.CommonFunc.HTMLTestRunner import HTMLTestRunner
# from UniAutos.src.InterfaceFunc.Test_search import Mysearch
from UniAutos.src.InterfaceFunc.Test_ticket import Myticket

if __name__ == "__main__":
    # # unittest.main()
    # test_suite = unittest.TestSuite()  # 创建一个测试集合
    # test_suite.addTest(Mysearch('test01'))  # 测试套件中添加测试用例
    # # test_suite.addTest(unittest.makeSuite(MyTest))#使用makeSuite方法添加所有的测试方法
    # # 执行测试套件
    # unittest.main()
    print('Hello World')
    testunit = unittest.TestSuite()
    # 将测试用例加入到测试容器中
    testunit.addTest(Myticket("test01"))
    testunit.addTest(Myticket("test02"))
    testunit.addTest(Myticket("test03"))
    testunit.addTest(Myticket("test04"))
    testunit.addTest(Myticket("test05"))
    testunit.addTest(Myticket("test06"))
    testunit.addTest(Myticket("test07"))
    testunit.addTest(Myticket("test08"))
    # 获取当前时间，这样便于下面的使用。
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    # 打开一个文件，将result写入此file中
    with open(r"..\src\report\result" + now + ".html", 'wb') as fp:
        runner = HTMLTestRunner(stream=fp,
                                title='Nima的测试报告',
                                description=u'详细信息:'
                                )
        runner.run(testunit)

    # # 1、设置待执行用例的目录
    # test_dir = os.path.join(os.getcwd())
    #
    # # 2、自动搜索指定目录下的case，构造测试集,执行顺序是命名顺序：先执行test_add，再执行test_sub
    # discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
    #
    # # 实例化TextTestRunner类
    # runner = unittest.TextTestRunner()
    #
    # # 使用run()方法运行测试套件（即运行测试套件中的所有用例）
    # runner.run(discover)



