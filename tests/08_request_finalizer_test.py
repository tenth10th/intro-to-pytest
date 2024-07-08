import pytest


def test_with_safe_cleanup_fixture(safe_fixture):
    print("\nRunning test_with_safe_cleanup_fixture...")
    assert True


@pytest.fixture
def safe_fixture(request):
    """
    The request can also be used to apply post-test callbacks
    (these will run even if the Fixture itself fails!)
    """
    print("\n(Begin setting up safe_fixture)")
    # request.addfinalizer(safe_cleanup)
    request.addfinalizer(safest_cleanup)
    # request.addfinalizer(safer_cleanup)
    risky_function()


def safe_cleanup():
    print("\n(safe_cleanup up after test...)")
    raise Exception("That didn't help at all!")

def safer_cleanup():
    print("\n(safer_cleanup up after test...)")
    raise Exception("Oh no, this didn't work either!")

def safest_cleanup():
    print("\n(safest_cleanup up after test...)")
    print("\n(phew, that worked)")


def risky_function():
    print("   (Running Risky Function: Totally worth it!)")
    # # Uncomment to simulate a failure during Fixture setup!
    # raise Exception("Whoops, I guess that risky function didn't work...")
