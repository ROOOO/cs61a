def multiply(m, n):
    """
    >>> multiply(5, 3)
    15
    """
    if n == 1:
        return m
    return multiply(m, n - 1) + m

def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(n)
    if n == 1:
        return 1
    if n & 1 == 0:
        return 1 + hailstone(n // 2)
    else:
        return 1 + hailstone(n * 3 + 1)

def merge(n1, n2):
    """Merge two numbers
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge(21, 31)
    3211
    """
    if n1 == 0:
        return n2
    if n2 == 0:
        return n1
    last1 = n1 % 10
    last2 = n2 % 10
    if last1 < last2:
        return last1 + 10 * merge(n1 // 10, n2)
    else:
        return last2 + 10 * merge(n1, n2 // 10)

def make_func_repeater(f, x):
    """
    >>> incr_1 = make_func_repeater(lambda x: x + 1, 1)
    >>> incr_1(2) # same as f(f(x))
    3
    >>> incr_1(5)
    6
    """
    def repeat(n):
        if n == 0:
            return x
        else:
            return f(repeat(n - 1))
    return repeat

def is_prime(n):
    """
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """
    def prime_helper(k):
        if n == k:
            return True
        elif n <= 1 or n % k == 0:
            return False
        else:
            return prime_helper(k + 1)
    return prime_helper(2)
