import pytest
from parstats import DataProvider


def test_constructor_with_bogus_filename():
    with pytest.raises(FileNotFoundError):
        DataProvider("Bogus")