import pytest


@pytest.fixture(params=["a", "b", "c", "d"])
def letters_fixture(request):
    """
    Fixtures can cause tests to be run multiple times (once per parameter)
    """
    yield request.param


@pytest.fixture(params=[1, 2, 3, 4])
def numbers_fixture(request):
    """
    Fixtures can invoke each other (producing cartesian products of parameters)
    """
    yield request.param


def test_params_ception(letters_fixture, numbers_fixture):
    """
    Print out our "coordinate" (the product of our combined fixtures)
    """
    coordinate = letters_fixture + str(numbers_fixture)

    print('\n   Running test_params_ception with "{}"'.format(coordinate))
