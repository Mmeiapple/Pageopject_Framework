import os
from common.base_page_info import BasePage
from Process_test import login_test
from selenium import webdriver

class OraganizationUserAdduserPage(BasePage):
    def __init__(self,driver):
        super.__init__(driver)

# 添加用户页面
        self.inputusername_input={'element_name': '用户名输入框',
                                  'locator_type': 'xpath',
                                  'locator_value': '//input[@id="account"]',
                                  'timeout': 1}
        self.inputuserpassword_input={'element_name': '密码输入框',
                                      'locator_type': 'xpath',
                                      'locator_value': '//input[@id="password1"]',
                                      'timeout': 1}
        self.inputRepeatpassword_input={'element_name': '第二次密码输入框',
                                      'locator_type': 'xpath',
                                      'locator_value': '//input[@id="password2"]',
                                      'timeout': 1}
        self.inputrealname_input={'element_name': '真实姓名输入框',
                                  'locator_type': 'xpath',
                                  'locator_value': '//input[@id="realname"]',
                                   'timeout': 1}
        self.inputentrydate_input = {'element_name': '入职日期输入框',
                                    'locator_type': 'xpath',
                                    'locator_value': '//input[@id="join"]',
                                    'timeout': 1}
        self.clickpage_click={'element_name': '页面空白处',
                                    'locator_type': 'xpath',
                                    'locator_value': '//table[@class="table table-form"]',
                                    'timeout': 1}
        self.inputJobchoice_input = {'element_name': '职位选择输入框',
                                'locator_type': 'xpath',
                                'locator_value': '//option[@value="qa"]',
                                'timeout': 1}
        self.inputrightsgroup_input={'element_name': '权限分组输入框',
                                'locator_type': 'xpath',
                                'locator_value': '//div[@id="group_chosen"]',
                                'timeout': 1}
        self.inputemail_input = {'element_name': '邮箱输入框',
                                     'locator_type': 'xpath',
                                     'locator_value': '//input[@id="email"]',
                                     'timeout': 1}
        self.inputcodeaccount_input = {'element_name': '源代码帐号输入框',
                                     'locator_type': 'xpath',
                                     'locator_value': '//input[@id="commiter"]',
                                     'timeout': 1}
        self.gender_button = {'element_name': '性别按钮',
                                     'locator_type': 'xpath',
                                     'locator_value': '//input[@id="genderf"]',
                                     'timeout': 1}
        self.inputpasswordchecking_input = {'element_name': '密码校验输入框',
                                     'locator_type': 'xpath',
                                     'locator_value': '//input[@id="verifyPassword"]',
                                     'timeout': 1}
        self.savebutton_buttom = {'element_name': '保存按钮',
                                     'locator_type': 'xpath',
                                     'locator_value': '//button[@id="submit"]',
                                     'timeout': 1}