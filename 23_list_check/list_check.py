def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    counter = 0
    for item in lst:
        if isinstance(item, list) == True:
            counter += 1
    return counter == len(lst)
