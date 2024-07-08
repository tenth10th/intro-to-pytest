## 23: Re-Usable mock fixtures

In addition to using the `mocker` fixture extension directly, you can also create new fixtures that rely on it - This maintains the simpler interface to creating (and managing) mocks, still allows you to control the scope, and can be very helpful if you want to use the same "base" Mock in multiple tests. (Mocks can be reconfigured - but by default, you'll get a new "copy" in each test that uses them.)

[tests/23_re_usable_mock_test.py](../tests/23_re_usable_mock_test.py)

```
pytest -vs tests/23_re_usable_mock_test.py
```

_(More detailed tutorial coming soon - in the meantime, check out the code above)_

### Up Next:

[Reviewing the Mocker Fixture](24_reviewing_the_mocker_fixture.md)
