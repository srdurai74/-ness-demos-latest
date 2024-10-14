import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver =""

@pytest.fixture()
def setup():
    global driver
    driver = webdriver.Chrome()
    driver.get('https://javascript.info/alert-prompt-confirm')
    driver.maximize_window()
    yield
    driver.close()



# @pytest.mark.skip
def test_confirm_alert(setup):

    driver.find_element(By.XPATH,'//div[@id="svp96eabha"]//div[1]/a').click()
    time.sleep(5)
    driver.switch_to.alert.dismiss()

    assert driver.switch_to.alert.text == 'false'
    time.sleep(5)
    driver.switch_to.alert.accept()


def test_prompt_alert(setup):

    driver.find_element(By.CSS_SELECTOR,'div#xtk9v3lt7b div:first-child > a').click()
    time.sleep(5)
    driver.switch_to.alert.send_keys('30')

    time.sleep(5)
    driver.switch_to.alert.accept()

    assert '30 years' in driver.switch_to.alert.text

    time.sleep(5)
    driver.switch_to.alert.accept()





