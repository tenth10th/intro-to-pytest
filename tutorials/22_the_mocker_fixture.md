## 22: The Mocker Fixture

PyTest is compatible with the `Mock` objects and `patch` features from Python's `unittest.mock` module. However, there is an additional fixture, installable as a plugin, that makes them a lot easier to manage.

The `pytest-mock` extension adds a built-in `mocker` fixture, which allows you to create mocks, and automatically manage them in the scope of a test:

[tests/22_the_mocker_fixture.py](../tests/22_the_mocker_fixture_test.py)

```
pytest -vs tests/22_the_mocker_fixture_test.py
```

_(More detailed tutorial coming soon - in the meantime, check out the code above)_

### Up Next:

The `mocker` fixture extension is also handy for creating re-usable mocks across multiple tests:

[Re-Useable Mocker Fixtures](23_re_useable_mocker_fixtures.md)
