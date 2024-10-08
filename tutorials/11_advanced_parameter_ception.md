## 11: Advanced Parameter-ception!

Let's try that again, but with our test case requiring on only one fixture (which, in turn, requires a second fixture):

[tests/11_advanced_params_ception_test.py](../tests/11_advanced_params_ception_test.py)


```
pytest -vs tests/11_advanced_params_ception_test.py
```

The end result is... almost identical, even though the approach is different.

Since our parameterized `coordinate_fixture` requires another parameterized fixture, `numbers_fixture`, we still get the Cartesian Product of both set of parameters, even though the test case itself only requires one of them.

And this relationship is still reflected in the names PyTest assigns to the tests being run: the letter from the "inner" fixture appears first, followed by the digit from the "outer" fixture it requires.

This can be a deceptively simple but powerful feature - You can essentially create "higher order fixtures" request each other, and use "layers" or "trees" of fixtures to further customize behavior, all without touching the test case itself.

For example, try uncommenting the commented section of code (lines 19 through 22) to enable a clever piece of filtering logic using the `pytest.skip` function, and run the test again...

Now the `coordinate_fixture` applies some extra logic about which parameter combinations should be used, without affecting `numbers_fixture`, or the test case.

This also demonstrates that PyTest responds to `skip` at any time - even if it's called inside of a fixture, before we've even gotten into a test case, allowing us to avoid any undesirable combinations. This is another hint to how PyTest works, internally: Our test case functions are merely specifications for the tests that PyTest will be running, and we can conditionally skip a test at any point before it completes (by passing or failing).

In this example, we've added our filtering logic to one of our parameterized fixtures... But we could further abstract this into a `letters_fixture`and `numbers_fixture` which yield parameters, and a third, more purpose-specific `coordinates_fixture` that depends on those, adds the filtering logic, and has no parameters of its own, with the test case depending on it only. If we expect to use our two parameterized fixtures separately, that might be an even better way of organizing them.

Finally, this can also serve as an example of how fixture dependencies are not entirely unlike an `import` - If you add the `number_fixture` as an argument for (and dependency of) `test_advanced_fixtureception` on line 25, what do you expect might happen?

While this seems like it could be problematic - The test case now depends on `number_fixture` twice, both directly with a named argument, and indirectly through `coordinates_fixture`'s dependency - PyTest is surprisingly cool about it.

You might expect this to result in `number_fixture` being invoked twice, doubling our resulting tests, or even multiplying them by another copy of our extra parameter... But PyTest recognizes that both dependencies refer to the same fixture, and that fixture (by default) is run once per test case, and so we get the same results as if our `number_fixture` was only referred to once.

### Up Next:

[Fixture Scoping](12_fixture_scoping.md)
