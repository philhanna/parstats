import pytest
from arstats import to_display_name, to_section_name, to_title_case

@pytest.mark.parametrize("gameName, expected", [
    ("freecell", "Freecell"),
    ("freecell.scm", "Freecell"),
    ("auld-lang-syne", "Auld Lang Syne"),
    ("", ""),
    ("a-short-name.scm", "A Short Name"),
])
def test_to_display_name(gameName, expected):
    actual = to_display_name(gameName)
    assert expected == actual

@pytest.mark.parametrize("gameName, expected", [
    ("freecell", "freecell.scm"),
    ("auld-lang-syne", "auld_lang_syne.scm"),
    ("", ""),
    ("Spider", "spider.scm"),
])
def test_to_section_name(gameName, expected):
    actual = to_section_name(gameName)
    assert expected == actual

@pytest.mark.parametrize("name, expected", [
    ("", ""),
    ("   ", ""),
    ("a", "A"),
    ("OK", "Ok"),
    ("OK ", "Ok"),
])
def test_title_case(name, expected):
    actual = to_title_case(name)
    assert expected == actual
