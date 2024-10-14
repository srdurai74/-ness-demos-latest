import time

from behave import given, when, then

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


driver = ""

@given(u'the user is on the ebay home page')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.get('https://ebay.com')


@when(u'the user searches for "samsung"')
def step_impl(context):
    context.driver.find_element(By.ID, 'gh-ac').send_keys('samsung')
    time.sleep(3)
@when(u'select a "{category}"')
def step_impl(context,category):
    context.category = category

    select = Select(context.driver.find_element(By.ID, 'gh-cat'))
    select.select_by_visible_text(category)

    time.sleep(3)

@when(u'click the search button')
def step_impl(context):
    context.driver.find_element('id', 'gh-btn').click()
    time.sleep(3)

@then(u'the search results page for samsung is displayed')
def step_impl(context):
    print(context.category)
    if(context.category == 'Cell Phones & Accessories'):
        assert "Samsung" in context.driver.title

    time.sleep(3)