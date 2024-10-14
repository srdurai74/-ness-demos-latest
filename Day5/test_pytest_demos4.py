import pytest

@pytest.mark.dependency()
def test_a():
    assert False

@pytest.mark.dependency()
def test_b():
    assert True

@pytest.mark.dependency(depends=["test_a"])
def test_c():
    assert True

@pytest.mark.dependency(depends=["test_b"])
def test_d():
    assert True

@pytest.mark.dependency(depends=["test_b", "test_c"])
def test_e():
    assert True
