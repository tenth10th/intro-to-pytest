import pytest


@pytest.fixture(params=["a", "b", "c", "d", "e"])
def letter(request):
    """
    Fixtures with parameters will run tests multiple times
    (You can access the current parameter via the request fixture)
    """
    print("\n   (letter fixture yielding request.param: {})".format(request.param))
    yield request.param


@pytest.fixture(params=[1, 2, 3], ids=['foo', 'bar', 'baz'])
def mode(request):
    """
    The "ids" keyword argument can be used to provide alternate
    labels for parameters ("foo", "bar", "baz" instead of 1, 2, 3)
    """
    print("\n   (mode fixture yielding request.param: {})".format(request.param))
    yield request.param


def test_parameterization(letter):
    print("   Running test_parameterization with request.param: {}".format(letter))


def test_modes(mode):
    print("   Running test_modes with request.param: {}".format(mode))