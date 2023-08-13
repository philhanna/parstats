import pytest
from arstats import Statistics

def test_accessors():
    ps = Statistics(45, 241, 479, 907)
    assert ps.wins() == 45
    assert ps.losses() == 196
    assert ps.total() == 241
    assert ps.best() == 479
    assert ps.average() == 693
    assert ps.worst() == 907
    assert ps.wins_to_next_higher() == 3
    assert ps.losses_to_next_lower() == 3

    ps = Statistics(0, 0, 0, 0)
    assert ps.wins() == 0
    assert ps.losses() == 0
    assert ps.total() == 0
    assert ps.best() == 0
    assert ps.average() == 0
    assert ps.worst() == 0
    assert ps.wins_to_next_higher() == -1
    assert ps.losses_to_next_lower() == -1

def test_statistics_from_string():
    tests = [
        ("current", "45;241;479;907;", [45, 241, 479, 907], False, ""),
        ("no games", "0;0;0;0;", [0, 0, 0, 0], False, ""),
        ("1 loss", "0;1;0;0;", [0, 1, 0, 0], False, ""),
        ("too few", "0;1;300;", None, True, "got 3"),
        ("too many", "0;1;300;45;241;479;907;", None, True, "got 7"),
        ("bad wins", "bogus;1;1;1;", None, True, "wins"),
        ("bad total", "1;bogus;1;1;", None, True, "total"),
        ("bad best", "1;1;bogus;1;", None, True, "best"),
        ("bad worst", "1;1;1;bogus;", None, True, "worst"),
    ]
    for tt in tests:
        name, line, expected, expected_error, expected_word = tt
        def inner_test():
            actual = Statistics.from_string(line)
            if expected_error:
                errmsg = str(actual)
                assert expected_word in errmsg
            else:
                assert actual is not None
                assert expected[0] == actual.wins()
                assert expected[1] == actual.total()
                assert expected[2] == actual.best()
                assert expected[3] == actual.worst()
        inner_test.__name__ = f"test_new_statistics_from_string_{name}"
        inner_test.__qualname__ = f"test_new_statistics_from_string.{name}"
        globals()[inner_test.__name__] = inner_test
