import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with


def get_data():
    # get data from excel source and return it
    return [
        ('Sam','Sam'),
        ('Admin','admin123')
    ]

@pytest.mark.parametrize("username,password", get_data())
def test_login(username,password):

    driver = webdriver.Chrome()
    driver.get('https://opensource-demo.orangehrmlive.com')
    driver.implicitly_wait(10)
    driver.maximize_window()
    time.sleep(5)

    # using relative locators
    username_field = driver.find_element(locate_with(By.NAME,'username').above({By.NAME:'password'}))
    username_field.send_keys(username)
    time.sleep(2)
    password_field = driver.find_element(locate_with(By.NAME,'password').below({By.NAME:'username'}))
    password_field.send_keys(password)
    time.sleep(2)
    login_button = driver.find_element(locate_with(By.XPATH,'//button[@type="submit"]').near({By.NAME:'password'}))
    login_button.click()
    time.sleep(5)
    if((username == 'Admin') and (password =='admin123')):

        # message in dashboard page on successful login
        dashboard_text_item = driver.find_element(By.XPATH, '//h6')
        is_dashboard_msg_displayed = dashboard_text_item.is_displayed()

        # assertion for valid credentials
        assert is_dashboard_msg_displayed
    else:
        # error message in home page
        error_msg_field = driver.find_element(By.XPATH, '//')
        error_msg = error_msg_field.text

        # assertion for invalid credentials
        assert error_msg == 'Invalid credentials'

    driver.quit()
