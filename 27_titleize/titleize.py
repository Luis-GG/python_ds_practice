def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    words = phrase.split(" ")
    new_str = []

    for word in words:
        new_str.append(word.capitalize())

    return " ".join(new_str)
