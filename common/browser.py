import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


current=os.path.dirname(__file__)
chrome_driver_path=os.path.join(current,'../webdriver/chromedriver.exe')
firefox_driver_path=os.path.join(current,'../webdriver/geckodriver.exe')




class Browser(object):
    def __init__(self,drivername='chrome'):
        self.chromedriverpath=chrome_driver_path
        self.drivername=drivername
        self.firefoxdriverpath=firefox_driver_path

    def getdriver(self):
        if self.drivername.lower()=='chrome':
            return self.getchromebrowser()
        elif self.drivername.lower()=='firefox':
            return self.getfirefoxbrowser()

    def getchromebrowser(self):
        chrome_options=Options()
        # 谷歌浏览器可以加上这个属性来规避BUG
        chrome_options.add_argument('--disable-gpu')
        # 设置默认编码为utf-8
        chrome_options.add_argument('lang=zh_CN.UTF-8')
        # 取消chrome浏览器控制标语
        chrome_options.add_experimental_option('useAutomationExtension',False)
        # 取消chrome浏览器控制标语
        chrome_options.add_experimental_option('excludeSwitches',['enable-automation'])
        chrome_driver_path=os.path.join(self.chromedriverpath)
        driver=webdriver.Chrome(options=chrome_options,executable_path=chrome_driver_path)
        return driver


    def getfirefoxbrowser(self):
        firefox_driver_path=os.path.join(self.firefoxdriverpath)
        driver=webdriver.Firefox(executable_path=firefox_driver_path)
        return driver

if __name__=="__main__":
    Browser('firefox').getdriver()