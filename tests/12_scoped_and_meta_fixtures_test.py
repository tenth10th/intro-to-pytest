from pytest import fixture, mark
from other_code.services import ExpensiveClass
import string


@fixture(scope="module")
def scoped_expensive_fixture():
    """
    Scoping affects how often fixtures are (re)initialized
    The "module" scope encourages pytest to initialize it once per module/file
    (and shut it down after the final test in the module/file)
    """
    print("\n(Begin Module-scoped fixture...)\n")
    expensive_class = ExpensiveClass()

    yield expensive_class

    expensive_class.cleanup()
    print("(End Module-scoped fixture!)")


def test_scoped_A(scoped_expensive_fixture):
    """
    A very simple test, that does not (explicitly!) request any fixtures...
    """
    print("\n   Running test_A with {}".format(scoped_expensive_fixture))


def test_scoped_B(scoped_expensive_fixture):
    """
    Another simple test, that also does not appear to request any fixtures...
    """
    print("\n   Running test_B with {}".format(scoped_expensive_fixture))
