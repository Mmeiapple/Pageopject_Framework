import random
import time
from Process_test.login_test import login
from common.set_driver import SetDriver
from elementinfo.organization_user_page import OraganizationUserPage
from elementinfo.organization_home_page import OraganizationHomePage
from elementinfo.organization_user_adduser_page import OraganizationUserAdduserPage
from elementinfo.organization_company_page import OrganizationCompanyPage

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

#添加用户--密码校验错误测试
def NormalUserCreation_Secreterror(dri):
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


#编辑公司信息--正常编辑公司信息
def EditCompanyInformation(dri):
    loginin = login(dri)
    company_info = OrganizationCompanyPage(dri)
    # 点击组织
    home_info = OraganizationHomePage(dri)
    home_info.click_organization_link()
    # 点击公司
    home_info.click_company_link()
    # 点击编辑公司
    company_info.click_editcompany_click()
    # 切换框架
    company_info.switch_switchframe()
    # 输入公司姓名
    company_info.clear_input_companyname_input()
    company_info.input_companyname_input('黑麋鹿如是说')
    # 输入联系方式
    company_info.clear_input_phone_input()
    company_info.input_phone_input('18888888888')
    # 输入传真方式
    company_info.clear_input_fax_input()
    company_info.input_fax_input('0745-12312')
    # 输入地址
    company_info.clear_input_address_input()
    company_info.input_address_input('天空之城')
    # 输入邮编号码
    company_info.clear_input_zipcode_input()
    company_info.input_zipcode_input('4323143')
    # 输入外部地址
    company_info.clear_website_input()
    company_info.input_website_input('https//:hm.com')
    # 输入内部地址
    company_info.clear_backyard_input()
    company_info.input_backyard_input('http:172.98.0.1')
    # 选择匿名登录
    company_info.click_anonymous_click()
    # 保存
    company_info.submit_save_button()
    # 退出框架
    company_info.quitframe()
    home_info.click_user_link()

#点击组织下的连接--正常点击
def ClickOrganizationLink(dri):
    loginin= login(dri)
    driver = OraganizationHomePage(dri)
    # 点击组织连接
    driver.click_organization_link()
    # 点击部门连接
    driver.click_department_link()
    # 点击公司连接
    driver.click_company_link()
    # 点击动态连接
    driver.click_dynamic_link()
    # 点击动态连接
    driver.click_department_link()
    # 点击用户连接
    driver.click_user_link()

#点击用户下的连接--正常点击
def click_user_link(dri):
    driver1 = OraganizationHomePage(dri)
    loginin = login(dri)
    driver1.click_organization_link()
    driver = OraganizationUserPage(dri)
    driver.click_adduser()
    time.sleep(2)
    driver.back()
    driver.click_addusers()
    time.sleep(2)
    driver.back()
    driver.click_deleteuser_button()
    time.sleep(2)
    driver.click_dismissdeleteuser_button()
    time.sleep(2)
    driver.click_selection_button()
    time.sleep(2)
    driver.click_selection_button()
    time.sleep(2)
    driver.click_maintenancedepartment_link()
    time.sleep(2)
    driver.back()
    driver.click_edituser_button()

#删除用户--取消
def click_user_link(dri):
    driver1 = OraganizationHomePage(dri)
    loginin = login(dri)
    driver1.click_organization_link()
    driver = OraganizationUserPage(dri)
    driver.click_adduser()
    time.sleep(2)
    driver.back()
    driver.click_deleteuser_button()
    time.sleep(2)
    driver.click_dismissdeleteuser_button()
    time.sleep(2)

if __name__=="__main__":
     dri=SetDriver()
     click_user_link(dri)
