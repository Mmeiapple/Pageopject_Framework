import os
from common.base_page_info import BasePage
from Process_test import login_test
from selenium import webdriver

class OraganizationHomePage(BasePage):
    def __init__(self,driver):
        super(OraganizationHomePage,self).__init__(driver)
        #一级目录链接
        self.organization_link={'element_name':'组织链接',
                                 'locator_type':'xpath',
                                 'locator_value':'//a[@href="/zentao3/www/company/"]',
                                 'timeout':1}
        #二级目录链接
        self.user_link={'element_name':'用户链接',
                                 'locator_type':'xpath',
                                 'locator_value':'//a[@href="/zentao3/www/company-browse.html"]',
                                 'timeout':1}
        self.department_link={'element_name':'部门链接',
                                 'locator_type':'xpath',
                                 'locator_value':'//a[@href="/zentao3/www/dept-browse.html"]',
                                 'timeout':1}
        self.permissions_link={'element_name':'权限链接',
                                 'locator_type':'xpath',
                                 'locator_value':'//a[@href="/zentao3/www/group-browse.html"]',
                                 'timeout':1}
        self.dynamic_link = {'element_name': '动态链接',
                                'locator_type': 'xpath',
                                'locator_value': '//a[@href="/zentao3/www/company-dynamic.html"]',
                                'timeout': 1}
        self.company_link = {'element_name': '公司链接',
                                'locator_type': 'xpath',
                                'locator_value': '//a[@href="/zentao3/www/company-view.html"]',
                                'timeout': 1}


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
        driver.click_organization_link()
        driver.click_department_link()
        driver.click_company_link()
        driver.click_dynamic_link()
        driver.click_department_link()
        driver.click_user_link()
    finally:
        driver.quitbrowsr()


