def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    rst = 1
    while k > 0:
        rst *= n
        n -= 1
        k -= 1
    return rst



def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    # 1
    s = 0
    while y:
        s += y % 10
        y //= 10
    return s
    # 2
    s_y = str(y)
    l = len(s_y)
    s = 0
    while l > 0:
        s += int(s_y[l - 1])
        l -= 1
    return s



def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    # 1
    while n:
        if n % 100 == 88:
            return True
        n //= 10
    return False
    # 2
    s_n = str(n)
    i = 0
    l = len(s_n)
    while i < l - 1:
        if s_n[i] == s_n[i + 1] == '8':
            return True
        i += 1
    return False


