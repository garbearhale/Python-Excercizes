def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """
    if a>b:
        return "The first number is greater"
    elif b>a:
        return "The second number is greater"
    elif a==b:
        return "The numbers are equal"
    else:
        return "Not a number"