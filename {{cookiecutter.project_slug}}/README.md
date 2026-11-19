# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Setup

```bash
# Install dependencies (creates the virtualenv automatically)
poetry install

# Install pre-commit hooks
poetry run pre-commit install
```

## Daily workflow

```bash
# Run tests
poetry run pytest

# Type check
poetry run mypy

# Lint + format
poetry run ruff check --fix
poetry run ruff format

# Run all pre-commit hooks on all files
poetry run pre-commit run --all-files
```

## Layout

```
src/{{ cookiecutter.package_name }}/   # package source (src layout)
tests/                                # pytest test suite
```
