## 19: PyTesting with Classes

We've established that you don't _need_ to write Classes when using PyTest, and in many cases, it isn't necessary.

But we also mentioned that PyTest will discover and run Class-based tests, such as those created using Python's built in `unittest` module. And there are a few features and behaviors which come along with Class-based testing. Let's see what a Class-based test might look like in PyTest:

[tests/19_class_based_test.py](../tests/19_class_based_tests.py)

```
pytest -vs tests/19_class_based_tests.py
```

_(More detailed tutorial coming soon - in the meantime, check out the code above)_

### Up Next:

[Advanced Class-Based Tests](20_advanced_class_based_tests.md)
