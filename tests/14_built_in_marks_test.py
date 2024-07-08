import pytest

# An accurate simulation of not having any credentials!
api_credentials = None

@pytest.mark.skip(reason="This feature is currently broken")
def test_broken_feature():
    # Always skipped!
    assert False


@pytest.mark.skipif(not api_credentials, reason="API credentials not found!")
def test_skipif():
    # Skipped if a certain condition is met
    assert False

@pytest.mark.xfail(reason="It's okay if this fails")
def test_where_failure_is_acceptable_xpass():
    # Allows failed assertions (returns "XPASS" if there are no failures)
    assert True


@pytest.mark.xfail(reason="This should probably fail?")
def test_where_failure_is_acceptable_xfail():
    # Allows failed assertions (returns "xfail" on failure)
    assert False


@pytest.mark.xfail(strict=True, reason="This logic is totally backwards: Passing is actually a bad sign!")
def test_where_failure_is_mandatory():
    # Requires failed assertions! (returns "xfail" on failure; FAILs on pass!)
    assert False


# # Uncomment to skip all the tests in this module!
# pytest.skip("This whole Module is problematic at best...", allow_module_level=True)
