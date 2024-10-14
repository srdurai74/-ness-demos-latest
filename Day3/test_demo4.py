import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By



def test_kb_mouse_actions():

    driver = webdriver.Chrome()
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    driver.maximize_window()
    time.sleep(5)

    ActionChains(driver)\
        .move_to_element(driver.find_element(By.NAME,'username'))\
        .pause(2)\
        .click()\
        .pause(2)\
        .send_keys('abd')\
        .double_click() \
        .pause(2) \
        .key_down(Keys.BACKSPACE) \
        .key_up(Keys.BACKSPACE) \
        .pause(2) \
        .key_down(Keys.SHIFT)\
        .send_keys('Admin')\
        .key_up(Keys.SHIFT)\
        .double_click()\
        .perform()

    time.sleep(5)




