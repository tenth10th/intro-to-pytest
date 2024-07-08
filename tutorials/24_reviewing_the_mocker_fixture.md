## 24: Reviewing The Mocker Fixture

* PyTest is compatible with the `mock` objects and `patch` function from Python's built in `unittest.mock` module

* The `pytest-mock` extension enhances this further, by providing a globally available `mocker` fixture that automatically scopes mocks to the tests they're used in

* In addition, you can create your own fixtures that depend on `mocker`, and build and customize a Mock object before returning it - This makes it easier to "share" the same initial mock configuration across multiple tests.

* PyTest will create Mocks on demand - by default, a new Mock object will be created for each Test that relies on `mocker`, and they will be disposed of after the test ends. (This behavior extends to fixtures that use `mocker` to create, configure, and return a Mock.)

