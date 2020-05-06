from common.base_page_info import BasePage
from common.element_data_utils import GetElementInfo
from common.set_driver import SetDriver
from Process_test.login_test import login
from elementinfo.organization_home_page import OraganizationHomePage


class OrganizationCompanyPage(BasePage):
    def __init__(self,driver):
        super(OrganizationCompanyPage,self).__init__(driver)

        element_info=GetElementInfo('organization').getelementinfo('company_page')

        self.editcompany_click=element_info['editcompany_click']

        self.frame_switch = element_info['frame_switch']

        self.companyname_input = element_info['companyname_input']

        self.phone_input = element_info['phone_input']

        self.fax_input = element_info['fax_input']

        self.address_input = element_info['address_input']

        self.zipcode_input = element_info['zipcode_input']

        self.website_input = element_info['website_input']

        self.backyard_input = element_info['backyard_input']

        self.anonymous_click = element_info['anonymous_click']

        self.save_button = element_info['save_button']


    def switch_switchframe(self):
        self.switchframe(self.frame_switch)

    def click_editcompany_click(self):
        self.click(self.editcompany_click)

    def clear_input_companyname_input(self):
        self.clear(self.companyname_input)

    def input_companyname_input(self,companyname):
        self.input(self.companyname_input,companyname)

    def clear_input_phone_input(self):
        self.clear(self.phone_input)

    def input_phone_input(self,phone):
        self.input(self.phone_input,phone)

    def clear_input_fax_input(self):
        self.clear(self.fax_input)

    def input_fax_input(self,fax):
        self.input(self.fax_input,fax)

    def clear_input_address_input(self):
        self.clear(self.address_input)

    def input_address_input(self,address):
        self.input(self.address_input,address)

    def clear_input_zipcode_input(self):
        self.clear(self.zipcode_input)

    def input_zipcode_input(self,zipcode):
        self.input(self.zipcode_input,zipcode)

    def clear_website_input(self,):
        self.clear(self.website_input)

    def input_website_input(self,website):
        self.input(self.website_input,website)

    def clear_backyard_input(self,):
        self.clear(self.backyard_input)

    def input_backyard_input(self,backyard):
        self.input(self.backyard_input,backyard)

    def click_anonymous_click(self):
        self.click(self.anonymous_click)

    def submit_save_button(self):
        self.submit(self.save_button)

if __name__=="__main__":
    dri=SetDriver()
    loginin=login(dri)
    company_info=OrganizationCompanyPage(dri)
    #点击组织
    home_info=OraganizationHomePage(dri)
    home_info.click_organization_link()
    #点击公司
    home_info.click_company_link()
    #点击编辑公司
    company_info.click_editcompany_click()
    #切换框架
    company_info.switch_switchframe()
    #输入公司姓名
    company_info.clear_input_companyname_input()
    company_info.input_companyname_input('黑麋鹿如是说')
    #输入联系方式
    company_info.clear_input_phone_input()
    company_info.input_phone_input('18888888888')
    #输入传真方式
    company_info.clear_input_fax_input()
    company_info.input_fax_input('0745-12312')
    # 输入地址
    company_info.clear_input_address_input()
    company_info.input_address_input('天空之城')
    #输入邮编号码
    company_info.clear_input_zipcode_input()
    company_info.input_zipcode_input('4323143')
    #输入外部地址
    company_info.clear_website_input()
    company_info.input_website_input('https//:hm.com')
    #输入内部地址
    company_info.clear_backyard_input()
    company_info.input_backyard_input('http:172.98.0.1')
    #选择匿名登录
    company_info.click_anonymous_click()
    #保存
    company_info.submit_save_button()
    #退出框架
    company_info.quitframe()
    home_info.click_user_link()
