import os
from selenium.webdriver.common.by import By
from selenium import webdriver
from common.base_page_info import BasePage
from common.log_print import Log
class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.caotao_button={'element_name':'版本选择按钮',
                                 'locator_type':'xpath',
                                 'locator_value':'//a[@id="zentao"]',
                                 'timeout':1}
        self.username_inputbox={'element_name':'用户名输入框',
                                 'locator_type':'xpath',
                                 'locator_value':'//input[@id="account"]',
                                 'timeout':1}
        self.userpassword_inputbox={'element_name':'密码输入框',
                                    'locator_type':'xpath',
                                    'locator_value':'//input[@name="password"]',
                                    'timeout':1}
        self.login_button={ 'element_name':'登录按钮',
                            'locator_type':'xpath',
                            'locator_value':'//button[@id="submit"]',
                            'timeout':1}

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
        driver.openurl('http://172.16.4.221/')
        driver.waittime()
        driver.clickzaotao()
        driver.setmaxbrowser()
        driver.inputusername('admin')
        driver.inputuserpassword('Hm123456')
        driver.clicklogin()
    finally:
        driver.quitbrowsr()
