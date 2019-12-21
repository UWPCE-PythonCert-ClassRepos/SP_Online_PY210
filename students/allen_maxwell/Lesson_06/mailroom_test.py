#!/usr/bin/env python3

# Allen Maxwell
# Python 210
# 12/17/2019
# mailroom_test.py

import unittest
import os
import mailroom


test_donors = {
    'Tom Sawyer': [120000.5, 2, 326892.24],
    'Luke Skywalker': [1.1, 3, 5465.37],
    'Johnny Quest': [1800.63, 1, 877.33],
    'John Wick': [7008.02, 3, 236.14],
    'James Bond': [100000.00, 1, 10000.00]}


def test_list(test_donors):
    donor_list = '\n'.join([donor for donor in sorted(test_donors)])
    return donor_list


def test_letter_string(name, amount):
    '''Test letter string'''

    test_letter = '''\n
        Dear {},\n
        Thank you so much for your generous gift of ${:,.2f}!\n
        Your donation will go far in helping so many orphaned kittens
        and puppies find a new home.\n
        Thank You,\n
        Paws'''.format(name, amount)
    return test_letter


class test_mailroom(unittest.TestCase):

    def test_check_menu_response(self):
        ''' Tests menu negative responses'''

        # Test invalid entries
        error_message = '\nPlease enter a number 1 - 4'
        assert mailroom.check_menu_response('0') == error_message
        assert mailroom.check_menu_response('5') == error_message
        assert mailroom.check_menu_response('allen') == error_message
        assert mailroom.check_menu_response('') == error_message
        assert mailroom.check_menu_response(None) == error_message

    def test_get_report(self):
        ''' Test get_report(dict)'''

        test_report = [
            'Donor Name         |  Total Given |  Num Gifts |  Average Gift',
            '--------------------------------------------------------------',
            'Tom Sawyer           $ 120,000.50       2        $ 326,892.24',
            'James Bond           $ 101,000.01       2        $  50,500.00',
            'John Wick            $   7,008.02       3        $     236.14',
            'Johnny Quest         $   1,800.63       1        $     877.33',
            'Luke Skywalker       $       1.10       3        $   5,465.37']

        report_result = mailroom.get_report(test_donors)
        for i in range(len(test_report)):
            assert report_result[i] == test_report[i]

    def test_check_donor_name(self):
        '''Test check_donor_name(str, dict)'''

        # Test existing donor entries
        for name in test_donors:
            assert mailroom.check_donor_name(name, test_donors) == name
            assert mailroom.check_donor_name(name.lower(), test_donors) == name
            assert mailroom.check_donor_name(name.upper(), test_donors) == name

        # Test new donor entries
        assert mailroom.check_donor_name('Paul Eliot', test_donors) == 'Paul Eliot'
        assert mailroom.check_donor_name('john cash', test_donors) == 'John Cash'
        assert mailroom.check_donor_name('JOHN JONES', test_donors) == 'John Jones'
        assert test_donors.get('Paul Eliot') == [0, 0, 0]
        assert test_donors.get('John Cash') == [0, 0, 0]
        assert test_donors.get('John Jones') == [0, 0, 0]
        assert mailroom.check_donor_name('LIST', test_donors) == test_list(test_donors)
        assert mailroom.check_donor_name('list', test_donors) == test_list(test_donors)

        # Test invalid entries
        error_message = 'Please enter a full name'
        assert mailroom.check_donor_name('paul', test_donors) == error_message
        assert mailroom.check_donor_name('100', test_donors) == error_message
        assert mailroom.check_donor_name('', test_donors) == error_message
        assert mailroom.check_donor_name(' ', test_donors) == error_message

    def test_check_donation_amount(self):
        ''' Test check_donation_amount(str)'''

        # Test valid entries
        assert mailroom.check_donation_amount('0') == 0.0
        assert mailroom.check_donation_amount('10') == 10.0
        assert mailroom.check_donation_amount('2.321') == 2.321
        assert mailroom.check_donation_amount('.000001') == 0.000001

        # Test invalid entries
        error_message = 'Please enter a numeric value'
        assert mailroom.check_donation_amount('abc') == error_message
        assert mailroom.check_donation_amount('cd100.3') == error_message
        assert mailroom.check_donation_amount('') == error_message
        assert mailroom.check_donation_amount(' ') == error_message
        assert mailroom.check_donation_amount('.') == error_message

    def test_add_donation(self):
        ''' Test add_donation(str, dict)'''

        # Test valid entry
        assert mailroom.add_donation('James Bond', 1000.01, test_donors) == test_letter_string('James Bond', 1000.01)
        assert test_donors.get('James Bond') == [101000.01, 2, 50500.005]

    def test_get_letter_text(self):
        ''' Tests get_letter_text(string, float)'''

        # Test valid entries
        assert mailroom.get_letter_text('John Paul', 100.01) == test_letter_string('John Paul', 100.01)
        assert mailroom.get_letter_text('John Wick', 10000.00) == test_letter_string('John Wick', 10000.00)
        assert mailroom.get_letter_text('Tom Sawyer', 250000.00) == test_letter_string('Tom Sawyer', 250000.00)

    def test_send_letters(self):
        ''' Tests send_letters'''

        # Test valid entries
        mailroom.save_thank_all(test_donors)
        for donor in test_donors:
            first_name = donor.split()[0]
            last_name = donor.split()[1].strip(',')
            name = first_name + ' ' + last_name
            file_name = os.path.join("./{}_{}.txt".format(first_name, last_name))
            assert os.path.exists(file_name)
            with open(file_name, 'r') as file_text:
                assert file_text.read() == test_letter_string(name, test_donors.get(donor)[0])


if __name__ == "__main__":

    unittest.main()
