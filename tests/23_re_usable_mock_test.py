from other_code.services import count_service, SimulatedDBFailure
from pytest import fixture, raises


@fixture
def re_usable_db_mocker(mocker):
    """
    Fixtures can invoke mocker to return "re-usable" mocks
    """
    # autospec encourages your mock to have the same interfaces as the real thing
    # (highly recommended where applicable!)
    print("\n(creating re-usable mock that avoids the slow DB call...)")
    mock_db_service = mocker.patch("other_code.services.db_service", autospec=True)
    mock_db_service.return_value = [(0, "fake row", 0.0)]
    return mock_db_service


def test_re_usable_mocker(re_usable_db_mocker):
    """
    count_service is very slow - But now we can test the API, without the cost
    """
    c = count_service("foo")
    re_usable_db_mocker.assert_called_with("foo")
    assert c == 1


def simulate_failure(count_service_arg):
    print("(simulating a database failure for input: bar)")
    if count_service_arg == "bar":
        raise SimulatedDBFailure("Oh no! Our Database! It's Broken!")


def test_mocker_with_exception(re_usable_db_mocker):
    """
    Mocks can be configured to raise Exceptions - Useful for testing error handling!
    """
    re_usable_db_mocker.side_effect = simulate_failure

    with raises(SimulatedDBFailure):
        count_service("bar")
