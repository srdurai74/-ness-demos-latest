import pytest
import allure

@allure.feature("Feature A")
@allure.story("Story 1")
@allure.title("Test Case 1")
def test_case_1():
    # with allure.step("Step 1: Prepare the test"):
        assert True  # Replace with actual preparation logic

    # with allure.step("Step 2: Execute the test"):
        assert 1 + 1 == 2  # Replace with actual test logic

@allure.feature("Feature A")
@allure.story("Story 2")
@allure.title("Test Case 2")
def test_case_2():
    allureLogs("ssssssssssssssssssss")
    allure.attach("aaaaaaTest passed as expected", name="Test Status2", attachment_type=allure.attachment_type.TEXT)

    # with allure.step("Step 1: Prepare for second test"):
    assert True  # Preparation for the second test

    # with allure.step("Step 2: Execute the second test"):
    assert 2 + 2 == 4  # Actual test logic


def allureLogs(text):
    with allure.step(text):
        print(text)