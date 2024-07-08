## 6: Yield Fixtures

Here's a more complicated fixture that uses the `yield` keyword - You may be more accustomed to seeing it used in generator functions, which are typically called repeatedly (e.g. iterated) to deliver their values.

If this seems confusing (or if you aren't familiar with `yield`), don't worry: This is a little different, but the important thing to understand is that `yield` is a lot like `return`, except for one interesting difference...

[tests/06_yield_fixture_test.py](../tests/06_yield_fixture_test.py)

```
pytest -vs tests/06_yield_fixture_test.py
```

Like last time, our fixture ran before the test case that requested it... Up until the point that we called `yield`. Then our test was run, receiving the "yielded" value as an argument... And then, _after_ the test finished, our fixture picked up where it left off, and ran the rest of the code (on line 20, after the `yield` call).

This allows us have both pre-test and post-test actions, with a minimum of code! But there are a few things to keep in mind:

 * Unlike a typical generator, our yield fixtures should never yield more than once. _(And PyTest enforces this - try adding a second yield and see what happens: Spoiler Alert! As with many of our hypothetical questions, the result is an unusable test)._

    * If this doesn't match up with what you expect from Generators, don't worry about it - Fixtures _can_ be generators, and PyTest will use them accordingly, but it expects them to yield exactly once, and that it will perform the first generation before the test case, and the second generation (the "cleanup" code after the `yield`) after the test case completes.

    * In older versions of Pytest, additional `yield`s will simply never be reached - In newer versions of Pytest, additional `yield`s will result in the test immediately failing! TLDR: Don't yield more than once in a Pytest fixture.

 * There is a corner case to be aware of here: If something goes wrong _inside_ our fixture, such that an unhandled exception is thrown before we call `yield`, we'll never get to the post-yield code... Kind of understandable, if you think about it!
 
    * This may not be a serious concern - it also means we won't actually run the test cases that request on our broken fixture, so perhaps the post-test cleanup may not be as vital?
    
    * This doesn't totally ruin our test run, either - The test cases that request on the broken fixture will fail during "setup", but PyTest will continue to run other tests.
 
    * (If this seems like it might be problematic for some use cases, don't worry: We'll cover "request finalizers" later, a more thorough, context-manager-like cleanup option.)

### Up Next:

[Request Fixtures](07_request_fixtures.md)