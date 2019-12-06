
def fibonacci(n):
    """Finds value of Fibonacci sequence at nth index"""
    return sum_series(n)


def lucas(n):
    """Finds value of Lucas at nth index"""
    return sum_series(n, 2, 1)


# optional values of (0,1) or (2,1) for fib or lucas
def sum_series(n, first=0, second=1):
    """Finds the sum of sequence up to the nth value"""

    if n == 0:
        return first

    if n == 1:
        return second

    return sum_series(n-1, first, second) + sum_series(n-2, first, second)
