import os
from selenium.webdriver.common.by import By
from selenium import webdriver
from common.base_page_info import BasePage
from common.log_print import Log
from common.element_data_utils import GetElementInfo
from common.element_data_yaml import GetElementInfoYaml
class LoginPage(BasePage):
    def __init__(self,driver):
        super(LoginPage,self).__init__(driver)
        # self.caotao_button={'element_name':'版本选择按钮',
        #                          'locator_type':'xpath',
        #                          'locator_value':'//a[@id="zentao"]',
        #                          'timeout':1}
        # self.username_inputbox={'element_name':'用户名输入框',
        #                          'locator_type':'xpath',
        #                          'locator_value':'//input[@id="account"]',
        #                          'timeout':1}
        # self.userpassword_inputbox={'element_name':'密码输入框',
        #                             'locator_type':'xpath',
        #                             'locator_value':'//input[@name="password"]',
        #                             'timeout':1}
        # self.login_button={ 'element_name':'登录按钮',
        #                     'locator_type':'xpath',
        #                     'locator_value':'//button[@id="submit"]',
        #                     'timeout':1}
        # element=GetElementInfo('login_page').getelementinfo()
        # self.caotao_button=element['caotao_button']
        # self.username_inputbox=element['username_inputbox']
        # self.userpassword_inputbox=element['userpassword_inputbox']
        # self.login_button =element['login_button']
        element=GetElementInfoYaml().getelementinfo()
        self.caotao_button=element['login_page']['caotao_button']
        self.username_inputbox=element['login_page']['username_inputbox']
        self.userpassword_inputbox=element['login_page']['userpassword_inputbox']
        self.login_button =element['login_page']['login_button']

    def clickzaotao(self):
        self.click(self.caotao_button)

    def inputusername(self,username):
        self.input(self.username_inputbox,username)

    def inputuserpassword(self,password):
        self.input(self.userpassword_inputbox,password)

    def clicklogin(self):
        self.click(self.login_button)


if __name__=="__main__":
    try:
        current=os.path.dirname(__file__)
        webpath=os.path.join(current,'../webdriver/chromedriver.exe')
        dri=webdriver.Chrome(executable_path=webpath)
        driver=LoginPage(dri)
        driver.openurl('http://106.53.50.202:8999/zentao3/www/user-login-L3plbnRhbzYvd3d3Lw==.html')
        driver.waittime()
        driver.setmaxbrowser()
        driver.inputusername('admin')
        driver.inputuserpassword('a12345678')
        driver.clicklogin()
    finally:
        driver.quitbrowsr()
