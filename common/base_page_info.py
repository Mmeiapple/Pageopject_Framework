import os
import time
from selenium  import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from common.log_print import Log
class BasePage(object):
    def __init__(self,driver):
        driver=webdriver.Chrome()
        self.driver=driver

    #浏览器的基本操作
    def openurl(self,url):
        self.driver.get(url)
        Log.logsinfo('打开浏览器地址%s'%url)

    def waittime(self):
        self.driver.implicitly_wait(60)

    def setmaxbrowser(self):
        self.driver.maximize_window()

    def setmixbrowser(self):
        self.driver.minimize_window()

    def refulsbrowser(self):
        self.driver.refresh()

    def quitbrowsr(self):
        time.sleep(2)
        self.driver.quit()
        Log.logsinfo('退出浏览器--success')

    def closebrowser(self):
        self.driver.close()

    def gettitle(self):
        return self.driver.title()

    #定位元素

    def find_element(self,element_info):
        locator_type_name=element_info['locator_type']
        locator_value_info=element_info['locator_value']
        locator_timeout=element_info['timeout']
        if locator_type_name=='xpath':
            locator_type=By.XPATH
        elif locator_type_name=='class':
            locator_type=By.CLASS_NAME
        elif locator_type_name=='id':
            locator_type=By.ID
        elif locator_type_name=='selector':
            locator_type=By.CSS_SELECTOR
        elif locator_type_name=='link_text':
            locator_type=By.LINK_TEXT
        element=WebDriverWait(self.driver,locator_timeout).\
            until(lambda x:x.find_element(locator_type,locator_value_info))
        Log.logsinfo('识别元素【%s】--success' % element_info['element_name'])
        return element


    #元素操作方法
    def click(self,element_info):
        elment=self.find_element(element_info)
        elment.click()
        Log.logsinfo('【%s】进行点击'%element_info['element_name'])

    def input(self,element_info,content):
        elment=self.find_element(element_info)
        elment.send_keys(content)
        Log.logsinfo('对【%s】输入内容【%s】'%(element_info['element_name'],content))


    #页面布局操作方法

    def switchframe(self,element_info):
        element=self.find_element(element_info)
        self.driver.switch_to.frame(element)
        Log.logsinfo('切入框架--【%s】'%element_info['element_name'])

    def quitframe(self):
        self.driver.switch_to.default_content()
        Log.logsinfo('切回默认框架')


