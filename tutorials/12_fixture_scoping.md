## 12: Fixture Scoping

We've observed that, by default, fixtures are called once per test case that requests them.

Let's change that! The `@fixture` decorator can actually take arguements, and one of them is `scope`:

[tests/12_scoped_and_meta_fixtures_test.py](../tests/12_scoped_and_meta_fixtures_test.py)

```
pytest -vs tests/12_scoped_and_meta_fixtures_test.py
```

While both test functions request the `scoped_expensive_fixture`, it has been scoped to the "module" level - It only will be instantiated once for all the tests in this module (python file).

To make the ordering even clearer, `scoped_expensive_fixture` is a "yield fixture" - We can see that the initial setup happens before any of the tests run, and the "post-yield" section runs after all the tests in the module have run. And we can see that each test is recieving the same shared instance of `ExpensiveClass`.

The other available scope is "session": This will limit the fixture to being instantiated once for this whole run of Pytest. What do you think will happen if we change `scope` to "session" on line 6?

### Up Next:

[Review of Fixtures](13_reviewing_fixtures.md)
