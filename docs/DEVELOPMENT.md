## Development _(of this project)_

### Installation

The package dependencies for this project are managed with Pipenv, and exported to `requirements.txt` for ease of install. Since this exercise is all about PyTest, `pytest` and a few core extensions are the main dependencies.

However, the additional tools in `dev_requirements.txt` may be useful if you are testing or maintaining the project itself:

* [tox]() is used to automate testing of the code in all the currently supported versions of Python

* [flake8]() is a pretty good linter, and readily supported by VS Code

### Virtual Environments

In the top level of the project, to create a virtual environment and install the default and development requirements, first create a virtual environment. I would recommend running a command like:
```
python3 -m venv .venv/
```

You can then activate this environment in a terminal by running:
```
source .venv/bin/activate
```

Though, assuming you have installed your virtual environment into your folder as described above, VS Code (usually) activates it automatically in new terminals. I find this very convenient!

### Dependency Management

After activating your virtual environment (if any, see above), install the required dev tools:
```
pip install -r docs/dev_requirements.txt
```

This includes `pip-tools`, which can be used to generate new versions of our top level requirements file:

```
pip-compile requirements.in
```

Or new versions of our dev requirements: _(in the docs/ folder:)_

```
pip-compile dev_requirements.in
```

I have also been experimenting with `uv`, a Rust-accelerated replacement for pip-compile: If you install `uv`, you can give this a try: _(in the docs/ folder:)_
```
uv pip compile dev_requirements.in -o dev_requirements.uv.txt
```
Which serves a similar purpose (identifying the newest compatible versions of all our dependencies as defined in `requirements.in`, and writing them, with explicit versions and dependency annotations, to `requirements.txt`), but is much, much faster...

### Testing (across Python versions)

As this project is implemented as a series of Pytest tests, "testing" mostly consists of ensuring that these tests run as expected in all supported versions of Python. I prefer using `tox` to automate this cross-version testing process.

In addition to installing `tox` (which is included in the dev requirements), you must also ensure that you have all the appropriate versions of Python installed and available for use - I strongly recommend using [pyenv](https://github.com/pyenv/pyenv) for this: For example, the following commands will install them:
```
pyenv install 2.7
pyenv install 3.6
pyenv install 3.7
pyenv install 3.8
pyenv install 3.9
pyenv install 3.10
pyenv install 3.11
```

And then this command will make sure that each version can be invoked directly:

```
pyenv global 2.7 3.6 3.7 3.8 3.9 3.10 3.11
```

You can then simply run `tox`, which will in turn run `pytest` under each version of python, and report the aggregated results (all tests must pass in all versions of Python in order for tox to consider a run successful):

```
tox
```

The list of supported Python versions is stored in `tox.ini`, and unfortunately there are some inconsistencies in how python version numbers are represented there. _(This format is also very different from how `pyenv` describes Python versions, so there is not currently a convenient way to specify the supported Python versions in one place.)_

The currently supported versions of Python should also be clearly "badged" at the top of [README.md](../README.md).

I have not officially added 3.12 support, as I had several different issues during my last attempt (circa Python 3.12.0a3), but I'd be happy to add it once things have stabilized.

### Continuous Integration

I have not yet attempted to set up a CI/CD system for this project, as it doesn't change very often _(and since it is literally **made of tests,** there is no clear separation to be made between unit and integration testing...)_

But this probably wouldn't be too difficult to implement if there was some interest in it?