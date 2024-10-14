import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def test_login():

    base_url = 'https://ebay.com'
    driver_path='path to the driver'

    # this setting is for selenium 4.x initial versions
    #driver = webdriver.Chrome(executable_path=driver_path)

    # service1 = Service(driver_path)
    # driver = webdriver.Chrome(service=service1)

    # driver = webdriver.Chrome()
    # driver = webdriver.Edge()

    # driver = webdriver.Firefox()

    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    driver = webdriver.Chrome(options=options)

    time.sleep(2)
    driver.get(base_url)

    time.sleep(5)
    driver.close()

