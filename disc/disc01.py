def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    return temp < 60 or raining

def square(x):
    print('here!')
    return x * x

def so_slow(num):
    x = num
    while x > 0:
        x += 1
    return x / 0

def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    x = n - 1
    while x > 1:
        if n % x == 0:
            return False
        x -= 1
    return True
