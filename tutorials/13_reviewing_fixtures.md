## 13: Reviewing Fixtures

* Fixtures are PyTest's mechanism for controlling the "context" around your test cases, and for setting up and tearing down resources required by a test.

    * _(later, we'll talk more about using fixtures to manage Mocks, a particularly tricky and dangerous resource...)_

* PyTest comes with a number of [built in fixtures](https://docs.pytest.org/en/latest/reference.html#fixtures) for general use. (You will also likely want to create your own, to reflect what resources your code needs in order to be tested...)

* Test cases can request a fixture (i.e. express a "dependency" on it) by having named arguments:

    * Remember, Pytest will be calling our test cases - the simple case is for tests to not have arguments.

    * If they _do_ have arguments, Pytest looks for fixtures whose name matches the argument name, and calls them

        * _(Test cases will fail if their named arguments don't correspond to valid fixtures!)_

        * _(You can run `pytest --fixtures` for a reminder of what named fixtures are available)_

    * The value returned by your fixture (if any) will be passed into the test case, as that named argument

* You can implement "setUp" and "tearDown" functionality for your fixtures in two ways:

    * If your fixture uses `yield`, the code up to and including the `yield` will be run before the test (with the value being yielded being passed in to the test case). Any code after the `yield` will be

        * `yield` is generally simpler, and more readable, and prefered for simpler use cases. (Keeping your fixtures small, and limiting them to a "single job" helps address these concerns - Multiple simple fixtures are preferable to a single complicated fixture that can fail at different points!)

    * The built-in `request` fixture allows you add finalizer function(s) to a fixture - These are guaranteed to be run after any test case that the fixture is used with, regardless of whether the test based or failed (or even if the fixture itself failed... or even if other finalizer functions failed!)

        * `request.addfinalizer()` is more verbose, and more complicated, but worth it when a fixture is necessarily complicated, or has resources that **must** be cleaned up. (It's even better to avoid this situation, if you can - But sometimes it may be necessary.)

* Fixtures are typically functions with the `@pytest.fixture` decorator:

    * By default, fixtures have "function scope", and will be called once per test case that requests them: If the fixture returns an object, each test will get a new, "fresh" instance of that object.

    * We can pass a named `scope` argument to the `@pytest.fixture()` decorator:

        * `fixture(scope="module")` limits the fixture to being called once per module (python file) where it is requested, and the return value will be reused for each test case in that module. This can help your tests run faster, if a fixture is expensive or time consuming to run.

        * `fixture(scope="session")` limits the fixture to being called once for this whole Pytest run - This is an even more extreme limitation, for extremely expensive fixtures!

        * At `module` and `session` scope, the fixture is called before the first test that requests it, and any cleanup happens after the conclusion of the last test that requests it (in that Module, or across the whole Pytest run, respectively).

    * Fixtures with parameters (`params`) can cause multiple tests (a.ka. "items" or "nodes") to be created out from a given test case - These "parameterized" tests can pass or fail independently, and are named after the parameters.

        * _(When Pytest says it has collected 72 "items", this the number of tests it will actually run - This counts the test cases you've created directly in code, as well as additional tests defined as parameters to those test cases...)_

        * _(You can run `pytest -v` for more verbose output, including the names of each test being run - for "parameterized" tests, this will be the name of the test case, followed by the parameters in square brackets, e.g. `test_parameters[a]`)

* Fixtures can be defined "locally", in the same module as the test cases that use them, or "globally" in a `conftest.py` file. (In the event of multiple implementations of a given fixture name, PyTest will prefer the "most local" one, e.g. the fixture located closest to the test case in your file structure.)

    * It's generally simpler and more readable to keep fixtures "local" to the tests that use them...

    * It's also generally simpler to have a single `conftest.py` at the top level of your repository, unless you have a large number of shared fixtures

    * _(While it is possible to have multiple fixtures with the name name, which can override each other based on "distance" to a test, this is a really confusing feature -  you should probably avoid using it unless absolutely necessary!)_

* Fixtures can get "very meta":

    * Fixtures can request on each other, and can access the values that are returned or yielded by other fixtures

        * This allows you to keep your fixtures simple - Ideally each fixture should have one "job"

        * Complicated collections of fixtures can be kept simple, allowing test cases to call into the "tree" of requests where necessary

    * Fixture requests are similar to `import`s, in that a requested fixture will only be invoked once, even if multiple fixtures have the same dependencies:

        * If Fixture A requests fixture B and fixture C...

        * And Fixture B also requests fixture C...

        * Then a test case requests the A fixture, the C fixture will only be called once!

        * (even if a test case explicitly requests A, B, and C, each fixture will still only be called once!)

    * If a test case depends on multiple fixtures that have parameters, or parameterized fixtures depend on each other, the affected test cases will be called with the full cartesian product of all the parameters (e.g. every combination of all the fixture parameters).
        
        * If you have a Letters fixture ["A", "B"]
        * And a Numbers fixture [1, 2]
        * A test case `test_with_params` that requests both fixtures will result in four "parameterized" tests:
            * `test_with_params[A-1]`
            * `test_with_params[A-2]`
            * `test_with_params[B-1]`
            * `test_with_params[B-2]`

Fixtures are very complicated, but ultimately very powerful - we've really only scratched the surface here, but hopefully this gives you an overview of what they can do for your tests!

_(Coming soon: More examples of fixture use cases)_

For now, let's move on to another powerful concept...

### Up Next:

[Introduction to Test Marking](14_intro_to_test_marking.md)