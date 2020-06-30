# Testing Python project

You would need these packages

- pytest
- pytest-cov
- coverage

## Run Pytest at command line

```shell script
pytest ./test/unit/calculate_test.py
```

## Code Coverage

```shell script
coverage run --source=app -m pytest ./test/unit/calculate_test.py
coverage report -m
```

The structure should look like this:

```text
.
├── app
│   ├── calculate.py
│   ├── calculate.pyc
│   ├── __init__.py
│   ├── __init__.pyc
│   └── __pycache__
│       ├── calculate.cpython-36.pyc
│       └── __init__.cpython-36.pyc
├── __init__.py
├── readme.md
└── test
    └── unit
        ├── calculate_test.py
        ├── __init__.py
        ├── __init__.pyc
        └── __pycache__
            ├── calculate_test.cpython-27-PYTEST.pyc
            ├── calculate_test.cpython-36-pytest-5.4.3.pyc
            └── __init__.cpython-36.pyc

5 directories, 14 files
```