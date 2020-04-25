import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import  By
from Process_test.login_test import login

try:
    driver=webdriver.Chrome()
    login=login(driver)
    # 点击组织
    driver.find_element(By.XPATH,'//a[text()="组织"]').click()
    # 点击批量添加用户
    # driver.find_element(By.XPATH,'//a[@class="btn btn-secondary"]').click()
    # driver.back()
    # time.sleep(2)
    # #添加用户
    # driver.find_element(By.XPATH,'//a[@class="btn btn-primary"]').click()
    # driver.back()
    # 编辑按钮
    # driver.find_element(By.XPATH,'//form/table/tbody/tr[2]/td[11]/a[1]/i[@class="icon-common-edit icon-edit"]').click()
    # driver.back()
    # time.sleep(2)
    # driver.find_elements(By.XPATH,'//i[@class="icon-common-edit icon-edit"]')[2].click()
    # 删除按钮
    driver.find_element(By.XPATH,'//table/tbody/tr[3]/td[11]/a[2]/i[@class="icon-trash"]').click()
    # 取消删除
    time.sleep(2)
    driver.find_element(By.XPATH,'//button[@class="close"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//div/div[2]/div/div[2]/div/a[@class="btn btn-info btn-wide"]').click()
finally:
    time.sleep(5)
    driver.quit()