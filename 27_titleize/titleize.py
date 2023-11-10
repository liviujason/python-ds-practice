def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

    list = phrase.split(' ')

    for i, item in enumerate(list):
        list[i] = str(list[i]).capitalize()

    return ' '.join(list)
