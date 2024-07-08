## 20: Advanced Class usage

In addition to more standard `unittest` style behavor, you can also use fixtures and marks on class test methods, and they behave much like you might expect. (In addition to making individual test methods, you can also mark the class itself, which will apply to all the test methods on that class):

[tests/20_advanced_class_test.py](../tests/20_advanced_class_based_tests.py)

```
pytest -vs tests/20_advanced_class_based_tests.py
```

_(More detailed tutorial coming soon - in the meantime, check out the code above)_

### Up Next:

[Reviewing Class-Based Tests](21_reviewing_class_based_tests.md)
