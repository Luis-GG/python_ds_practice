def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """
    keys_list = list(d.keys())

    min_key = keys_list[0]
    max_key = keys_list[0]

    for num in keys_list:
        if num < min_key:
            min_key = num
        if num > max_key:
            max_key = num

    return (min_key, max_key)
