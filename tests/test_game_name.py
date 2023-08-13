import pytest
from arstats import title_case

@pytest.mark.parametrize("name, expected", [
    ("", ""),
    ("   ", ""),
    ("a", "A"),
    ("OK", "Ok"),
    ("OK ", "Ok"),
])
def test_title_case(name, expected):
    assert title_case(name) == expected