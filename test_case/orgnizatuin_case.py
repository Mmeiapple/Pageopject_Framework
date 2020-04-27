import random
from Process_test.login_test import login
from common.set_driver import SetDriver
from elementinfo.organization_user_page import OraganizationUserPage
from elementinfo.organization_home_page import OraganizationHomePage
from elementinfo.organization_user_adduser_page import OraganizationUserAdduserPage
num=random.randint(1,1000)


#添加用户--正常添加用户测试
def NormalUserCreation(dri):
    #登录
    loginin=login(dri)
    #点击组织
    home_info=OraganizationHomePage(dri)
    home_info.click_organization_link()
    #点击添加用户
    user_info=OraganizationUserPage(dri)
    user_info.click_adduser()
    #进入添加用户表单
    adduser_info=OraganizationUserAdduserPage(dri)
    adduser_info.input_username_input('test' + str(num))
    adduser_info.input_userpassword_input('a.123456')
    adduser_info.input_repeatpassword_input('a.123456')
    adduser_info.input_realname_input('测试' + str(num))
    adduser_info.clear_entrydate_input()
    adduser_info.input_entrydate_input('2020-04-26')
    adduser_info.click_clickpage_clickt()
    adduser_info.click_Jobchoice_click()
    adduser_info.click_rightsgroup_selected_click()
    adduser_info.click_rightsgroup_click()
    adduser_info.input_email_input('50534' + str(num) + '@qq.com')
    adduser_info.input_codeaccount_input(str(num))
    adduser_info.click_gender_button()
    adduser_info.clear_passwordchecking_input()
    adduser_info.input_passwordchecking_input('a12345678')
    adduser_info.scroll_scrollbarelement()
    adduser_info.click_save_button()

#添加用户--密码校验错误测试
def NormalUserCreation(dri):
    #登录
    loginin=login(dri)
    #点击组织
    home_info=OraganizationHomePage(dri)
    home_info.click_organization_link()
    #点击添加用户
    user_info=OraganizationUserPage(dri)
    user_info.click_adduser()
    #进入添加用户表单
    adduser_info=OraganizationUserAdduserPage(dri)
    adduser_info.input_username_input('test' + str(num))
    adduser_info.input_userpassword_input('a.123456')
    adduser_info.input_repeatpassword_input('a.123456')
    adduser_info.input_realname_input('测试' + str(num))
    adduser_info.clear_entrydate_input()
    adduser_info.input_entrydate_input('2020-04-26')
    adduser_info.click_clickpage_clickt()
    adduser_info.click_Jobchoice_click()
    adduser_info.click_rightsgroup_selected_click()
    adduser_info.click_rightsgroup_click()
    adduser_info.input_email_input('50534' + str(num) + '@qq.com')
    adduser_info.input_codeaccount_input(str(num))
    adduser_info.click_gender_button()
    adduser_info.clear_passwordchecking_input()
    adduser_info.input_passwordchecking_input('999999')
    adduser_info.scroll_scrollbarelement()
    adduser_info.click_save_button()




if __name__=="__main__":
     dri=SetDriver()
     NormalUserCreation(dri)
