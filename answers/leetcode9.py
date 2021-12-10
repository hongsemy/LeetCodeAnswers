def is_palindrome(x: int) -> bool:
    """ Given an integer x, return True if x is palindrome integer.
    
    An integer is a palindrome whe it reads the same backward as forward
    - For example, 121 is a palindrome while 123 is not.

    === Constraints ===
    - -2^31 <= x <= 2^31 -1
    
    Params
        int(x): An integer to check whether it is palindrome or not
    Return
        bool: A result
        
    >>> is_palindrome(121)
    True
    >>> is_palindrome(-121)
    False
    >>> is_palindrome(10)
    False
    >>> is_palindrome(-101)
    False
    """
    for i in range(len(str(x))//2):
        if str(x)[i] != str(x)[-i-1]:
            return False
    
    return True


def is_palindrome_no_conversion(x: int) -> bool:
    """ Given an integer x, return True if x is palindrome integer.
    
    An integer is a palindrome whe it reads the same backward as forward
    - For example, 121 is a palindrome while 123 is not.

    === Constraints ===
    - -2^31 <= x <= 2^31 -1
    
    Params
        int(x): An integer to check whether it is palindrome or not
    Return
        bool: A result
        
    >>> is_palindrome_no_conversion(121)
    True
    >>> is_palindrome_no_conversion(-121)
    False
    >>> is_palindrome_no_conversion(10)
    False
    >>> is_palindrome_no_conversion(-101)
    False
    """
    first_half = x
    last_half = 0
    