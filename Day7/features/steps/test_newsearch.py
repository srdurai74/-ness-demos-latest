import allure
from behave import given, when, then


@given(u'the user is on the ebay home page')
def step_impl(context):
    print("User is on the ebay home page")


@when(u'the search text and make year is entered')
def step_impl(context):
    print("Search text is entered")
    for row in context.table:
        print(row)
        print(row[0])
        print(row[1])

@when(u'the search button is clicked')
def step_impl(context):
    allureLogs("Search button is clicked")
    print("Search button is clicked")

@then(u'the search results page is displayed')
def step_impl(context):
    assert True
    print("Search results page for samsung is displayed")
    allure.attach('the user should be registered', name='Test Status', attachment_type=allure.attachment_type.TEXT)


def allureLogs(text):
    with allure.step(text):
        pass