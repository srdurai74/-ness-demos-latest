import time

import allure
from behave import given, when, then

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = ""

@given(u'the user is on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.get('https://opensource-demo.orangehrmlive.com')
    allure.attach("End of step1")


@when(u'the username is entered')
def step_impl(context):
    time.sleep(3)
    context.driver.find_element(By.NAME,'username').send_keys('Admin')
    allure.attach("End of step2")

@when(u'the password is entered')
def step_impl(context):
    time.sleep(3)
    context.driver.find_element(By.NAME, 'password').send_keys('admin123')

@when(u'the login button is clicked')
def step_impl(context):
    time.sleep(3)
    context.driver.find_element(By.XPATH, '//div[3]/button').click()
    allure.attach(context.driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)


@then(u'the dashboard page is displayed')
def step_impl(context):
    try:
        time.sleep(3)
        assert "Dashboard" == context.driver.find_element(By.XPATH, "//h").text
    except NoSuchElementException as e:
        allure.attach(context.driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
    time.sleep(3)
    context.driver.close()



@when(u'the user clicks the link in the footer')
def step_impl(context):
    print('click the link in the footer')


@then(u'a new window is displayed')
def step_impl(context):
    print('new window is displayed')
    context.driver.close()
