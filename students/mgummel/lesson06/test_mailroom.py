#!/usr/bin/env python3

from mailroom import *

test_db1  = {
    "William Gates, III": [653772.32, 12.17],
    "Jeff Bezos": [877.33],
    "Dax Shephard": [123.32],
    "Paul Allen": [663.23, 43.87, 1.32],
    "Eric Johnson": [23432.23, 43289.32],
    "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
    "Marc Benioff": [45023.15, 442.30]
}

test_db2 = {
    "Eddie Vedder": [43.12, 432.70, 723.40],
    "Gerard Way": [76.45]
}


def test_sum():
    assert sum([2343.23, 4324.12, 567.17]) == 7234.52


def test_avg():
    assert avg([23.57, 43.42, 45.38]) == 37.46


"""def add_donor(new_donor, db_dict=donor_db):
    db_dict.setdefault(new_donor, list())"""


def test_generate_list1():
    name_list = '\n'.join(["William Gates, III",
                           "Jeff Bezos",
                           "Dax Shephard",
                           "Paul Allen",
                           "Eric Johnson",
                           "Mark Zuckerberg",
                           "Marc Benioff"])
    assert generate_list(test_db1) == name_list


def test_generate_list2():
    name_list = '\n'.join(["Eddie Vedder",
                           "Gerard Way"])
    assert generate_list(test_db2) == name_list


def test_compute_sorted1():
    sorted_item = list()
    sorted_item.append(("Eddie Vedder", 1199.22, 3, 399.74))
    sorted_item.append(("Gerard Way", 76.45, 1, 76.45))
    assert compute_sorted(test_db2) == sorted_item


def test_get_donor1():
    db_tuple = ("Gerard Way", [76.45])
    assert get_donor("Gerard Way", test_db2) == db_tuple


def test_get_donor2():
    db_tuple = ("Eric Johnson", [23432.23, 43289.32])
    assert get_donor("Eric Johnson", test_db1) == db_tuple


def test_build_template1():
    email_template = '\n'.join(('\n\nDear Dax Shephard,\n',
                                'Thank you for your very kind donation of $123.32.\n',
                                'It will be put to very good use.\n',
                                '           Sincerely,',
                                '             -The Team\n'))
    assert build_template(("Dax Shephard", test_db1["Dax Shephard"])) == email_template


def test_build_template2():
    email_template = '\n'.join(('\n\nDear Marc Benioff,\n',
                                'Your past donation amount of $45023.15\n',
                                'has helped our organization tremendously.\n',
                                'Thank you for your very kind donation of $442.30.\n',
                                'It will be put to very good use.\n',
                                '           Sincerely,',
                                '             -The Team\n'))
    assert build_template(("Marc Benioff", test_db1["Marc Benioff"])) == email_template


def test_build_template3():
    email_template = '\n'.join(('\n\nDear Gerard Way,\n',
                                'Thank you for your very kind donation of $76.45.\n',
                                'It will be put to very good use.\n',
                                '           Sincerely,',
                                '             -The Team\n'))
    assert build_template(("Gerard Way", test_db2["Gerard Way"])) == email_template


def test_build_template4():
    email_template = '\n'.join(('\n\nDear Eddie Vedder,\n',
                                'Your past donation amount of $475.82\n',
                                'has helped our organization tremendously.\n',
                                'Thank you for your very kind donation of $723.40.\n',
                                'It will be put to very good use.\n',
                                '           Sincerely,',
                                '             -The Team\n'))
    assert build_template(("Eddie Vedder", test_db2["Eddie Vedder"])) == email_template