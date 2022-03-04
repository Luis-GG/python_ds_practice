from operator import indexOf


def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    new_string = ""

    for char in phrase:

        if char.lower() == to_swap.lower():
            if char.isupper():
                new_string += char.lower()

            else:
                new_string += char.upper()

        else:
            new_string += (char)

    return new_string
