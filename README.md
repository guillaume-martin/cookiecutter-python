# python-project cookiecutter template

A [cookiecutter](https://github.com/cookiecutter/cookiecutter) template for new
Python projects using **Poetry**, **mypy**, **pre-commit** (with ruff), and pytest,
in a src layout.

## Usage

```bash
# From a local clone of this template
cookiecutter /path/to/python-project

# Or straight from the repo
cookiecutter gh:<user>/<repo>
```

Cookiecutter will prompt for each value (defaults in `cookiecutter.json`):

| Variable         | Default          | Used for                                  |
| ---------------- | ---------------- | ----------------------------------------- |
| `project_name`   | `Python Project` | README title                              |
| `project_slug`   | `python-project` | Output directory + Poetry package name    |
| `package_name`   | `python_project` | Importable package under `src/`           |
| `author_name`    | `Your Name`      | `pyproject.toml` authors                  |
| `author_email`   | `you@example.com`| `pyproject.toml` authors                  |
| `description`    | —                | `pyproject.toml` description              |
| `python_version` | `3.11`           | `python = ^...`, mypy, ruff target        |
| `version`        | `0.1.0`          | Initial `__version__`                     |

Non-interactive example:

```bash
cookiecutter --no-input \
  project_name="My App" \
  project_slug="my-app" \
  package_name="my_app" \
  /path/to/python-project
```

## Generated project

```
<project_slug>/
├── .gitignore
├── .pre-commit-config.yaml
├── pyproject.toml        # Poetry + mypy (strict) + ruff + pytest
├── README.md
├── src/<package_name>/__init__.py
└── tests/
    ├── __init__.py
    └── test_smoke.py
```

Then, inside the generated project:

```bash
poetry install
poetry run pre-commit install
```
