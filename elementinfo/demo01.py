import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import  By
from Process_test.login_test import login
from common.set_driver import SetDriver
from elementinfo.organization_home_page import OraganizationHomePage
from elementinfo.organization_company_page import OrganizationCompanyPage

try:
    driver=SetDriver()
    login=login(driver)
    # 点击组织
    driver.find_element(By.XPATH,'//a[text()="组织"]').click()
    # 选择公司
    home_info=OraganizationHomePage(driver)
    home_info.click_company_link()
    # ---修改公司名称---
    # 点击编辑
    driver.find_element(By.XPATH, '//a[@id="editCompany"]').click()
    # 切框架
    frame = driver.find_element(By.XPATH, '//div/div/div[2]/iframe[@id="iframe-triggerModal"]')
    # driver.switch_to.frame(frame)
    company_info=OrganizationCompanyPage(driver)
    company_info.switchframe1(frame)

    # 修改公司名称
    driver.find_element(By.XPATH, '//input[@id="name"]').clear()
    driver.find_element(By.XPATH, '//input[@id="name"]').send_keys('黑麋鹿如是说')
    #联系方式
    driver.find_element(By.XPATH,'//input[@id="phone"]').clear()
    driver.find_element(By.XPATH,'//input[@id="phone"]').send_keys('18888888888')
    # 传真
    driver.find_element(By.XPATH, '//input[@id="fax"]').clear()
    driver.find_element(By.XPATH, '//input[@id="fax"]').send_keys('0745-3227659')
    # 地址
    driver.find_element(By.XPATH, '//input[@id="address"]').clear()
    driver.find_element(By.XPATH, '//input[@id="address"]').send_keys('天空之城298号')
    # 邮政编码
    driver.find_element(By.XPATH, '//input[@id="zipcode"]').clear()
    driver.find_element(By.XPATH, '//input[@id="zipcode"]').send_keys('423887')
    # 官网
    driver.find_element(By.XPATH, '//input[@id="website"]').clear()
    driver.find_element(By.XPATH, '//input[@id="website"]').send_keys('https://hm.com')
    # 内网
    driver.find_element(By.XPATH, '//input[@id="backyard"]').clear()
    driver.find_element(By.XPATH, '//input[@id="backyard"]').send_keys('https://hm.com')
    # 匿名登录
    driver.find_element(By.XPATH,'//input[@id="guest0"]').click()
    # 保存
    driver.find_element(By.XPATH, '//button[@id="submit"]').submit()
    # 切出框架
    company_info.quitframe1()
    home_info.click_user_link()

finally:
    time.sleep(5)
    driver.quit()