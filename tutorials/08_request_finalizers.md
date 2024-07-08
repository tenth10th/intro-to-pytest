
## 8: Request "finalizer" Callbacks

Sometimes we want to run a "cleanup" function after testing is complete: We've already covered a very easy way to do this using `yield` [inside a fixture](), but noted that it's not the safest option, if anything goes wrong inside our fixture...

Fortunately, PyTest has a `request` plugin (a built-in global fixture) that, among other things, can be used to add a "finalizer", a function which is guaranteed to be called after the fixture (and the test(s) that request it) are run... Even in the worst case scenario, where our fixture itself fails:

[tests/08_request_finalizer_test.py](../tests/08_request_finalizer_test.py)

```
pytest -vs tests/08_request_finalizer_test.py
```

As usual, we can see that our fixture runs first (including a "risky" function call), followed by our test case, and finally our safe_cleanup function. One advantage of this approach is that we can re-use a shared cleanup function, but the main benefit is that even if our fixture fails to initialize, our finalizer "cleanup" function still gets run!

To really see the finalizer in action, uncomment line 11 in `08_request_finalizer_test.py` (e.g. the commented-out "raise Exception" call), and re-run the test using the command above.

That "risky" function didn't work out - it derailed our fixture, and our test case never even ran! But despite all that, our `safe_cleanup` function still got called. (you may have to scroll further up in the terminal to see this - the output of safe_cleanup will appear before the resulting Error is unpacked.)

In a real test, with a fixture that sets up something complicated or expensive (and might fail _after_ it has made some kind of a mess), guaranteed cleanup could be a really important feature!

If you've ever used a Context Manager, this is a similar idea - much like how the `__exit__()` method is guaranteed to be called when exiting the context, even in the event of an error, the request finalizer will be called after the fixture's scope, even if the fixture or test raised an exception...

* It's possible to add multiple finalizers to a fixture - In that case, each of them will run after the test case that requested the fixture, regardless of how successful the fixture or test case was

* If you add multiple request finalizers, it is possible for them to fail independently. Any errors during a test (from the test, fixture, or finalizers) will cause that test to Fail... but Pytest will attempt to call all the finalizers that have been added, even if the test, fixture(s), or other finalizer(s) have already raised Exceptions!

There's one more major feature of fixtures that we haven't covered yet, and it's a very powerful one...

### Up Next:

[Fixture Parameters](09_fixture_parameters.md)
