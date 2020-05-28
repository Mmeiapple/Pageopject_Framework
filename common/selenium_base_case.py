import os
import unittest
from common.log_print import Log
from common.get_config import getconfig
from common.base_page_info import BasePage
from common.browser import Browser


class SeleniumBaseCase(unittest.TestCase):

    '''
    封装一个setUp类方法

    '''
    @classmethod
    def setUpClass(cls) -> None:
        Log.logsinfo("=======测试类开始=======")
        cls.url=getconfig.geturl

    """
    封装一个初始化测试工作方法
    
    """

    def setUp(self) -> None:
        self.basepage=BasePage(Browser('chrome').getdriver())
        self.basepage.waittime(10)
        self.basepage.openurl(self.url)
        self.basepage.setmaxbrowser()

    """
    封装一个结束测试工作方法

    """

    def tearDown(self) -> None:
        # 测试用例失败截图
        errors = self._outcome.errors
        for test, exc_info in errors:
            if exc_info:
                self.basepage.timesleep()
                self.basepage.screenshot_as_file()
        self.basepage.timesleep(3)
        self.basepage.closebrowser()
        Log.logsinfo('---------测试方法执行完毕-----------')

    """
    封装一个tearDown类方法

    """
    @classmethod
    def tearDownClass(cls) -> None:


        Log.logsinfo("=======测试类结束=======")

if __name__=="__main__":
    unittest.main(verbosity=2)