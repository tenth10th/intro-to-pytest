# intro-to-pytest

[![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)](https://www.python.org/downloads/release/python-2718/)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-3615/)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-3716/)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-3816/)
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-3916/)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3109/)
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3111/)

_(I have reluctantly forked this repo, as I no longer have access to maintain the [original version](https://github.com/pluralsight/intro-to-pytes) - Please feel free to merge my changes back in, version if you have the permission to do so!)_

An introduction to PyTest with lots of simple, hackable examples, currently compatible with Python 2.7 and 3.6+ (up to 3.11).

These examples are intended to be self-explanatory to a Python developer, with minimal setup - In addition to your preferred version of Python, you'll also need `pytest` and the `pytest-mock` plugin installed to use all these examples, which you can install by running:

```
pip install -r requirements.txt
```

in this folder - ideally, inside a virtual environment, to keep this from affecting your local Python libraries. _(Consider using [venv](https://docs.python.org/3/library/venv.html) or another virtual environment manager of your choice.)_

Once you've got all the requirements in place, you should be able to simply run

```
pytest
```

In this folder, and see 77 items being collected, and 72 tests passing _(with a few skipped or in other special statuses, which is intentional - more on that later...)_

PyTest will list the names of each test module file that it found, and then a period for each test case that passed, or other symbols for tests that failed, were skipped, etc.

But if you're seeing all that, congratulations! You're ready to get started.

The recommended approach is to read each example file, then run it directly with pytest, with the `v` flag (so that each Test Case is listed "verbosely", by name) and the `s` flag, so that we can all the standard output (prints) from the Tests, which will help explain how each example is working; PyTest normally captures and hides this output, except for tests that are currently failing. (In the examples below, we'll shorten these arguements to `-vs`.)

Each example test was intended to be self-explanatory, but I have begun adding short tutorial guides to explain more of the context, suggest experiments and hacks you can attempt on th examples, and to provide recaps and reviews for each major section. The tutorial track starts with:

[Tutorial Zero: An Empty Test](tutorials/00_empty_test.md)

Not all of the examples have an accompanying tutorial (yet), but were written to be self-explanatory, and should at least include basic comments to explain the feature being demonstrated.

If you have any feedback, questions, or PyTest features you'd like to see covered, please let [me](https://github.com/tenth10th) know via [GitHub Issues](https://github.com/pluralsight/intro-to-pytest/issues) or a Pull Request. As I am no longer with Pluralsight, it has become somewhat more difficult to maintain this project = but since it is open source (and still seems popular) I am working with some former co-workers to keep it maintained. Thanks for your patience!

More information on how to test and develop in this project is now available in the [Development](docs/DEVELOPMENT.md) doc.