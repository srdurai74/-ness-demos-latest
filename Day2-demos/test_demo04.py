import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from BaseConfig import BaseData

def test_search():

    driver = webdriver.Chrome()
    driver.get('https://javascript.info/alert-prompt-confirm')
    driver.maximize_window()
    driver.implicitly_wait(10) # wait for 10 seconds

    driver.find_element(By.CSS_SELECTOR,"div#e97lnstiz9 div:nth-child(1) > a").click()
    time.sleep(5)
    driver.switch_to.alert.accept()

    time.sleep(5)