#!/usr/bin/env python3
"""
Purpose: Mailroom Part 4 testing mail room functionality python certificate from UW
Author: Pirouz Naghavi
Date: 07/14/2020
"""

import pytest
import os


@pytest.fixture
def mailroom_gen_db_seven_donors():
    import mailroom
    mailroom.donor_db = {
        'William Gates, III': [653772.32, 12.17],
        'Jeff Bezos': [877.33],
        'Paul Allen': [663.234, 43.87, 1.32],
        'Mark Zuckerberg': [1663.23, 4300.87, 10432.0],
        'Jayz': [999.9, 100.0, 100.0],
        'Beyonce': [1000.0, 100.0],
        'Melinda Gates': [10000000.0, 1000000.0, 1000020.0],
    }
    return mailroom


def test_adding_donor_1(mailroom_gen_db_seven_donors):
    assert 'John Smith' not in mailroom_gen_db_seven_donors.donor_db
    mailroom_gen_db_seven_donors.update_donors('John Smith')
    assert 'John Smith' in mailroom_gen_db_seven_donors.donor_db


def test_adding_donor_2(mailroom_gen_db_seven_donors):
    assert '' not in mailroom_gen_db_seven_donors.donor_db
    mailroom_gen_db_seven_donors.update_donors('')
    assert '' in mailroom_gen_db_seven_donors.donor_db


def test_adding_donor_3(mailroom_gen_db_seven_donors):
    assert 'Melinda Gates' in mailroom_gen_db_seven_donors.donor_db
    mailroom_gen_db_seven_donors.update_donors('Melinda Gates')
    assert 'Melinda Gates' in mailroom_gen_db_seven_donors.donor_db


def test_adding_donor_raises_typeerror_1(mailroom_gen_db_seven_donors):
    with pytest.raises(TypeError):
        mailroom_gen_db_seven_donors.update_donors(100)


def test_adding_donor_raises_typeerror_2(mailroom_gen_db_seven_donors):
    with pytest.raises(TypeError):
        mailroom_gen_db_seven_donors.update_donors()


def test_adding_donation_1(mailroom_gen_db_seven_donors):
    assert 99.99 not in mailroom_gen_db_seven_donors.donor_db['Beyonce']
    mailroom_gen_db_seven_donors.add_donation('Beyonce', 99.99)
    assert 99.99 in mailroom_gen_db_seven_donors.donor_db['Beyonce']


def test_adding_donation_2(mailroom_gen_db_seven_donors):
    assert 1 == mailroom_gen_db_seven_donors.donor_db['Beyonce'].count(1000.0)
    mailroom_gen_db_seven_donors.add_donation('Beyonce', 1000.0)
    assert 2 == mailroom_gen_db_seven_donors.donor_db['Beyonce'].count(1000.0)


def test_adding_donation_3(mailroom_gen_db_seven_donors):
    old_sum = sum(mailroom_gen_db_seven_donors.donor_db['Paul Allen'])
    mailroom_gen_db_seven_donors.add_donation('Paul Allen', 1000.0)
    assert old_sum + 1000.0 == sum(mailroom_gen_db_seven_donors.donor_db['Paul Allen'])


def test_adding_donation_raises_typeerror_1(mailroom_gen_db_seven_donors):
    with pytest.raises(TypeError):
        mailroom_gen_db_seven_donors.add_donation()


def test_adding_donation_raises_typeerror_2(mailroom_gen_db_seven_donors):
    with pytest.raises(TypeError):
        mailroom_gen_db_seven_donors.add_donation(1000.0, 'Paul Allen')


def test_adding_donation_raises_keyerror_1(mailroom_gen_db_seven_donors):
    with pytest.raises(KeyError):
        mailroom_gen_db_seven_donors.add_donation('Paul AllenXO', 1000.0)


def test_adding_donation_raises_keyerror_2(mailroom_gen_db_seven_donors):
    with pytest.raises(KeyError):
        mailroom_gen_db_seven_donors.add_donation('', 1000.0)


def test_adding_donation_raises_keyerror_3(mailroom_gen_db_seven_donors):
    with pytest.raises(KeyError):
        mailroom_gen_db_seven_donors.add_donation('Paul Allen ', 1000.0)


def test_adding_donation_raises_valueerror_1(mailroom_gen_db_seven_donors):
    with pytest.raises(ValueError):
        mailroom_gen_db_seven_donors.add_donation('Paul Allen', -1000.0)


def test_adding_donation_raises_valueerror_2(mailroom_gen_db_seven_donors):
    with pytest.raises(ValueError):
        mailroom_gen_db_seven_donors.add_donation('Paul Allen', -0.0)


def test_adding_donation_raises_valueerror_3(mailroom_gen_db_seven_donors):
    with pytest.raises(ValueError):
        mailroom_gen_db_seven_donors.add_donation('Paul Allen', 0)


def test_adding_donation_raises_valueerror_3(mailroom_gen_db_seven_donors):
    with pytest.raises(ValueError):
        mailroom_gen_db_seven_donors.add_donation('Paul Allen', 0)


def test_write_thank_you_1(mailroom_gen_db_seven_donors):
    assert 'Paul Allen' in mailroom_gen_db_seven_donors.write_thank_you('Paul Allen')


def test_write_thank_you_2(mailroom_gen_db_seven_donors):
    assert str(mailroom_gen_db_seven_donors.donor_db['Paul Allen']
               [len(mailroom_gen_db_seven_donors.donor_db['Paul Allen']) - 1]) \
        in mailroom_gen_db_seven_donors.write_thank_you('Paul Allen')


def test_write_thank_you_3(mailroom_gen_db_seven_donors):
    assert format(float(sum(mailroom_gen_db_seven_donors.donor_db['Paul Allen'])), '0.2f') \
        in mailroom_gen_db_seven_donors.write_thank_you('Paul Allen')


