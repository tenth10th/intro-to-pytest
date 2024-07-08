## 0: An Empty Test

The first test is pretty boring: It is a module (.py file) with "test" in the name, containing a callable (in this case, a plain old function) which also has "test" in the name, that doesn't really do anything - Aside from demonstrating how Pytest identifies tests.

[tests/00_empty_test.py](../tests/00_empty_test.py)

```
pytest -vs tests/00_empty_test.py
```

This is about as minimal as a PyTest test case can get - It doesn't assert anything. It doesn't really do anything interesting at all! But since it also doesn't raise any Exceptions, it results in a passing test.

Among other things, this demonstrates that we can use PyTest tests to simply "exercise" our code, even if we don't assert anything specific about the behavior (beyond it not being "broken"), in the sense that it does not raise any unhandled Exceptions or Errors.

This is also an example of how PyTest decides what is and is not a test: By default, it looks in for callables (such as functions or methods) whose names begin with "test". And earlier, when we ran it without any arguments, it searched for tests in all the modules (`.py` files) whose name started with "test_" or ended with "_test", by default, and it searched through the all the subfolders of our repo to find them.

If you take a look at the file, you'll see that PyTest _did_ run the `test_empty` function, since its name starts with "test", but it chose not to run the `empty_test` function, since it contains the word "test", but does not start with it.

All of these "test discovery" behaviors [can be overidden or extended](https://pytest.org/en/8.0.x/example/pythoncollection.html#changing-naming-conventions), if you want, but I recommend at least starting with PyTest's defaults. (They tend to be pretty reasonable, and following standard conventions will make your project easier for other developers to understand.)

While it's a start, this test doesn't really prove much - let's fix that!

## Up Next:

[Basic Tests and Assertions](01_basic_test.md)
