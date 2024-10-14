

import pytest

@pytest.fixture()
def init():
    print('before the test')
    yield
    print('after the test')

def test_methodone(init):
    print('Method one')


def test_methodtwo(init):
    print('Method two')
