import os
import random
from common.base_page_info import BasePage
from Process_test import login_test
from selenium import webdriver
from elementinfo.organization_user_page import OraganizationUserPage
from elementinfo.organization_home_page import OraganizationHomePage
from common.element_data_utils import GetElementInfo
num=random.randint(1,1000)
class OraganizationUserAdduserPage(BasePage):
    def __init__(self,driver):
        super(OraganizationUserAdduserPage,self).__init__(driver)

# 添加用户页面
        elememnt=GetElementInfo('organization_user_adduser_page').getelementinfo()

#       用户名输入框
        self.username_input=elememnt['username_input']
        # 密码输入框
        self.userpassword_input=elememnt['userpassword_input']
        # 第二次密码输入框
        self.repeatpassword_input=elememnt['repeatpassword_input']
        # 真实姓名输入框
        self.realname_input=elememnt['realname_input']
        # 入职日期输入框
        self.entrydate_input = elememnt['entrydate_input']
        # 页面空白处
        self.clickpage_click=elememnt['clickpage_click']
        # 页面空白处

        # 职位选择
        self.Jobchoice_click = elememnt['Jobchoice_click']
        # 权限分组输入框选中
        self.rightsgroup_selected_click=elememnt['rightsgroup_selected_click']
        # 权限选中
        self.rightsgroup_click=elememnt['rightsgroup_click']
        # 邮箱输入框
        self.email_input = elememnt['email_input']
        # 源代码帐号输入框
        self.codeaccount_input = elememnt['codeaccount_input']
        # 性别按钮
        self.gender_button = elememnt['gender_button']
        # 密码校验输入框
        self.passwordchecking_input = elememnt['passwordchecking_input']
        # 保存按钮
        self.save_button = elememnt['save_button']


    def input_username_input(self,username):
        self.input(self.username_input,username)

    def input_userpassword_input(self,password):
        self.input(self.userpassword_input,password)

    def input_repeatpassword_input(self,password):
        self.input(self.repeatpassword_input,password)

    def input_realname_input(self,realname):
        self.input(self.realname_input,realname)

    def clear_entrydate_input(self):
        self.clear(self.entrydate_input)

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

    def clear_passwordchecking_input(self):
        self.clear(self.passwordchecking_input)

    def input_passwordchecking_input(self,passwordchecking):
        self.input(self.passwordchecking_input,passwordchecking)

    def click_save_button(self):
        self.click(self.save_button)

    def scroll_scrollbarelement(self):
        self.scrollbarelement(self.save_button)

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
    driver.input_userpassword_input('a.123456')
    driver.input_repeatpassword_input('a.123456')
    driver.input_realname_input('测试'+str(num))
    driver.clear_entrydate_input()
    driver.input_entrydate_input('2020-04-26')
    #点击页面空白处
    driver.click_clickpage_clickt()
    driver.click_Jobchoice_click()
    driver.click_rightsgroup_selected_click()
    driver.click_rightsgroup_click()
    driver.input_email_input('50534'+str(num)+'@qq.com')
    driver.input_codeaccount_input(str(num))
    driver.click_gender_button()
    driver.clear_passwordchecking_input()
    driver.input_passwordchecking_input('a12345678')
    driver.scroll_scrollbarelement()
    driver.click_save_button()




