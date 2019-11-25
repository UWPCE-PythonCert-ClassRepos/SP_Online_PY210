#!/usr/bin/env python

"""
Dictionary and Set Lab

The starting dict is a global value.

Dictionaries1() and Dictionaries2() use the starting dict.
"""

start_dict = dict(name='Chris', city='Seattle', cake='Chocolate')


def dictionaries1():  # pretty straightforward
    print(start_dict)
    start_dict.pop('cake')
    print(start_dict)
    start_dict['fruit'] = 'Mango'
    print(start_dict)
    print(start_dict.keys())
    print(start_dict.values())
    print('cake' in start_dict)
    print('Mango' in start_dict.values())


def dictionaries2():
    count_t = []  # establish an empty list for future population with count values
    for item in start_dict.values():
        count_t.append(item.lower().count('t'))  # number of 't' characters per string, case insensitive.
    dict2 = dict(name=count_t[0], city=count_t[1], cake=count_t[2])  # create new dict
    print(dict2)


def set1():
    """
    Set1

    This could have been done with 'if-elif-else' structure, but I used a dict switch to give \
    it a try.
    """
    # initialize empty sets
    s2 = set([])
    s3 = set([])
    s4 = set([])

    # define functions to update sets
    def s_2():
        s2.update([i])

    def s_3():
        s3.update([i])

    def s_4():
        s4.update([i])
    switch_set_dict = {2: s_2, 3: s_3, 4: s_4}
    for i in range(21):
        for val in [2, 3, 4]:
            # execute switch dict if divisible by 2, 3, or 4.
            if i % val == 0:
                switch_set_dict.get(val)()
    print(s2, '\n', s3, '\n', s4)
    print(s3.issubset(s2))
    print(s4.issubset(s2))


def set2():  # pretty straightforward
    P_set = set('Python')
    P_set.update('i')
    m_set = frozenset('marathon')
    print(P_set.union(m_set))
    print(P_set.intersection(m_set))