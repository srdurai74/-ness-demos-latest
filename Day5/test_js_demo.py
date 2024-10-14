import time

from selenium import webdriver


def test_js():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    # driver.get('https://google.com')
    #
    # time.sleep(5)
    #
    # driver.execute_script("(document.getElementsByName('q')[0]).value='Selenium'")
    # time.sleep(5)
    # # driver.execute_script("alert('username entered')")
    #
    # driver.execute_script("(document.getElementsByName('btnK')[0]).click()")
    #
    # time.sleep(5)
    #

    driver.get('https://ebay.com')
    time.sleep(2)
    driver.execute_script("window.scroll(0,800)")
    driver.get_screenshot_as_file("demo.png")

    time.sleep(5)