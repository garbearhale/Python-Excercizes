def truncate(phrase, n):
    """Return truncated-at-n-chars version of  phrase.
    
    If the phrase is longer than, or the same size as, n make sure it ends with '...' and is no
    longer than n.
    
        >>> truncate("Hello World", 6)
        'Hel...'
        
        >>> truncate("Problem solving is the best!", 10)
        'Problem...'
        
        >>> truncate("Yo", 100)
        'Yo'
        
    The smallest legal value of n is 3; if less, return a message:
    
        >>> truncate('Cool', 1)
        'Truncation must be at least 3 characters.'

        >>> truncate("Woah", 4)
        'W...'

        >>> truncate("Woah", 3)
        '...'
    """
    
    # return sum([num for num in nums if isinstance(num, float)])
    newWord = ""
    count = 0
    newCount = 0
    for letter in phrase:
        count += 1
    if (n <= count) & (n >= 3):
        dots = n - 3
        for ltr in phrase:
            if newCount < dots:
                newWord += ltr
            if (newCount >= dots) & (newCount < n):
                newWord += "."
            else:
                newWord += ""
            newCount += 1
        return newWord
    else:
        print("Sorry the number must be at least 3")
                
    
            
