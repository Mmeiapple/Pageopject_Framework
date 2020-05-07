import os
import unittest
from common.log_print import Log
from common.get_config import getconfig
from common.base_page_info import BasePage
from common.browser import Browser


class SeleniumBaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        Log.logsinfo("=======测试类开始=======")
        cls.url=getconfig.geturl

    def setUp(self) -> None:
        self.basepage=BasePage(Browser('chrome').getdriver())
        self.basepage.waittime(10)
        self.basepage.openurl(self.url)
        self.basepage.setmaxbrowser()

    def test1(self):
        Log.logsinfo('测试用例1')

    def tearDown(self) -> None:
        self.basepage.timesleep(4)
        self.basepage.closebrowser()

    @classmethod
    def tearDownClass(cls) -> None:
        Log.logsinfo("=======测试类结束=======")


if __name__=="__main__":
    unittest.main(verbosity=2)