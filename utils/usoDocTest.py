def sum_list(lst):
    """
    Suma todos los elementos de una lista.

    >>> sum_list([1, 2, 3, 4])
    10
    >>> sum_list([5, 5, 5])
    15
    >>> sum_list([-1, 1])
    0
    """
    return print(sum(lst))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)