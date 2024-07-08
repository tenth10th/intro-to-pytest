## 14: Introduction to Test Marking

PyTest includes a "mark" decorator, which can be used to tag tests and other objects with special properties.

Several marks are pre-defined in PyTest, and can be used to change how tests are interpreted: If a test is failing for known or expected reasons, we can mark it to indicate those reasons. (This is ideally better than simply deleting or commenting out the test - it won't pass or fail in the usual way, but it still be counted and listed). Hopefully, these marks will be applied temporarily, if at all, and I strongly recommend including a "reason", to help you (and others) understand how they should be fixed.

Here are some tests with built-in marks already applied:

[tests/14_built_in_marks_test.py](../tests/14_built_in_marks_test.py)

Let's see what happens when we run them:

```
pytest -vs tests/14_built_in_marks_test.py
```

Interestingly, no tests passed, but this didn't count as an overall failure! The counts in the Pytest output indicate that two tests were "skipped", 2 were "xfailed" (expected or allowed to fail), and 1 was "xpassed":

* `skip` prevents the test from being run, though it is still listed, and the result is counted as "skipped" rather than "passed" or "failed". (You can provide a "reason", which will be printed along with the name of the test in verbose mode: Ideally, use this to summarize why you're skipping it, and what needs to be done to fix it.)

* `ifskip` skips the test if a condition is true - this can make skipping dynamic, based on configuration or other state within your application or tests...

* `xfail` will "accept" failures - the result of the test will be listed as XPASS if it passes, or XFAIL if it fails, to indicate that failure is accepted, but that the outcome is still tracked. Again, it's best to include a "reason" why you're using this feature!

* `xfail` with `strict=True` will essentially reverse the normal pass/fail logic! The test is now _required_ to Fail, and so XFAIL is considered successful, but XPASS will actually be treated as an error! This is hopefully something you only need to do temporarily, until you can rewrite or otherwise correct a test to reflect a change in behavior. (And again, the "reason" option can help record the context for future reference...)

There are a few more built-in marks (also ) but we'll cover them later in this section.

### Up Next:

In addition to the built-in marks, you can also define your own custom Marks for categorization purposes:

[Custom User-Defined Marks](15_custom_marks.md)
