def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    
    newLetter = ""
    
    for letter in phrase:
        if letter == phrase[:1]:   
            newLetter += letter.upper()
        else:
            newLetter += letter.lower()
    return newLetter
