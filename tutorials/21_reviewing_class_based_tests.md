## 21: Reviewing Class-Based Tests

* While Pytest allows you to write function-based tests (which are recommended!) it also supports Class based tests...

* (This includes old style tests, as created using Python's built in `unittest` framework, as well as tests whose class and method names follow Pytest's naming convention, even if they don't use the `unittest` decorators)

* Class-based tests may be helpful in organizing data and resources used in a test - though [Pytest Fixtures](04_intro_to_fixtures.md) are a powerful and often more flexible way to accomplish similar things, with less code

* You can still use Fixtures and Marks in class-based tests, and can apply them to the parent Class, as well as the methods. (this is potentially _yet another_ way to apply fixtures automatically across groups of tests!)

* If you're a fan of Behavior Driven Design, and BDD tests, you may find Class-based tests appealing, especially when combined with a BDD plugin for PyTest - though there are [PyTest BDD frameworks](https://pypi.org/project/pytest-bdd/) that do not require class-based tests as well

### Up Next:

PyTest also integrates with the `unittest.mock` module, and there's an excellent plugin to make this even easier:

[The Mocker Fixture](22_the_mocker_fixture.md)
