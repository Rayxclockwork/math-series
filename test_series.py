import pytest
from series import fibonacci, lucas, sum_series


def test_fibonacci():
    expected = 34
    actual = fibonacci(9)
    assert expected == actual

# @pytest.mark.skip('pending')


def test_lucas():
    expected = 18
    actual = lucas(6)
    assert expected == actual

# @pytest.mark.skip('pending')


def test_sum_series():
    assert sum_series(9) == 34
    # expected = 21
    # actual = sum_series(9, first = 0, second = 1)
    # assert expected == actual
