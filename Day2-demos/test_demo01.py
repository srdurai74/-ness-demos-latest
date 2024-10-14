import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from DataConfig import Data

def test_search():

    driver = webdriver.Chrome()
    driver.get('https://ebay.com')
    driver.maximize_window()
    driver.implicitly_wait(10) # wait for 10 seconds

    # if element not found, nosuchelementexception will be thrown
    driver.find_element(By.XPATH,"//input[@name='_nkw' and @type='text']").send_keys(Data.SEARCH_TEXT)
    time.sleep(2)

    category_list = driver.find_element(By.CSS_SELECTOR,"select#gh-cat")
    categories = Select(category_list)

    categories.select_by_visible_text(Data.CATEGORY)

    driver.find_element(By.XPATH,"//input[@value='Search']").click()
    time.sleep(2)

    caty_list = driver.find_elements(By.TAG_NAME,"option")
    for caty in caty_list:
        print(caty.text)

    # print(driver.page_source)

    assert Data.SEARCH_TEXT in driver.current_url

    driver.close() # close the active window
    driver.quit() # close all the child windows along with parent window