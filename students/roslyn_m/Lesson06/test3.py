from unittest.mock import patch
from unittest import TestCase

def sum():
    """Asks for the number of integers the user will type and
    the space separated integers."""
    n = input("Type the number of integers: ")
    L = input("Type the integers separated by space: ")
    L = L.split(' ')
    result = 0
    for num in range(n):
        result += int(L[num])
    return result