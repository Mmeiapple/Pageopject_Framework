import os
from selenium.webdriver.common.by import By
from selenium import webdriver
from common.base_page_info import BasePage
from common.log_print import Log
from common.element_data_utils import GetElementInfo
from common.element_data_yaml import GetElementInfoYaml
from common.browser import Browser
class LoginPage(BasePage):
    def __init__(self,driver):
        super(LoginPage,self).__init__(driver)
        element=GetElementInfo('login').getelementinfo('login_page')
        #获取元素定位信息
        self.caotao_button=element['caotao_button']
        self.username_inputbox=element['username_inputbox']
        self.userpassword_inputbox=element['userpassword_inputbox']
        self.login_button =element['login_button']
    #调用父类方法
    def clickzaotao(self):
        self.click(self.caotao_button)

    def inputusername(self,username):
        self.input(self.username_inputbox,username)

    def inputuserpassword(self,password):
        self.input(self.userpassword_inputbox,password)

    def clicklogin(self):
        self.click(self.login_button)

    def switch_accept(self):
        self.accept()


if __name__=="__main__":
    try:
        dri=Browser('chrome').getdriver()
        driver=LoginPage(dri)
        driver.openurl('http://106.53.50.202:8999/zentao3/www/user-login-L3plbnRhbzYvd3d3Lw==.html')
        driver.waittime()
        driver.setmaxbrowser()
        driver.inputusername('admin')
        driver.inputuserpassword('a12345678')
        driver.clicklogin()
        driver.waittime(2)
    finally:
        driver.quitbrowsr()
