import time

import pytest
from selenium import webdriver


# @pytest.mark.order("last")
# @pytest.mark.order(2)

@pytest.mark.smoke
def test_a():
    time.sleep(3)
    assert True

# @pytest.mark.order(1)

@pytest.mark.smoke
@pytest.mark.regression
def test_b():
    time.sleep(3)
    assert True

@pytest.mark.regression
def test_c():
    time.sleep(3)
    assert False

@pytest.mark.regression
def test_d():
    time.sleep(3)
    assert True
