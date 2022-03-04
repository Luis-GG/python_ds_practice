def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """

    seperated_phrase = phrase.split(" ")

    seperated_phrase[0] = seperated_phrase[0].capitalize()

    return " ".join(seperated_phrase)
