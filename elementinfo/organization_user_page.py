import os
import time
from common.base_page_info import BasePage
from selenium import webdriver
from elementinfo.organization_home_page import OraganizationHomePage
from Process_test.login_test import login

class OraganizationUserPage(BasePage):
    def __init__(self,driver):
        super(OraganizationUserPage,self).__init__(driver)
        # 用户页面元素
        self.adduser_button = {'element_name': '添加用户按钮',
                               'locator_type': 'xpath',
                               'locator_value': '//div/div[3]/a[2]/i[@class="icon icon-plus"]',
                               'timeout': 1}
        self.addusers_button = {'element_name': '批量添加用户按钮',
                                'locator_type': 'xpath',
                                'locator_value': '//a[@class="btn btn-secondary"]',
                                'timeout': 1}
        self.selection_button = {'element_name': '全选按钮',
                                 'locator_type': 'xpath',
                                 'locator_value': '//div[@title="全选"]',
                                 'timeout': 1}
        self.edituser_button = {'element_name': '编辑用户按钮',
                                'locator_type': 'xpath',
                                'locator_value': '//form/table/tbody/tr[2]/td[11]/a[1]/i[@class="icon-common-edit icon-edit"]',
                                'timeout': 1}
        self.deleteuser_button = {'element_name': '删除用户按钮',
                                  'locator_type': 'xpath',
                                  'locator_value': '//table/tbody/tr[3]/td[11]/a[2]/i[@class="icon-trash"]',
                                  'timeout': 1}
        self.dismissdeleteuser_button = {'element_name': '取消删除按钮',
                                  'locator_type': 'xpath',
                                  'locator_value': '//div/div/div/button[@class="close"]',
                                  'timeout': 1}
        self.maintenancedepartment_link = {'element_name': '维护部门链接',
                                           'locator_type': 'xpath',
                                           'locator_value': '//a[@class="btn btn-info btn-wide"][text()="维护部门"]',
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
    def click_dismissdeleteuser_button(self):
        self.click(self.dismissdeleteuser_button)

    def click_maintenancedepartment_link(self):
        self.click(self.maintenancedepartment_link)
if __name__=='__main__':
    try:
        current=os.path.dirname(__file__)
        webpath=os.path.join(current,'../webdriver/chromedriver.exe')
        dri=webdriver.Chrome(executable_path=webpath)
        driver1=OraganizationHomePage(dri)
        loginin=login(dri)
        driver1.click_organization_link()
        driver=OraganizationUserPage(dri)
        driver.click_adduser()
        time.sleep(2)
        driver.back()
        driver.click_addusers()
        time.sleep(2)
        driver.back()
        driver.click_deleteuser_button()
        time.sleep(2)
        driver.click_dismissdeleteuser_button()
        time.sleep(2)
        driver.click_selection_button()
        time.sleep(2)
        driver.click_selection_button()
        time.sleep(2)
        driver.click_maintenancedepartment_link()
        time.sleep(2)
        driver.back()
        driver.click_edituser_button()
    finally:
        time.sleep(3)
        driver.quitbrowsr()