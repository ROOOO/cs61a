def count_stair_ways(n):
    """
    >>> count_stair_ways(1)
    1
    >>> count_stair_ways(2)
    2
    >>> count_stair_ways(3)
    3
    """
    if n == 1:
        return 1
    if n == 2:
        return 2
    return count_stair_ways(n - 1) + count_stair_ways(n - 2)


def count_k(n, k):
    """
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    if n < 0:
        return 0
    if n == 0:
        return 1
    total = 0
    i = 1
    while i <= k:
        total += count_k(n - i, k)
        i += 1
    return total


def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [i * s[i] for i in range(len(s)) if i % 2 == 0]


def max_product(s):
    """Return the maximum product that can be formed using non-consecutive
    elements of s.

    >>> max_product([10, 3, 1, 9, 2]) # 10 * 9
    90
    >>> max_product([5, 10, 5, 10, 5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    max_result = 1
    l = len(s)
    for i in range(l):
        for j in range(2, l - 1):
            temp_product = 1
            for x in [x for x in s[i::j]]:
                temp_product *= x
            max_result = max(max_result, temp_product)
    return max_result
