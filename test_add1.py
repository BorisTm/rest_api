import pytest
import test_add


@pytest.fixture(params=[5, 10])
def x(request):
    print("x")
    return request.param


@pytest.fixture(scope='module')
def y():
    print("y")
    return 5


def test_add1():
    assert test_add.add(2, 3) == 5


def test_add2():
    with pytest.raises(ValueError):
        test_add.add(42, 1)


def test_add3(x, y):
    assert test_add.add(x, y) == 10


def test_add4(x, y):
    assert test_add.add(x, y) == 10