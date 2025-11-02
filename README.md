# Test Driven Developmen by Example Book Source


This repository contains the source code examples from the book "Test Driven Development by Example"
by Kent Beck.

The code is converted to Python from the original Java examples in the book.


## Requirements

- Python >= 3.12
- uv
- just (optional)


## Setting up

1\. Clone the repo

```shell
git clone https://github.com/cr8ivecodesmith/tdd-by-example.git
cd tdd-by-example
```

2\. Init virtualenv and install requirements

```shell
uv venv --clear
uv sync --group dev
```

3\. Run tests

```shell
uv run pytest
```

or

```shell
just test full
```
