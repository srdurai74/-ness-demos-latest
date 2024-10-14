

import pytest

# @pytest.mark.skip
# def test_methodone(init):
#     print('Method one')

# @pytest.mark.xfail(reason="Bug not fixed")

@pytest.mark.dependency(depends=['test_methodtwo'])
def test_methodone():
    assert True

@pytest.mark.dependency()
def test_methodtwo():
    assert True
