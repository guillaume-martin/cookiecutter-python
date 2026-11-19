import {{ cookiecutter.package_name }}


def test_version() -> None:
    assert {{ cookiecutter.package_name }}.__version__ == "{{ cookiecutter.version }}"
