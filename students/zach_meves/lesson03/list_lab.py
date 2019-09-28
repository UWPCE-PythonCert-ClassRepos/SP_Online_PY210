#!/usr/bin/env python3
"""
list_lab.py

Zach Meves
Python 210
Lesson 03

Exercise : List Lab
"""


def _create_basic_list():
    """For internal use only.

    Returns the starting list with Apples, Pears, Oranges, and Peaches."""

    return ['Apples', 'Pears', 'Oranges', 'Peaches']


def _get_user_input(prompt):
    """For internal use only.

    Get valid user input with the provided prompt.

    Returns string of user input."""

    _inp = ''
    while not _inp:
        _inp = input(prompt)

    return _inp


def series_1():
    """Performs the actions for series 1.

    Returns
    -------
    list
        Result of series 1 actions"""

    lst = _create_basic_list()
    print(lst)

    # Ask user for a new fruit, put it at end of list
    _fruit = _get_user_input("Enter a fruit to add to the list:\n> ")
    lst.append(_fruit)

    # Display the list
    print(lst)

    # Ask user for a number, display that fruit (1-based indexing)
    _num = 0
    while True:
        _num = int(_get_user_input("Enter a number:\n> "))
        if 1 <= _num <= len(lst):
            break
        else:
            print(f"Number must be between 1 and {len(lst)}")
    print(f'{_num} - {lst[_num - 1]}')

    # Add a fruit to beginning of list using '+'
    print('Adding "Banana" to front of list with the + operator')
    lst = ['Banana'] + lst
    print(lst)

    # Add a fruit to beginning of list using ``insert``
    print('Adding "Grape" to front of list using the "insert" method')
    lst.insert(0, 'Grape')
    print(lst)

    # Display all fruits that begin with 'P'
    _p_list = []
    for fruit in lst:
        if fruit.startswith('P'):
            _p_list.append(fruit)
    print(f"Fruits beginning with 'P': {', '.join(_p_list)}")

    return lst


def series_2(fruits):
    """Performs actions from series 2 with a given list of fruits.

    Parameters
    ----------
    fruits : list
        List of fruits, output of Series 1"""

    # Display list
    print(fruits)

    # Remove last fruit
    fruits.pop()
    print('Removed last fruit')
    print(fruits)

    # Ask user for a fruit to delete
    _fruit = '____'
    while True:
        _fruit = _get_user_input("Enter a fruit to delete:\n> ")
        if _fruit in fruits:
            break
        else:
            print(f'{_fruit} is not in the list')
    _num_frt = fruits.count(_fruit)
    for _ in range(_num_frt):
        fruits.remove(_fruit)


def series_3(fruits):
    """Perform actions for series 3.

    Parameters
    ----------
    fruits : list
        List of fruits, output of Series 1
    """

    # Get lowercase names, and get list of unique fruit names and count
    lower_fruits = [x.lower() for x in fruits]
    fruit_count = dict()
    for f in lower_fruits:
        if f in fruit_count:
            fruit_count[f] += 1
        else:
            fruit_count[f] = 1

    _to_delete = []
    # Iterate over unique fruits, asking if should delete
    for fruit, count in fruit_count.items():
        while True:
            _resp = _get_user_input(f"Do you like {fruit}?\n> ")
            _r_lower = _resp.lower()
            if _r_lower in ('yes', 'no'):
                if _r_lower == 'no':
                    # Delete fruit from list - find all occurrences
                    _i_ = -1
                    for _ in range(count):
                        _i_ = lower_fruits.index(fruit, _i_ + 1)
                        _to_delete.append(_i_)
                break
            else:
                print('Please respond with "yes" or "no"')

    # Do the deletion
    _to_delete.sort()
    _to_delete.reverse()
    for i in _to_delete:
        fruits.pop(i)

    print('Final fruit list:')
    print(fruits)


def series_4(fruits):
    """Perform actions for series 4.

    Parameters
    ----------
    fruits : list
        List of fruits to operate on, output of Series 1"""

    # New list, with each item's letters reversed
    new_fruits = [x[::-1]for x in fruits]

    # Delete last item of original list
    fruits.pop()

    print(f'Original list: {fruits}')
    print(f'New list: {new_fruits}')


if __name__ == "__main__":
    """Perform the 4 steps for the lab."""

    # Series 1
    print('Series 1:')
    result_1 = series_1()

    # Series 2
    print('\nSeries 2:')
    series_2(result_1[:])

    # Series 3
    print('\nSeries 3:')
    series_3(result_1[:])

    # Series 4
    print('\nSeries 4:')
    series_4(result_1[:])