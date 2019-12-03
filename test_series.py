from series import fibonacci, lucas


def test_fibonacci():
    expected = 13
    actual = sum(5, 8)
    assert expected is actual, "sum of 5 and 8 should be 13"

def test_lucas():
    expected = 29
    actual = sum(11, 18)
    assert expected is actual, "sum of 11 and 18 is 29"
