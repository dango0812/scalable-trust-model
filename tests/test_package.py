import trustmodel


def test_package_exposes_installed_version() -> None:
    assert trustmodel.__version__ == "0.1.0"
