## 18: Reviewing Marks

* Marks are PyTest's mechanism for marking or "tagging" test cases, to categorize them, or change their behavior

* Marks can change test behavior, skipping them, allowing or requiring them to fail, or applying settings to all the tests in a module

* Marks can be used to categorize tests, and combined with command line switches to run or not run some tests

* Marks can also be used to parametrize a test - essentially an "inline" version of a [parameterized fixture](09_fixture_parameters.md)

* Marks can be used on individual tests, or, by creating a `pytestmark` object, applied to all the tests in a file!

### Up Next:

While you don't _need_ to write tests as Classes in PyTest, it is possible:

[Class-Based Tests](19_class_based_tests.md)