def test_write_thank_you_4(mailroom_gen_db_seven_donors):
    assert str(len(mailroom_gen_db_seven_donors.donor_db['Paul Allen'])) \
        in mailroom_gen_db_seven_donors.write_thank_you('Paul Allen')


def test_write_thank_you_raises_typeerror(mailroom_gen_db_seven_donors):
    with pytest.raises(TypeError):
        mailroom_gen_db_seven_donors.write_thank_you()


def test_write_thank_you_raises_keyerror(mailroom_gen_db_seven_donors):
    with pytest.raises(KeyError):
        mailroom_gen_db_seven_donors.write_thank_you('Paul AllenXO')


def test_list_donors_1(mailroom_gen_db_seven_donors):
    assert 'Jeff Bezos                    \t' in mailroom_gen_db_seven_donors.get_donors_list_report()


def test_list_donors_2(mailroom_gen_db_seven_donors):
    assert 'Jeff BezosAI                  \t' not in mailroom_gen_db_seven_donors.get_donors_list_report()


def test_list_donors_3(mailroom_gen_db_seven_donors):
    assert 'Jeff Bezos                     \t' not in mailroom_gen_db_seven_donors.get_donors_list_report()


def test_list_donors_4(mailroom_gen_db_seven_donors):
    assert 'Paul Allen                    \t' in mailroom_gen_db_seven_donors.get_donors_list_report()


def test_list_donors_5(mailroom_gen_db_seven_donors):
    assert 'Paul Al                       \t' not in mailroom_gen_db_seven_donors.get_donors_list_report()


def test_sort_donors_1(mailroom_gen_db_seven_donors):
    sorted_list = mailroom_gen_db_seven_donors.sort_donors(list(mailroom_gen_db_seven_donors.donor_db.items()))
    true_sorted_list = list(mailroom_gen_db_seven_donors.donor_db.items())
    true_sorted_list.sort(key=lambda item: sum(item[1]), reverse=True)
    assert sorted_list == true_sorted_list


def test_sort_donors_2(mailroom_gen_db_seven_donors):
    sorted_list = mailroom_gen_db_seven_donors.sort_donors(list(mailroom_gen_db_seven_donors.donor_db.items()))
    binary_comparison_list = [sum(sorted_list[i][1]) >= sum(item[1]) for i, item in enumerate(sorted_list[1:])]
    assert False not in binary_comparison_list


def test_check_report_generation_1(mailroom_gen_db_seven_donors):
    assert 'Melinda Gates' in mailroom_gen_db_seven_donors.get_report()[3]


def test_check_report_generation_2(mailroom_gen_db_seven_donors):
    assert ' 3' in mailroom_gen_db_seven_donors.get_report()[3]


def test_check_report_generation_3(mailroom_gen_db_seven_donors):
    assert format(sum([10000000.0, 1000000.0, 1000020.0]), '.2f') in mailroom_gen_db_seven_donors.get_report()[3]


def test_check_report_generation_4(mailroom_gen_db_seven_donors):
    assert 'William Gates, III' in mailroom_gen_db_seven_donors.get_report()[4]


def test_check_report_generation_5(mailroom_gen_db_seven_donors):
    assert ' 2' in mailroom_gen_db_seven_donors.get_report()[4]


def test_check_report_generation_6(mailroom_gen_db_seven_donors):
    assert format(sum([653772.32, 12.17]), '.2f') in mailroom_gen_db_seven_donors.get_report()[4]


def test_check_report_generation_7(mailroom_gen_db_seven_donors):
    # print(mailroom_gen_db_seven_donors.get_report()[-1])
    assert 'Paul Allen' in mailroom_gen_db_seven_donors.get_report()[-2]


def test_check_report_generation_8(mailroom_gen_db_seven_donors):
    assert ' 3' in mailroom_gen_db_seven_donors.get_report()[-2]


def test_check_report_generation_9(mailroom_gen_db_seven_donors):
    assert format(sum([663.234, 43.87, 1.32]), '.2f') in mailroom_gen_db_seven_donors.get_report()[-2]


def test_thank_you_file_generation_1(mailroom_gen_db_seven_donors):
    dirpath, dirnames, filenames = next(os.walk('letters/'))
    file_count_before = len(filenames)
    mailroom_gen_db_seven_donors.send_thank_you_to_all()
    dirpath_aft, dirnames_aft, filenames_aft = next(os.walk('letters/'))
    file_count_aft = len(filenames_aft)
    assert file_count_before + len(mailroom_gen_db_seven_donors.donor_db) == file_count_aft


def test_write_thank_you_5(mailroom_gen_db_seven_donors):
    assert 'Paul Allen' in mailroom_gen_db_seven_donors.write_thank_you('Paul Allen')


def test_write_thank_you_6(mailroom_gen_db_seven_donors):
    assert 'Melinda Gates' in mailroom_gen_db_seven_donors.write_thank_you('Melinda Gates')


def test_write_thank_you_7(mailroom_gen_db_seven_donors):
    assert 'William Gates, III' in mailroom_gen_db_seven_donors.write_thank_you('William Gates, III')


def test_write_thank_you_8(mailroom_gen_db_seven_donors):
    assert 'Beyonce' in mailroom_gen_db_seven_donors.write_thank_you('Beyonce')


def test_write_thank_you_9(mailroom_gen_db_seven_donors):
    assert str(mailroom_gen_db_seven_donors.donor_db['Beyonce']
               [len(mailroom_gen_db_seven_donors.donor_db['Beyonce']) - 1]) \
           in mailroom_gen_db_seven_donors.write_thank_you('Beyonce')