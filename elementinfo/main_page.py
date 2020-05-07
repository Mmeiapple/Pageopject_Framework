from common.base_page_info import BasePage
from common.element_data_utils import GetElementInfo
from common.browser import Browser
from Process_test import login_test

class MainPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        element=GetElementInfo('main').getelementinfo('main_page')
        self.myzone_link=element['myzone_link']
        self.user_menu=element['user_menu']
        self.quit_button=element['quit_button']


    def goto_myzone(self):  # 进入我的地盘菜单
        self.click(self.myzone_link)

    def get_username(self):
        value = self.get_text(self.user_menu)
        return value

    def click_username(self):
        self.click( self.user_menu )

    def click_quit_button(self):
        self.click( self.quit_button )


if __name__=="__main__":
    dri=Browser('chrome').getdriver()
    login=login_test.login(dri)
    driver=MainPage(dri)
    driver.setmaxbrowser()
    driver.goto_myzone()