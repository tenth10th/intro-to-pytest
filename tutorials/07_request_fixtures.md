## 7: The "request" fixture

Fixtures are very powerful, not only because PyTest can run them automatically, but because they can be "aware" of the context in which they're being used!

(And also, as we're about to see, Fixtures can requst other Fixtures, allowing for some really interesting behavior...)

In this example, we'll write a fixture which leverages the built-in `request` fixture (aka a "Plugin", a standard fixture that is globally available to all PyTest tests) which, as the name suggests, lets the fixture introspect into how it is being requested. Essentially, the fixture can learn more about where and how it's being invoked:

[tests/07_request_test.py](../tests/07_request_test.py)

```
pytest -vs tests/07_request_test.py
```

Among other things, `request` allows our fixture to tell that it's being invoked with function-level scope (e.g. it is being instantiated per function that requests on it), it knows which "node" it's currently running on (in a dependency tree sense: It knows which test case is currently calling it), and it knows which Module it's being run in, which in this case is the `06_request_test.py` file.

This is a very powerful feature - our fixtures are simple functions, but `request` allows them to "react" to how they are being used.

In addition to providing context, the `request` fixture can also be used to influence PyTest's behavior as it runs our tests...

### Up Next:

[Request "finalizer" Callbacks](08_request_finalizers.md)