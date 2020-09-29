#!/usr/bin/env python3

from mailroom import *
import os

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


def test_add_donation1():
    transaction = add_donation("Eric Johnson", 32.45, test_db1)
    assert transaction == ("Eric Johnson", [23432.23, 43289.32, 32.45])


def test_add_donation2():
    transaction = add_donation("Rob Thomas", 23.23, test_db2)
    assert transaction == ("Rob Thomas", [23.23])


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


def test_file_creation1():
   cwd_path = os.path.abspath(".")
   write_files(cwd_path, db=test_db2)
   assert os.path.exists(f'{cwd_path}/Gerard_Way.txt')
   assert os.path.exists(f'{cwd_path}/Eddie_Vedder.txt')

def test_file_creation2():
   cwd_path = os.path.abspath(".")
   write_files(cwd_path, db=test_db1)
   assert os.path.exists(f'{cwd_path}/Paul_Allen.txt')
   assert os.path.exists(f'{cwd_path}/Eric_Johnson.txt')


def test_file_content1():
    with open('./Paul_Allen.txt', 'r', encoding='utf-8') as donor_email_file:
        email_file = donor_email_file.read()
    email_template = '\n'.join(('\n\nDear Paul Allen,\n',
                                'Your past donation amount of $707.10\n',
                                'has helped our organization tremendously.\n',
                                'Thank you for your very kind donation of $1.32.\n',
                                'It will be put to very good use.\n',
                                '           Sincerely,',
                                '             -The Team\n'))
    assert email_file == email_template


def test_file_content2():
    with open('./Jeff_Bezos.txt', 'r', encoding='utf-8') as donor_email_file:
        email_file = donor_email_file.read()
    email_template = '\n'.join(('\n\nDear Jeff Bezos,\n',
                                'Thank you for your very kind donation of $877.33.\n',
                                'It will be put to very good use.\n',
                                '           Sincerely,',
                                '             -The Team\n'))
    assert email_file == email_template


def test_file_content1():
    with open('./William_Gates_III.txt', 'r', encoding='utf-8') as donor_email_file:
        email_file = donor_email_file.read()
    email_template = '\n'.join(('\n\nDear William Gates, III,\n',
                                'Your past donation amount of $653772.32\n',
                                'has helped our organization tremendously.\n',
                                'Thank you for your very kind donation of $12.17.\n',
                                'It will be put to very good use.\n',
                                '           Sincerely,',
                                '             -The Team\n'))
    assert email_file == email_template


def test_file_content3():
    with open('./Gerard_Way.txt', 'r', encoding='utf-8') as donor_email_file:
        email_file = donor_email_file.read()
    email_template = '\n'.join(('\n\nDear Gerard Way,\n',
                                'Thank you for your very kind donation of $76.45.\n',
                                'It will be put to very good use.\n',
                                '           Sincerely,',
                                '             -The Team\n'))
    assert email_file == email_template