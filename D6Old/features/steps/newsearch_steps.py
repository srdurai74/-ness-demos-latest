from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import allure

driver = ""
@allure.step("Adding numbers:")
@allure.step("Verify product details page")
@allure.label("feature", "Product Search")
@given(u'the user in the home page')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.get('https://www.ebay.com')

@when(u'the search text is entered')
def step_impl(context):

    for row in context.table:
        searchtext = row[0]
        if(searchtext == 'samsung'):
            break
    context.driver.find_element(By.ID,"gh-ac").send_keys(searchtext)

@when(u'the search button is clicked')
def step_impl(context):
    context.driver.find_element(By.ID, "gh-btn").click()

@then(u'the Search results page should be displayed')
def step_impl(context):
    assert 'Samsung' in context.driver.title
    assert 'samsung' in context.driver.current_url

def allureLogs(text):
    with allure.step(text):
        pass
