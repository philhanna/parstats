import configparser
import getpass
import os.path

import pytest

from parstats import DataProvider
from parstats import HEADER_SECTION, RECENT_ITEM


@pytest.fixture
def dp():
    return DataProvider()

def test_constructor_with_bogus_filename():
    with pytest.raises(FileNotFoundError):
        DataProvider("Bogus")

def test_constructor_with_default_filename(dp):
    assert dp is not None

def test_constructor_with_given_filename():
    filename = os.path.join("testdata", "aisleriot")
    dp = DataProvider(filename)
    actual = dp.config["Aisleriot Config"]["Recent"]
    assert "spider;freecell;canfield;klondike;" == actual
    
def test_get_default_filename(dp):
    dp = DataProvider()
    username = getpass.getuser()
    filename = dp.get_default_filename()
    assert filename is not None
    assert username in filename

@pytest.mark.parametrize("filename, expected, expected_error", [
    (os.path.join("testdata", "aisleriot"), ["spider", "freecell", "canfield", "klondike"], None),
    (os.path.join("testdata", "stooges.ini"), None, None),
    #(os.path.join("testdata", "non-existent.ini"), None, FileNotFoundError),
    #(os.path.join("testdata", "bogus.ini"), None, configparser.Error),
    #(os.path.join("testdata", "bogus2.ini"), None, configparser.Error),
])
def test_data_provider_game_list(filename, expected, expected_error):
    if expected_error:
        with pytest.raises(expected_error):
            DataProvider(filename)
    else:
        dp = DataProvider(filename)
        actual = dp.get_game_list()
        if actual:
            assert set(actual) == set(expected)