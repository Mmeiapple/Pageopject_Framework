import os
from elementinfo.login_page import LoginPage
from common.set_driver import SetDriver
from common.get_config import getconfig
from common.browser import Browser

current = os.path.dirname(__file__)
webpath = os.path.join(current, '../webdriver/chromedriver.exe')

def login(driver,url=getconfig.geturl,username='admin',password='a12345678'):
    driver=LoginPage(driver)
    driver.openurl(url)
    driver.inputusername(username)
    driver.inputuserpassword(password)
    driver.clicklogin()
    return driver

if __name__=="__main__":
    dri=Browser('chrome').getdriver()
    a=login(dri)