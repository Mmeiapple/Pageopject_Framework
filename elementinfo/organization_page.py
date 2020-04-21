import os
from common.base_page_info import BasePage
from Process_test import login_test
from selenium import webdriver

class OraganizationPage(BasePage):
    def __init__(self,driver):
        super(OraganizationPage,self).__init__(driver)
        #一级目录链接
        self.organization_link={'element_name':'组织链接',
                                 'locator_type':'xpath',
                                 'locator_value':'//a[@href="/zentao/company/"]',
                                 'timeout':1}
        #二级目录链接
        self.user_link={'element_name':'用户链接',
                                 'locator_type':'xpath',
                                 'locator_value':'//a[@href="/zentao/company-browse.html"]',
                                 'timeout':1}
        self.department_link={'element_name':'部门链接',
                                 'locator_type':'xpath',
                                 'locator_value':'//a[@href="/zentao/dept-browse.html"]',
                                 'timeout':1}
        self.permissions_link={'element_name':'权限链接',
                                 'locator_type':'xpath',
                                 'locator_value':'//a[@href="/zentao/group-browse.html"]',
                                 'timeout':1}
        self.dynamic_link = {'element_name': '动态链接',
                                'locator_type': 'xpath',
                                'locator_value': '//a[@href="/zentao/company-dynamic.html"]',
                                'timeout': 1}
        self.company_link = {'element_name': '公司链接',
                                'locator_type': 'xpath',
                                'locator_value': '//a[@href="/zentao/company-view.html"]',
                                'timeout': 1}
        #用户页面元素
        self.adduser_button={'element_name': '添加用户按钮',
                              'locator_type': 'xpath',
                              'locator_value': '//div/div[3]/a[2]/i[@class="icon icon-plus"]',
                              'timeout': 1}
        self.addusers_button = {'element_name': '批量添加用户按钮',
                               'locator_type': 'xpath',
                               'locator_value': '//a[@href="/zentao/user-batchCreate-0.html"][contains(.,"批量添加用户")]',
                               'timeout': 1}
        self.selection_button={'element_name': '全选按钮',
                               'locator_type': 'xpath',
                               'locator_value': '//div[@title="全选"]',
                               'timeout': 1}
        self.edituser_button={'element_name': '编辑用户按钮',
                          'locator_type': 'xpath',
                          'locator_value': '//a[@href="/zentao/user-edit-4-company.html"]',
                           'timeout': 1}
        self.deleteuser_button={'element_name': '删除用户按钮',
                          'locator_type': 'xpath',
                          'locator_value': '//a[@href="/zentao/user-delete-20.html"]',
                           'timeout': 1}
        self.Maintenancedepartment_link={'element_name': '维护部门链接',
                                         'locator_type': 'xpath',
                                         'locator_value': '//a[@href="/zentao/dept-browse.html"]',
                                         'timeout': 1}
        self.Maintenancedepartment_link={'element_name': '维护部门链接',
                                         'locator_type': 'xpath',
                                         'locator_value': '//a[@href="/zentao/dept-browse.html"]',
                                         'timeout': 1}
        # 添加用户页面
        self.inputusername_input={'element_name': '输入用户名',
                                  'locator_type': 'xpath',
                                  'locator_value': '//input[@id="account"]',
                                  'timeout': 1}
        self.inputuserpassword_input={'element_name': '输入密码',
                                      'locator_type': 'xpath',
                                      'locator_value': '//input[@id="password1"]',
                                      'timeout': 1}
        self.inputresetpassword_input={'element_name': '第二次输入密码',
                                      'locator_type': 'xpath',
                                      'locator_value': '//input[@id="password2"]',
                                      'timeout': 1}



    def click_organization(self):
        self.click(self.organization_link)


if __name__=="__main__":
    current = os.path.dirname(__file__)
    webpath = os.path.join(current, '../webdriver/chromedriver.exe')
    dri=webdriver.Chrome(executable_path=webpath)
    login=login_test.login(dri)
    driver=OraganizationPage(dri)
    driver.click_organization()

