import os
import time
from common.base_page_info import BasePage
from selenium import webdriver
from elementinfo.organization_home_page import OraganizationHomePage
from Process_test.login_test import login
from common.element_data_utils import GetElementInfo

class OraganizationUserPage(BasePage):
    def __init__(self,driver):
        super(OraganizationUserPage,self).__init__(driver)
        # ---用户页面元素---

        # 添加用户按钮
        element_info=GetElementInfo('organization_user_page').getelementinfo()
        self.adduser_button = element_info['adduser_button']
        # 批量添加用户按钮
        self.addusers_button = element_info['addusers_button']
        # 全选按钮
        self.selection_button = element_info['selection_button']
        # 编辑用户按钮
        self.edituser_button = element_info['edituser_button']
        # 删除用户按钮
        self.deleteuser_button = element_info['deleteuser_button']
        # 取消删除按钮
        self.dismissdeleteuser_button = element_info['dismissdeleteuser_button']
        # 维护部门链接
        self.maintenancedepartment_link = element_info['maintenancedepartment_link']




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