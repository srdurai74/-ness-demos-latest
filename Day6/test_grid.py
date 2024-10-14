import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test_grid():

    options = Options()

    options.set_capability("browserName", "firefox");
    options.set_capability("platformName", "Windows 10");
    options.add_argument("--remote-allow-origins=*");

    driver = webdriver.Remote(command_executor="http://localhost:4444", options=options)

    driver.get("https://www.ebay.com")

    time.sleep(10)

    driver.find_element(By.ID, "gh-ac").send_keys("Indulekha")
    time.sleep(5)
    driver.find_element(By.ID, "gh-btn").click()
    time.sleep(5)
    driver.quit()