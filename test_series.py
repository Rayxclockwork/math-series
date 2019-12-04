from series import fib, lucas


def test_fibonacci(n):
    expected = 34
    actual = "9th value of fibonacci sequence"
    assert expected is actual, "The 9th value of Fibonacci is 34"

def test_lucas(n):
    expected = 18
    actual = "6th value of Lucas sequence"
    assert expected is actual, "The 6th value of Lucas is 18"

def test_sum_series():
    expected = 13
    actual = sum(5, 8)
    assert expected is actual, "sum of 5 and 8 should be 13"
