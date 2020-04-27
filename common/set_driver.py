import os
from selenium import webdriver

current = os.path.dirname(__file__)
webpath = os.path.join(current, '../webdriver/chromedriver.exe')

def SetDriver():
    driver=webdriver.Chrome(executable_path=webpath)
    driver.implicitly_wait(20)
    driver.maximize_window()
    return driver