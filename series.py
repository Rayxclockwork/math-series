
def fib(n):
    if n<0:
        print("Incorrect input")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def lucas(n):
    if n < 0:
        print("incorrect input")
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)


#optional values of (0,1) or (2,1) for fib or lucas
def sum_series(n, first = 0, second = 1):

    for i in range(n+1):
      if n < 0:
        print("incorrect input")
      elif n == 1:
        return first
      elif n == 2:
        return second
      else:
        return sum_series(n-1) + sum_series(n-2)
