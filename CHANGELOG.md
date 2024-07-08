# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2024-07-08

### Added

- This Changelog, for clearer accountability re: changes and revisions going forward

- Official support (and tox coverage) for Python versions up to 3.11

- _(Forked to this new repo, as a workaround to the original version becoming unmaintained)_

### Changed

- Updated to a more respectable version of pytest (8.0.X)

- Rewrote many tutorials to reflect the current preferred language used in the PyTest documentation. (To be fair: this tutorial was originally written in 2018...)

- Renumbered test content to be more "tutorial-centric": Tutorial steps are continuously numbered from 1 to 23, while tests are numbered to reflect the tutorial step they're associated with. (There are some gaps in Test numbering, as some Tutorial steps are reviews and do not have associated tests.)

- Links between tutorial steps and tests are now github-style relative URLs

- Parameter and Mark tutorial steps have been re-organized and re-named, hopefully introducing concepts in a more intuitive order

- Fixture features are introduced in a new, hopefully more inuitive order: Simple Fixtures, Fixture Returns, Yield Fixtures, The Request Fixture, Request Finalizers, Fixture Parameters, Param-Ception, Advanced Param-Ception, Scoped and Meta Fixtures

- Mark features are introduced in a new, hopefully more inuitive order: Built-in Marks, Custom Marks, Mark Parameterization, Marked Meta-Fixtures

## [1.0.0] - 2021-03-22

The _(unmaintained as of 2024)_ version of this project from https://github.com/pluralsight/intro-to-pytest.

_(this release was never explicitly versioned, but referring to it as 1.0.0 here for reference...)_