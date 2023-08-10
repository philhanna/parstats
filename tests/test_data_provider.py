import getpass
import pytest
from parstats import DataProvider

@pytest.fixture
def dp():
    return DataProvider()

def test_constructor_with_bogus_filename():
    with pytest.raises(FileNotFoundError):
        DataProvider("Bogus")

def test_constructor_with_default_filename(dp):
    assert dp is not None

def test_get_default_filename(dp):
    dp = DataProvider()
    username = getpass.getuser()
    filename = dp.get_default_filename()
    assert filename is not None
    assert username in filename