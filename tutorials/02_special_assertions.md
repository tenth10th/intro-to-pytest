## 2: Special Assertions

Not everything can be expressed as a simple assertion, though, but fear not! PyTest provides:

[tests/02_special_assertions_test.py](../tests/02_special_assertions_test.py)

```
pytest -vs tests/02_special_assertions_test.py
```
Two of these tests raise exceptions on purpose - we can use the `pytest.raises` context manager to both assert that the exception happens, and to handle that exception, so it doesn't count as a failure.

Likewise, the test will now fail if the exception _is not raised_ - For example, if you change line 9 to `x = 1 / 1`, PyTest will now fail the test, since the expected Exception was not raised. (and it will explain this in detail in the console!)

In `test_keyerror_details`, we also assign the exception to a variable using `as`, so that we can refer to it after the `pytest.raises` block - we can inspect it in more detail, or even `assert` that it has qualities we're expecting. Very helpful when you want to test for specific exception-raising behavior!

Finally, in `test_approximate_matches`, we use `pytest.approx` to help assert that our two values are "approximately" equal, even it's not exact, due to the challenges of floating point math. (We can also adjust how "close" the match needs to be for the test to pass - For more details, check out the [pytest.approx documentation](https://docs.pytest.org/en/latest/reference.html#pytest-approx).)

### Up Next:

[Review of the Basics](03_reviewing_the_basics.md)
