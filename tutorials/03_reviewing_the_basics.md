### 3: Reviewing the Basics

* PyTest cases can be as simple as a function whose name starts with "test", in a python file whose name starts with "test_" (or ends with "_test.py").

    * (PyTest will also find and run xUnit-style tests created using the standard `unittest` module, allowing you to start using PyTest alongside existing, legacy tests.
    
    * The test-finding behavior has reasonable defaults, but is [extremely configurable!](https://docs.pytest.org/en/latest/goodpractices.html#conventions-for-python-test-discovery).)

* A PyTest case will pass if:
    * Its assertions are True
       * _(Or it doesn't have any assertions!)_
    * And it doesn't raise any unhandled Exceptions.

* PyTest can be used to "exercise" code, and will report errors, even without any actual assertions!

* PyTest uses the basic Python `assert` keyword, but will introspect into your code and "unpack" useful info about why the assertion failed.

    * (If your PyTest case calls other code that makes assertions, they will be honored as well - in the sense that **any** failed assertions resulting from your test will cause the test to be reported as "failed".)
    
    * However, assertions that aren't local (e.g. not located directly inside your test function) won't be "unpacked" and explained in detail.
    
        * Whenever possible, keep all your `assert`ions inside your test cases, so that PyTest can document their failure reasons and context for you!

        * _(If you're trying to avoid repeated assertion code, PyTest has other features that can help with this, including fixtures and parameterization - we'll cover those later.)_

        * If you do feel compelled to call other functions (external to your test case) that perform assertions, try to make sure that they document their behavior - You can provide a second argument to `assert` to describe the context of a failed asssertion in more detail:
          ```
          assert (x > 0), "x should be > 0, but is {}".format(x)
          assert not (x % 2), "x should be divisible by 2, but is {}".format(x)
          ```

* PyTest provides features for "expecting" Exceptions, and matching approximately similar values, similiar to [unittest.TestCase](https://docs.python.org/2/library/unittest.html#basic-example):

    * [pytest.raises](https://docs.pytest.org/en/latest/reference.html#pytest-raises) is a context manager that can "require" certain exceptions, essentially asserting that a particular exception should occur in a code block (handling it, if it does), and failing the test if the exception does not occur.

    * [pytest.approx](https://docs.pytest.org/en/latest/reference.html#pytest-approx) can assert that numerical values are "approximately" equal, with a configurable level of precision. This is convenient for asserting the value of floating point numbers, which are (necessarily) not very precise...

### Up Next:

[Intro to Fixtures](04_intro_to_fixtures.md)
