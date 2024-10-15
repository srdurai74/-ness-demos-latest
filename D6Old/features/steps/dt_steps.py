import allure
from behave import given, when, then

'''

Explanation of Step Definitions

Given Step: The step_given_user_details function retrieves the user details from 
the data table and stores them in a list of dictionaries (context.user_details). 
Each row in the data table becomes a dictionary with keys corresponding to the column headers.

When Step: The step_when_register_user function simulates user registration for 
each user detail provided. It checks if the username, password, and email are present, 
and sets a registration status accordingly.

Then Steps:
The first step_then_registration_successful asserts that registration was 
successful for all valid users.
The second step_then_registration_failed asserts that the registration failed 
for any users with missing information.

'''

@given('I have the following user details')
def step_given_user_details(context):
    # Access the data table from the context
    context.user_details = []
    for row in context.table:
        # Append each row as a dictionary to the list
        context.user_details.append({
            'username': row['username'],
            'password': row['password'],
            'email': row['email'],
        })
    print("User details received:", context.user_details)

@when('I register the user')
def step_when_register_user(context):
    # Simulate user registration logic
    for user in context.user_details:
        if user['username'] and user['password'] and user['email']:
            print(f"Registering user: {user['username']}, Email: {user['email']}")
            context.registration_status = 'successful'
        else:
            print(f"Failed to register user: {user['username']}")
            context.registration_status = 'failed'

@then('the registration should be successful')
def step_then_registration_successful(context):
    assert context.registration_status == 'successful', "User registration failed!"

@then('the registration should fail with an error message')
def step_then_registration_failed(context):
    assert context.registration_status == 'failed', "User registration did not fail as expected!"

def allureLogs(text):
    with allure.step(text):
        pass

