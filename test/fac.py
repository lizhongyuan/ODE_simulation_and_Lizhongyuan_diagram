"""
@brief: Brief description of the class.
@author: Your Name
@date: 2024/11/11
"""

def factorial(n):
    """
    Calculate the factorial of a number.

    :param n: A non - negative integer.
    :return: The factorial of the number n.

    Example:
    >>> factorial(5)
    120
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
