import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By



def test_switch_windows():

    driver = webdriver.Chrome()
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    driver.maximize_window()
    time.sleep(5)

    driver.find_element(By.PARTIAL_LINK_TEXT,'Orange').click()
    time.sleep(5)

    print(driver.current_window_handle)
    parent_window = driver.current_window_handle


    driver.switch_to.window(driver.window_handles[1])

    assert driver.title == 'Human Resources Management Software | OrangeHRM'

    driver.switch_to.window(parent_window)


    assert driver.title == 'OrangeHRM'






