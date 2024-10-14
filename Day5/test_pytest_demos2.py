

import pytest

@pytest.fixture(scope="class")
def init():
    print('before the test')
    yield
    print('after the test')

@pytest.mark.usefixtures("init")
class BasicTest:
    pass

class Test_FixTest(BasicTest):

    def test_methodone(init):
        print('Method one')


    def test_methodtwo(init):
        print('Method two')
