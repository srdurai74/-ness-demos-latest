import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from BaseConfig import BaseData

def test_search():

    driver = webdriver.Chrome()
    driver.get(BaseData.BASE_URL)
    driver.maximize_window()
    driver.implicitly_wait(10) # wait for 10 seconds

    # driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
    # time.sleep(3)

    driver.find_element(By.PARTIAL_LINK_TEXT,"OrangeHRM").click()
    time.sleep(3)
