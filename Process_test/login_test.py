import os
from elementinfo.login_page import LoginPage
from selenium import webdriver
from common.element_data_utils import GetElementInfo

current = os.path.dirname(__file__)
webpath = os.path.join(current, '../webdriver/chromedriver.exe')

def login(driver,url='http://106.53.50.202:8999/zentao3/www/my/',username='admin',password='a12345678'):
    driver=LoginPage(driver)
    driver.openurl(url)
    driver.waittime()
    driver.setmaxbrowser()
    driver.inputusername(username)
    driver.inputuserpassword(password)
    driver.clicklogin()
    return driver

if __name__=="__main__":
    dri=webdriver.Chrome(executable_path=webpath)
    a=login(dri)