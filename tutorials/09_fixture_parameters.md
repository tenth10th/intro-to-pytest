## 9: Fixture Parameters

When we decorate a callable as a Fixture, we can also give it some additional properties, like parameters, allowing us to do parameterized testing - And the `request` plugin (built-in fixture) we've covered previously will come in handy here as well.

In testing, we use parameterization to refactor and "automate" similar tests. Especially in unit testing, you may find yourself in a situation where you want to run the same code, with the same set of assertions (essentially, the same "test") with a number of different inputs and expected outputs.

It's possible to just have multiple inputs and outputs and assertions in our test case... But at the expense of making that test more complicated, and harder to understand when it fails: We'll see a single test case and assertion passing or failing, regardless of how many of the other assertions were valid...

So let's look at a better approach:

[tests/09_fixture_parameters_test.py](../tests/09_fixture_parameters_test.py)

```
pytest -vs tests/09_fixture_parameters_test.py
```

Here we only have one test case / function, with one fixture, but that fixture includes five parameters, "a" through "e". Because our test case requests a parameterized fixture, PyTest will run it repeatedly, once for each parameter, and it treats each of those as a distinct "test" (a.k.a. "item" or "node") that can pass or fail independently: We can clearly see how many of those parameters passed or failed, and it even labeled those tests with both the test case name, and the parameter being used.

 * (This is an interesting philosophical point: When we saw PyTest referring to "nodes" earlier, they seemed to correspond to our test functions... But it's more accurate to say that our test functions are merely "specifications" or  for tests PyTest, and the resulting nodes are the _real_ tests that Pytest is actually running. In this case, a single python function is resulting in multiple tests...)

PyTest will run our test cases (and their fixture) once per parameter: In our fixture, we're using the `request` plugin to access the current parameter value, as `request.param`, and in this example we're simply yielding that value.

And so our single test case is run a total of five times, once for each parameter value, with that value being passed in as the named argument corresponding to `letters_fixture`. (likewise for test_modes, which is called three times.)

 * It doesn't have to be this direct - Our fixture might use the parameter to customize an object, then yield that object to our test. (Or even yield a tuple of values that are derived from the parameter).

There is also a second parameterized fixture, `mode`, which uses a second keyword argument, `ids`, which allows the names of each parameter to be "labeled" in a more readable way. For example, the parameters are 1, 2, and 3, but we could label them as "foo", "bar", and "baz" on the individual tests. (this means the resulting tests will be called )

This is a lot! And this behavior gets even more interesting (and powerful) when we consider that fixtures can request other fixtures...

### Up Next:

[Parameter-ception!](10_parameter_ception.md)
