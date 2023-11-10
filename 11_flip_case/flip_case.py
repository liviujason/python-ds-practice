def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    new_phrase = [char for char in phrase]

    for i, x in enumerate(new_phrase):
        if x == to_swap.lower():
            new_phrase[i] = new_phrase[i].capitalize()
        elif x == to_swap.capitalize():
            new_phrase[i] = new_phrase[i].lower()
    return ''.join(new_phrase)
