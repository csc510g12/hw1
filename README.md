# Homework 1

![GitHub License](https://img.shields.io/github/license/ncsu-csc510-25spring/hw1)
![Python Language](https://img.shields.io/badge/Language-Python-blue)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Code style: pylint](https://img.shields.io/badge/code%20style-pylint-yellowgreen)](https://pylint.pycqa.org/)
![Platform](https://img.shields.io/badge/Platform-ArchLinux-fedcba)
![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/ncsu-csc510-25spring/hw1/.github/workflows/poetry-pytest.yml)
[![codecov](https://codecov.io/gh/ncsu-csc510-25spring/hw1/graph/badge.svg?token=UYR1AABQ80)](https://codecov.io/gh/ncsu-csc510-25spring/hw1)
[![DOI](https://zenodo.org/badge/913940479.svg)](https://doi.org/10.5281/zenodo.14665061)

## How to setup

if you are using environment manager like `conda` or `virtualenv` please activate your environment first.

install poetry

```bash
pip install poetry
```

install dependencies

```bash
poetry install
```

initialize pre-commit

```bash
pre-commit install
```

## Adding Python Unit Tests

To add a new unit test, create a new file in the `tests` directory. The file should be named `test_<module_name>.py` where `<module_name>` is the name of the module you are testing. For example, if you are testing the `hw1` module, the file should be named `test_hw1.py`.

Run the tests using the following command:

```bash
poetry run pytest
```

you will see some tests passed and some failed. You can see the failed tests by scrolling up in the terminal.

## Team Members

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://www.gong.host"><img src="https://avatars.githubusercontent.com/u/33346934?v=4?s=100" width="100px;" alt="Gavin Gong"/><br /><sub><b>Gavin Gong</b></sub></a><br /><a href="https://github.com/csc510g12/hw1/commits?author=visualDust" title="Code">💻</a> <a href="https://github.com/csc510g12/hw1/commits?author=visualDust" title="Tests">⚠️</a> <a href="https://github.com/csc510g12/hw1/commits?author=visualDust" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/azkuang"><img src="https://avatars.githubusercontent.com/u/117621443?v=4?s=100" width="100px;" alt="azkuang"/><br /><sub><b>azkuang</b></sub></a><br /><a href="https://github.com/csc510g12/hw1/commits?author=azkuang" title="Code">💻</a> <a href="https://github.com/csc510g12/hw1/commits?author=azkuang" title="Tests">⚠️</a> <a href="https://github.com/csc510g12/hw1/commits?author=azkuang" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/odesai840"><img src="https://avatars.githubusercontent.com/u/77876944?v=4?s=100" width="100px;" alt="Ohm Desai"/><br /><sub><b>Ohm Desai</b></sub></a><br /><a href="https://github.com/csc510g12/hw1/commits?author=odesai840" title="Code">💻</a> <a href="https://github.com/csc510g12/hw1/commits?author=odesai840" title="Tests">⚠️</a> <a href="https://github.com/csc510g12/hw1/commits?author=odesai840" title="Documentation">📖</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
