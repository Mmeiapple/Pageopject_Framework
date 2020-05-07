import os
import time
from selenium  import webdriver
from common.get_config import getconfig
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.log_print import Log
class BasePage(object):
    def __init__(self,driver):
        # driver=webdriver.Chrome()
        self.driver=driver

    #浏览器的基本操作
    def openurl(self,url):
        self.driver.get(url)
        Log.logsinfo('打开浏览器地址%s--success'%url)

    def waittime(self,time=getconfig.gettimeout):
        self.driver.implicitly_wait(time)


    def timesleep(self,second=3):
        time.sleep(second)

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

    def back(self):
        self.driver.back()
        Log.logsinfo('返回上一页--success')

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
        Log.logsinfo('识别元素【%s】' % element_info['element_name'])
        return element


    #元素操作方法
    def click(self,element_info):
        element=self.find_element(element_info)
        element.click()
        Log.logsinfo('【%s】进行点击--success'%element_info['element_name'])

    def input(self,element_info,content):
        elment=self.find_element(element_info)
        elment.send_keys(content)
        Log.logsinfo('对【%s】输入内容【%s】--success'%(element_info['element_name'],content))

    def submit(self,element_info):
        element=self.find_element(element_info)
        element.submit()
        Log.logsinfo('【%s】表单提交--success' % element_info['element_name'])


    def clear(self,element_info):
        element=self.find_element(element_info)
        element.clear()



    """
    获取文本信息
    
    """

    def get_text(self,element_info):
        element=self.find_element(element_info)
        return element.text


    """
    frame框架操作
    
    """
    def switchframe(self,element_info):
        element=self.find_element(element_info)
        self.driver.switch_to.frame(element)
        Log.logsinfo('切入框架--【%s】--success'%element_info['element_name'])

    def quitframe(self):
        self.driver.switch_to.default_content()
        Log.logsinfo('切回默认框架--success')


    """
    
    句柄操作
    
    """

    def get_current_window_handle(self):
        return self.driver.current_window_handle

    def switch_window_by_handle(self,windowhandle):
        self.driver.switch_to.window(windowhandle)

    def switch_window_by_tiele(self,title):
        window_handles=self.driver.window_handles
        for window_handle in window_handles:
            if WebDriverWait(self.driver,getconfig.gettimeout).until(EC.title_contains(title)):
                self.driver.switch_to.window(window_handle)
                break

    def switch_window_by_tiele(self,url):
        window_handles=self.driver.window_handles
        for window_handle in window_handles:
            if WebDriverWait(self.driver,getconfig.gettimeout).until(EC.title_contains(url)):
                self.driver.switch_to.window(window_handle)
                break

    #将滚动条滚到元素位置
    def scrollbarelement(self,element_info):
        element = self.find_element(element_info)
        self.driver.execute_script('arguments[0].scrollIntoView();',element)



    """
    selenium 执行JS脚本
    
    """

    def deleteelementattribute(self,element_info,attribute_name):
        element=self.find_element(element_info)
        self.driver.execute_script('arguments[0].removeAttribute("%s");'%attribute_name,element)

    def updateelementattribute(self,element_info,attribute_name,value):
        element=self.find_element(element_info)
        self.driver.execute_script('arguments[0].setAttribute("%s","%s");'%(attribute_name,value),element)


    """
    
    Alert 操作
    
    """

    def accept(self,action='accept',time_out=getconfig.gettimeout):
        WebDriverWait(self.driver,time_out).until(EC.alert_is_present())
        alert=self.driver.switch_to.alert
        alert_text=alert.text
        if action =='accept':
            alert.accept()
        elif action == 'dismiss':
            alert.dismiss()
        return alert_text

    def alert_sends(self,contect):
        self.driver.switch_to.alert.send_keys(contect)

    """
    鼠标操作
    
    """

    def rightclick(self,element_info):
        element=self.find_element(element_info)
        ActionChains(self.driver).context_click(element).perform()

    def releasemouse(self):
        ActionChains(self.driver).release().perform()

    def releasehover(self,element_info):
        element=self.find_element(element_info)
        ActionChains(self.driver).move_to_element(element).perform()

    """
    截图操作
    
    """
    #
    # def screen(self,*screen_path):
    #     curren=os.path.dirname(__file__)
    #     now = time.strftime('%Y_%m_%d_%H_%M_%S')
    #     if len(screen_path)== 0:
    #         path=getconfig.getscreenpath
    #     else:
    #         path=screen_path[0]
    #     path=os.path.join(curren,path,'UItest%s.png'%now)
    #     self.driver.get_screenshot_as_file(path)
    def screenshot_as_file(self, *screenshot_path):
        current_dir = os.path.dirname(__file__)
        if len(screenshot_path) == 0:
            screenshot_filepath = getconfig.getscreenpath
        else:
            screenshot_filepath = screenshot_path[0]
        now = time.strftime('%Y_%m_%d_%H_%M_%S')
        screenshot_filepath = os.path.join(current_dir,screenshot_filepath, 'UITest_%s.png' % now)
        self.driver.get_screenshot_as_file(screenshot_filepath)


