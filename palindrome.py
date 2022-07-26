def is_palindrom(word):
    """
        Function detects whether a given word is palindrome,
        which means that reading it from beginning
        and from end returns the same value
        Arguments:
        word
    """
    return word[::-1] == word