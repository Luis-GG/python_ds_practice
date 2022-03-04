def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    tracker = {}

    for x in phrase:
        if tracker.get(x) == None:
            tracker[x] = 1
        else: 
            tracker[x] += 1
    
    return tracker