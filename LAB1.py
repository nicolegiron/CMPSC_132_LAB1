#Lab #1
#Due Date: 01/30/2021, 11:59PM

"""
    Collaboration Statement:

"""

def lowerFactorial(x, n):
    """
        >>> lowerFactorial(4, 2)
        12
        >>> lowerFactorial(34, 3)
        35904
        >>> lowerFactorial(0, 45)
        >>> lowerFactorial(4, -2) is None
        True
        >>> lowerFactorial(5.67, 4)
    """
    factorial = x
    if n < 0 or x < n or type(x) != int or type(n) != int:
      return
    while n > 1 and x > n:
      factorial *= (x-1)
      n-=1
      x-=1
    return factorial
