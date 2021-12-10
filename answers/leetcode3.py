def length_of_longest_substring(s: str) -> int:
    """ Given a string s, find the length of the longest substring
    without repeating characters
    
    Params
        s(str): A string to find a substring from
    Return
        int: The length of the substring
    
    === Constraints ===
    - 0 <= len(s) <= 5 * pow(10, 4)
    - s consists of English letters, digits, symbols and spaces.
       
    >>> length_of_longest_substring('abcabcbb')
    3
    >>> length_of_longest_substring('bbbbb')
    1
    >>> length_of_longest_substring('pwwkew')
    3
    >>> length_of_longest_substring('')
    0
    """
    return