import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from selenium.common import ElementNotInteractableException
from selenium.common import ElementClickInterceptedException

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from BaseConfig import BaseData

def test_search():

    driver = webdriver.Chrome()
    driver.get(BaseData.BASE_URL)
    driver.maximize_window()
    # driver.implicitly_wait(10) # wait for 10 seconds
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR,'div:nth-child(2) >input[name="username"]').send_keys("Admin")
    driver.find_element(By.CSS_SELECTOR,'div:nth-child(2) >input[name="password"]').send_keys("admin123")
    driver.find_element(By.XPATH,"//button[@type='submit']").submit()

    # wait = WebDriverWait(driver,10)
    errors = [NoSuchElementException, ElementNotInteractableException,ElementClickInterceptedException]

    wait = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=errors)

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'img ~ p')))

    driver.find_element(By.CSS_SELECTOR,'img ~ p').click()

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'ul[role="menu"] > li:last-child >a')))
    driver.find_element(By.CSS_SELECTOR,'ul[role="menu"] > li:last-child >a').click()



