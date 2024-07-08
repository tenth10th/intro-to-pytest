## 5: Fixture Returns

Beyond simply printing a message, a fixture can also return data, just like a regular function:

[tests/05_fixture_returns_test.py](../tests/05_fixture_returns_test.py)

```
pytest -vs tests/05_fixture_returns_test.py
```

When PyTest runs our test, which requests a fixture, it not only calls the `one_fixture()` function first, it also captures the return value (in this case, an integer, `1`), and passes it into our test function as the `one_fixture` argument.

So we can make assertions about what our fixture is returning, or use it in any other way we'd like during our test. And by default, PyTest calls our fixtures for each test that requests them, so we are guaranteed that each test is getting a new, "fresh" instance of what our fixture returns.

_(It doesn't make much of a difference for fixtures that return static data, but imagine a fixture that returns a List, Dict, or other mutable Object, that might be altered during a test?)_

This helps take care of test case "setUp" scenarios, but what about "tearDown"? (If you aren't familiar with xUnit, the "setUp" method is run before each test, and the "tearDown" method is called afterwards, and typically used to clean up after a test.)

### Up Next:

[Yield Fixtures](06_yield_fixtures.md)
