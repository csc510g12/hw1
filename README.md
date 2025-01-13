# Homework 1

![GitHub License](https://img.shields.io/github/license/ncsu-csc510-25spring/hw1)
![Python Language](https://img.shields.io/badge/Language-Python-blue)
![Platform](https://img.shields.io/badge/Platform-ArchLinux-fedcba)
![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/ncsu-csc510-25spring/hw1/.github/workflows/poetry-pytest.yml)
[![codecov](https://codecov.io/gh/ncsu-csc510-25spring/hw1/graph/badge.svg?token=UYR1AABQ80)](https://codecov.io/gh/ncsu-csc510-25spring/hw1)

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

## How To Collaborate

You can either choose to:

- Fork this repository:
  - Click on the fork button on the top right corner of this page.
  - Clone your forked repository to your local machine.
  - Add this repository as an upstream remote.
  - Add your code or make changes to the existing code.
  - Push your changes to your forked repository.
  - Create a pull request to the `main` branch of this repository.
- Create a new branch in this repository:
  - Clone this repository to your local machine.
  - Create a new branch and switch to that branch.
  - Add your code or make changes to the existing code.
  - Push your changes to this repository on your branch.
  - Create a pull request to the `main` branch of this repository.

Once you open a PR, contributor bot will add you into team member list below.

## Team Members

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://www.gong.host"><img src="https://avatars.githubusercontent.com/u/33346934?v=4?s=100" width="100px;" alt="Gavin Gong"/><br /><sub><b>Gavin Gong</b></sub></a><br /><a href="https://github.com/csc510g12/hw1/commits?author=visualDust" title="Code">💻</a> <a href="https://github.com/csc510g12/hw1/commits?author=visualDust" title="Tests">⚠️</a> <a href="https://github.com/csc510g12/hw1/commits?author=visualDust" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/azkuang"><img src="https://avatars.githubusercontent.com/u/117621443?v=4?s=100" width="100px;" alt="azkuang"/><br /><sub><b>azkuang</b></sub></a><br /><a href="https://github.com/csc510g12/hw1/commits?author=azkuang" title="Code">💻</a> <a href="https://github.com/csc510g12/hw1/commits?author=azkuang" title="Tests">⚠️</a> <a href="https://github.com/csc510g12/hw1/commits?author=azkuang" title="Documentation">📖</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
