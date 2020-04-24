import os
from common.base_page_info import BasePage
from Process_test import login_test
from selenium import webdriver

class OraganizationUserPage(BasePage):
    def __init__(self,driver):
        super.__init__(driver)
        # 用户页面元素
        self.adduser_button = {'element_name': '添加用户按钮',
                               'locator_type': 'xpath',
                               'locator_value': '//div/div[3]/a[2]/i[@class="icon icon-plus"]',
                               'timeout': 1}
        self.addusers_button = {'element_name': '批量添加用户按钮',
                                'locator_type': 'xpath',
                                'locator_value': '//a[@href="/zentao/user-batchCreate-0.html"][contains(.,"批量添加用户")]',
                                'timeout': 1}
        self.selection_button = {'element_name': '全选按钮',
                                 'locator_type': 'xpath',
                                 'locator_value': '//div[@title="全选"]',
                                 'timeout': 1}
        self.edituser_button = {'element_name': '编辑用户按钮',
                                'locator_type': 'xpath',
                                'locator_value': '//a[@href="/zentao/user-edit-4-company.html"]',
                                'timeout': 1}
        self.deleteuser_button = {'element_name': '删除用户按钮',
                                  'locator_type': 'xpath',
                                  'locator_value': '//a[@href="/zentao/user-delete-20.html"]',
                                  'timeout': 1}
        self.maintenancedepartment_link = {'element_name': '维护部门链接',
                                           'locator_type': 'xpath',
                                           'locator_value': '//a[@href="/zentao/dept-browse.html"]',
                                           'timeout': 1}
    def click_adduser(self):
        self.click(self.adduser_button)

    def click_addusers(self):
        self.click(self.addusers_button)

    def click_selection_button(self):
        self.click(self.selection_button)

    def click_edituser_button(self):
        self.click(self.edituser_button)

    def click_selection_button(self):
        self.click(self.selection_button)

    def click_deleteuser_button(self):
        self.click(self.deleteuser_button)

    def click_maintenancedepartment_link(self):
        self.click(self.maintenancedepartment_link)