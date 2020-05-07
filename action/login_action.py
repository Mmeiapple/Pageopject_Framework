from elementinfo.login_page import LoginPage
from common.browser import Browser
from elementinfo.main_page import MainPage
from common.get_config import getconfig

class LoginAction():
   def __init__(self,driver):
       self.loginpage=LoginPage(driver)

   """
    
   登录功能
    
   """

   def loginaction(self,username,password):
       self.loginpage.inputusername(username)
       self.loginpage.inputuserpassword(password)
       self.loginpage.clicklogin()

   """

   默认登录功能

   """
   def defaulelogin(self):
        self.loginaction(getconfig.getusername,getconfig.getpassword)



   """

   登录成功功能

   """

   def suceseelogin(self,username,password):
        self.loginaction(username,password)
        return MainPage(self.loginpage.driver)

   """

   登录失败功能

   """

   def faillogin(self, username, password):
       self.loginaction(username, password)
       return self.loginpage.accept()


