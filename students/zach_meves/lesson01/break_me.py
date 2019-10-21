"""
break_me.py
Zachary Meves
Python 210
Lesson 01
"""


def raise_name_error():
    """Function that will cause a :py:class:`NameError` to be raised."""
    a = b  # b is not defined, will raise NameError
    return a


def raise_type_error():
    """Function that will cause a :py:class:`TypeError` to be raised."""
    result = 1 + None  # Can't add an ``int`` and ``None`` -> TypeError
    return result


def raise_syntax_error():
    """Function that will cause a :py:class:`SyntaxError` to be raised."""
    eval('a = [1, 2, 3, "4]')  # Missing closing " in the last entry
    return a


def raise_attr_error():
    """Function that will cause a :py:class:`AttributeError` to be raised."""
    a = [1, 2, 3]
    return a.keys()  # A list has no attribute keys


if __name__ == '__main__':
    """Run script to test function."""
    funs_results = [(raise_name_error, NameError, 'NameError'),
                    (raise_type_error, TypeError, 'TypeError'),
                    (raise_syntax_error, SyntaxError, 'SyntaxError'),
                    (raise_attr_error, AttributeError, 'AttributeError')]

    for entry in funs_results:
        fun = entry[0]
        err = entry[1]
        try:
            fun()
            assert False  # None of these should run
        except err:
            print("{} raised a {}".format(fun.__name__, entry[2]))
