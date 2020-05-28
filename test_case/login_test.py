import unittest
from action.login_action import LoginAction
from common.selenium_base_case import SeleniumBaseCase
from common.log_print import Log
from common.test_data_utils import TestDataUtils


class Logintest(SeleniumBaseCase):

    def setUp(self) -> None:

        """
        继承父类的setUp方法

        """
        super().setUp()
        self.test_class_data=TestDataUtils('login_suite','LoginTest').convert_exceldata_to_testdata()

        """
        也可以在setUp方法中自定义功能,前提要写继承父类的方法 super().setUp()
        
        """
        Log.logsinfo('登录测试用例开始')

    def test_success_login(self):
        test_function_data=self.test_class_data['test_login_success']
        self._testMethodDoc=test_function_data['test_name']
        login_action=LoginAction(self.basepage.driver)
        main_page=login_action.suceseelogin(test_function_data['test_parameter'].get('username'),test_function_data['test_parameter'].get('password'))
        actual_result=main_page.get_username()
        self.assertEqual(actual_result,test_function_data['excepted_result'],'登录成功用例执行失败')

    def test_fail_login(self):
        test_function_data=self.test_class_data['test_login_fail']
        self._testMethodDoc = test_function_data['test_name']
        login_action=LoginAction(self.basepage.driver)
        actual_result=login_action.faillogin(test_function_data['test_parameter'].get('username'),test_function_data['test_parameter'].get('password'))
        self.assertEqual(actual_result,test_function_data['excepted_result'],'验证错误的用户名和密码能否成功处理执行失败')
    def tearDown(self) -> None:

        """
        继承父类的tearDown方法

        """
        super().tearDown()

        Log.logsinfo('登录测试用例结束')


if __name__=="__main__":
    unittest.main(verbosity=2)