import allure
from behave import given, when, then


@given(u'I have user data')
def step_impl(context):
    allureLogs('Step: I have user data')
    allure.attach('Step: I have user data', name='Test Status', attachment_type=allure.attachment_type.TEXT)

    # allure.attach('Step: I have user data', 'This is the user data')

    context.user_details = []

    for row in context.table:
        context.user_details.append({
                'username': row['username'],
                'password': row['password'],
                'email': row['email']
        })

    # print(context.user_details)


@when(u'i register the user')
def step_impl(context):
    # allure.attach('Step: i register the user', 'i register the user')
    allureLogs('i register the user')


    allure.attach('Step: i register the user', name='Test Status', attachment_type=allure.attachment_type.TEXT)

    # allure.attach(context.user_details)

@then(u'the user should be registered')
def step_impl(context):
    # allure.attach('Step: The user should be registered', 'The user should be registered')
    allure.attach('the user should be registered', name='Test Status', attachment_type=allure.attachment_type.TEXT)


def allureLogs(text):
    with allure.step(text):
        pass