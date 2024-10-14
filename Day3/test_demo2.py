import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver =""

@pytest.fixture()
def setup():
    global driver
    driver = webdriver.Chrome()
    driver.get('https://paytm.com')
    driver.maximize_window()
    yield
    driver.close()

def test_switch_frame(setup):

    driver.find_element(By.XPATH,'//span[text()="Sign In"]').click()
    time.sleep(10)


    print(driver.find_element(By.XPATH,'//iframe[@src="/v1/api/login?isIframe=true&theme=paytm-web"]').is_displayed())

    driver.switch_to.frame(0)
    # driver.switch_to.frame(driver.find_element(By.XPATH,'//iframe[@src="/v1/api/login?isIframe=true&theme=paytm-web"]'))
    time.sleep(5)

    print(driver.find_element(By.CSS_SELECTOR, 'div.qrLoginCont').is_displayed())

    # # driver.find_element(By.CSS_SELECTOR,'div._3NG4-yOlawf2yCGLW1iqWa > span > a').click()
    # time.sleep(5)
    #
    # driver.find_element(By.XPATH,'//a[@title="Close"]').click()
    #
    # time.sleep(5)
    #



