import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By



def test_kb_mouse_actions():

    driver = webdriver.Chrome()
    driver.get('https://jqueryui.com/droppable/')
    driver.maximize_window()
    time.sleep(5)



    driver.switch_to.frame(0)
    time.sleep(3)

    draggable = driver.find_element(By.ID, 'draggable')
    droppable = driver.find_element(By.ID, 'droppable')

    ActionChains(driver).drag_and_drop(draggable,droppable).perform()

    # ActionChains(driver) \
    #     .move_to_element(draggable)\
    #     .click_and_hold(draggable)\
    #     .move_to_element(droppable)\
    #     .pause(2)\
    #     .release()\
    #     .pause(2) \
    #     .click_and_hold(draggable) \
    #     .move_by_offset(30,60) \
    #     .release() \
    #     .pause(2)\
    #     .perform()

    time.sleep(5)




