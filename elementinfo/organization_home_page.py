import os
from Process_test import login_test
from selenium import webdriver
from common.base_page_info import BasePage
from common.element_data_utils import GetElementInfo

class OraganizationHomePage(BasePage):
    def __init__(self,driver):
        super(OraganizationHomePage,self).__init__(driver)

        #二级目录链接
        element=GetElementInfo('organization').getelementinfo('home_page')
        self.organization_link=element['organization_link']
        self.user_link=element['user_link']
        self.department_link=element['department_link']
        self.permissions_link=element['permissions_link']
        self.dynamic_link = element['dynamic_link']
        self.company_link = element['company_link']


    def click_organization_link(self):
        self.click(self.organization_link)

    def click_user_link(self):
        self.click(self.user_link)

    def click_department_link(self):
        self.click(self.department_link)

    def click_dynamic_link(self):
        self.click(self.dynamic_link)

    def click_company_link(self):
        self.click(self.company_link)


if __name__=="__main__":
    try:
        current = os.path.dirname(__file__)
        webpath = os.path.join(current, '../webdriver/chromedriver.exe')
        dri=webdriver.Chrome(executable_path=webpath)
        login=login_test.login(dri)
        driver=OraganizationHomePage(dri)
        #点击组织连接
        driver.click_organization_link()
        #点击部门连接
        driver.click_department_link()
        #点击公司连接
        driver.click_company_link()
        #点击动态连接
        driver.click_dynamic_link()
        #点击动态连接
        driver.click_department_link()
        #点击用户连接
        driver.click_user_link()
    finally:
        driver.quitbrowsr()


