import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def test_login():

    base_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    driver = webdriver.Chrome()

    time.sleep(2)
    driver.get(base_url)
    time.sleep(2)
    driver.maximize_window()
    time.sleep(2)

    driver.find_element(by='name',value='username').send_keys('admin')
    time.sleep(2)

    driver.find_element(by='name',value='password').send_keys('admin')
    time.sleep(2)

    driver.find_element(by='xpath', value='//form/div/button').click()
    time.sleep(2)

    error_msg_field = driver.find_element(by='xpath',value="//div[@class='orangehrm-login-error']/div/div/p")

    expected_text = 'Invalid credentials'

    time.sleep(2)
    assert error_msg_field.text == expected_text


# write code to assert page title
    time.sleep(2)
    assert driver.title == 'OrangeHRM'
    # write code to check if a webelement is present or not
    time.sleep(2)




    time.sleep(5)

    driver.close()

