import time

import allure
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = ""
@allure.step("Adding numbers.....")
@given(u'I am on the login page')
def step_impl(context):
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://opensource-demo.orangehrmlive.com')
    time.sleep(5)

@when(u'I enter username in the username field')
def step_impl(context):
    driver.find_element(By.NAME,'username').send_keys('Admin')
    time.sleep(2)


@when(u'I enter password in the password field')
def step_impl(context):
    driver.find_element(By.NAME,'password').send_keys('admin123')


@when(u'I click the login button')
def step_impl(context):
    driver.find_element(By.XPATH,'//form/div[3]/button').click()


@then(u'I should see the welcome page')
def step_impl(context):
    time.sleep(4)
    dashboard_txt = driver.find_element(By.XPATH,'//h6').text
    assert dashboard_txt == 'Dashboard'
    driver.close()

def allureLogs(text):
    with allure.step(text):
        pass
