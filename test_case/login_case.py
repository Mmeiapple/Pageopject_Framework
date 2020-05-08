import unittest
from action.login_action import LoginAction
from common.selenium_base_case import SeleniumBaseCase
from common.log_print import Log


class Logintest(SeleniumBaseCase):

    def setUp(self) -> None:
        """
        继承父类的setUp方法

        """

        super().setUp()

        """
        也可以在setUp方法中自定义功能,前提要写继承父类的方法 super().setUp()
        
        """
        Log.logsinfo('登录测试用例开始')

    def test_success_login(self):
        '''登录成功测试用例'''
        login_action=LoginAction(self.basepage.driver)
        main_page=login_action.suceseelogin('admin','a12345678')
        actual_result=main_page.get_username()
        self.assertEqual(actual_result,'admin','登录成功用例执行失败')

    def tearDown(self) -> None:

        """
        继承父类的tearDown方法

        """
        super().tearDown()

        Log.logsinfo('登录测试用例结束')


if __name__=="__main__":
    unittest.main(verbosity=1)