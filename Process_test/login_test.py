import os
from elementinfo.login_page import LoginPage
from selenium import webdriver

current = os.path.dirname(__file__)
webpath = os.path.join(current, '../webdriver/chromedriver.exe')

def login(driver,url='http://172.16.4.221/',username='admin',password='Hm123456'):
    driver=LoginPage(driver)
    driver.openurl(url)
    driver.waittime()
    driver.setmaxbrowser()
    driver.clickzaotao()
    driver.inputusername(username)
    driver.inputuserpassword(password)
    driver.clicklogin()
    return driver

if __name__=="__main__":
    dri=webdriver.Chrome(executable_path=webpath)
    a=login(dri)