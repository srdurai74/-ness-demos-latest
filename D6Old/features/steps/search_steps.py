import allure
from adodbapi.examples.xls_write import data
from behave import *
from behave.formatter import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import json

driver = ""

@allure.step("Adding numbers:")
@given(u'I am on the home page')
def step_impl(context):
    allureLogs("Welcome")
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.get('https://www.ebay.com')

@when(u'I fill in search field with Samsung')
def step_impl(context):
    allureLogs("Welcome")
    context.driver.find_element(By.ID,"gh-ac").send_keys("Samsung")
    allure.attach(context.driver.get_screenshot_as_png(), name="Application Home1", attachment_type=allure.attachment_type.PNG)


@when(u'select a "{category}"')
def step_impl(context,category):
    allureLogs("Welcome")
    allure.attach("Test passed as expected", name="Test Status", attachment_type=allure.attachment_type.TEXT)

    context.category = category
    select = Select(context.driver.find_element(By.ID,"gh-cat"))
    select.select_by_visible_text(category)
    allure.attach(context.driver.get_screenshot_as_png(), name="Application Home2", attachment_type=allure.attachment_type.PNG)


@when(u'I click search button')
def step_impl(context):
    allureLogs("Welcome")

    context.driver.find_element(By.ID,"gh-btn").click()
    allure.attach(context.driver.get_screenshot_as_png(), name="Application Home3", attachment_type=allure.attachment_type.PNG)



@then(u'I should see Search results page for Samsung')
def step_impl(context):
    allureLogs("Welcome")
    try:
        assert 'Samsung' in context.driver.title
        assert 'Samsung' in context.driver.current_url
    except AssertionError as e:
        allure.attach(str(e), name="Assertion Error", attachment_type=allure.attachment_type.TEXT)
    print(context.category)
    if(context.category == 'Books'):
        assert '267' in context.driver.current_url
        allure.attach("Test passed as expected", name="Test Status1", attachment_type=allure.attachment_type.TEXT)

    else:
        assert '15032' in context.driver.current_url
        allure.attach("Test passed as expected", name="Test Status2", attachment_type=allure.attachment_type.TEXT)

    context.driver.close()

def allureLogs(text):
    with allure.step(text):
        pass
