import os
import random
from common.base_page_info import BasePage
from Process_test import login_test
from selenium import webdriver
from elementinfo.organization_user_page import OraganizationUserPage
from elementinfo.organization_home_page import OraganizationHomePage
num=random.randint(1,1000)
class OraganizationUserAdduserPage(BasePage):
    def __init__(self,driver):
        super(OraganizationUserAdduserPage,self).__init__(driver)

# 添加用户页面
        self.username_input={'element_name': '用户名输入框',
                                  'locator_type': 'xpath',
                                  'locator_value': '//input[@id="account"]',
                                  'timeout': 1}
        self.userpassword_input={'element_name': '密码输入框',
                                      'locator_type': 'xpath',
                                      'locator_value': '//input[@id="password1"]',
                                      'timeout': 1}
        self.repeatpassword_input={'element_name': '第二次密码输入框',
                                      'locator_type': 'xpath',
                                      'locator_value': '//input[@id="password2"]',
                                      'timeout': 1}
        self.realname_input={'element_name': '真实姓名输入框',
                                  'locator_type': 'xpath',
                                  'locator_value': '//input[@id="realname"]',
                                   'timeout': 1}
        self.entrydate_input = {'element_name': '入职日期输入框',
                                    'locator_type': 'xpath',
                                    'locator_value': '//input[@id="join"]',
                                    'timeout': 1}
        self.clickpage_click={'element_name': '页面空白处',
                                    'locator_type': 'xpath',
                                    'locator_value': '//table[@class="table table-form"]',
                                    'timeout': 1}
        self.Jobchoice_click = {'element_name': '职位选择',
                                'locator_type': 'xpath',
                                'locator_value': '//option[@value="qa"]',
                                'timeout': 1}
        self.rightsgroup_selected_click={'element_name': '权限分组输入框选中',
                                'locator_type': 'xpath',
                                'locator_value': '//div[@id="group_chosen"]',
                                'timeout': 1}
        self.rightsgroup_click={'element_name': '权限分组选择',
                                'locator_type': 'xpath',
                                'locator_value': '//div[@class="chosen-drop chosen-auto-max-width chosen-no-wrap in"]/ul/li[@title="研发"]',
                                'timeout': 1}
        self.email_input = {'element_name': '邮箱输入框',
                                     'locator_type': 'xpath',
                                     'locator_value': '//input[@id="email"]',
                                     'timeout': 1}
        self.codeaccount_input = {'element_name': '源代码帐号输入框',
                                     'locator_type': 'xpath',
                                     'locator_value': '//input[@id="commiter"]',
                                     'timeout': 1}
        self.gender_button = {'element_name': '性别按钮',
                                     'locator_type': 'xpath',
                                     'locator_value': '//input[@id="genderf"]',
                                     'timeout': 1}
        self.passwordchecking_input = {'element_name': '密码校验输入框',
                                     'locator_type': 'xpath',
                                     'locator_value': '//input[@id="verifyPassword"]',
                                     'timeout': 1}
        self.save_button = {'element_name': '保存按钮',
                                     'locator_type': 'xpath',
                                     'locator_value': '//button[@id="submit"]',
                                     'timeout': 1}

    def input_username_input(self,username):
        self.input(self.username_input,username)

    def input_userpassword_input(self,password):
        self.input(self.username_input,password)

    def input_repeatpassword_input(self,password):
        self.input(self.repeatpassword_input,password)

    def input_realname_input(self,realname):
        self.input(self.realname_input,realname)

    def input_entrydate_input(self,time):
        self.input(self.entrydate_input,time)

    def click_clickpage_clickt(self):
        self.click(self.clickpage_click)

    def click_Jobchoice_click(self):
        self.click(self.Jobchoice_click)

    def click_rightsgroup_selected_click(self):
        self.click(self.rightsgroup_selected_click)

    def click_rightsgroup_click(self):
        self.click(self.rightsgroup_click)

    def input_email_input(self,email):
        self.input(self.email_input,email)


    def input_codeaccount_input(self,codeaccount):
        self.input(self.codeaccount_input,codeaccount)

    def click_gender_button(self):
        self.click(self.gender_button)

    def input_passwordchecking_input(self,passwordchecking):
        self.input(self.passwordchecking_input,passwordchecking)


    def click_save_button(self):
        self.click(self.save_button)

if __name__=="__main__":
    current = os.path.dirname(__file__)
    webpath = os.path.join(current, '../webdriver/chromedriver.exe')
    dri = webdriver.Chrome(executable_path=webpath)
    loginin=login_test.login(dri)
    homelement=OraganizationHomePage(dri)
    homelement.click_organization_link()
    userelement=OraganizationUserPage(dri)
    userelement.click_adduser()
    driver=OraganizationUserAdduserPage(dri)
    driver.input_username_input('test'+str(num))