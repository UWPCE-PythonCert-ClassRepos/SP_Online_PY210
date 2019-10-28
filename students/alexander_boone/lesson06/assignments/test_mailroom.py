#!/usr/bin/env python

import mailroom as mail
import os

# ----- TEST FUNCTIONS -----


def get_updated_donors_list():
    '''Generate updated donors variables for testing purposes.'''
    return mail.donors.keys()


def get_text(filepath):
    '''Get text from the specified written letter for testing.'''

    with open(filepath, "r") as readfile:
        contents = readfile.read()
        return contents

# ----- TEST CODE -----


def test_add_donor():
    """Test the add_donor function."""

    mail.add_donor('Alexander Boone')
    donors_list = get_updated_donors_list()
    assert any(donor == 'Alexander Boone' for donor in donors_list)


def test_update_donor():
    """Test the update_donor function."""

    name = 'Alexander Boone'
    donation = 1000
    assert mail.update_donor(name, donation) == {'Alexander Boone': [1000, 1]}


def test_print_list():
    """Test the print_list function."""

    assert (mail.print_list() == ['Arnold Schwarzenegger', 'Lebron James',
                                  'Elon Musk', 'Walter White',
                                  'Gordon Ramsay', 'Alexander Boone'])


def test_create_report():
    """Test the create_report function for accurate rerport data creation."""

    report_data = mail.create_report()
    assert any(item == ('Arnold Schwarzenegger', 100000, 1, 100000/1)
               for item in report_data)
    assert any(item == ('Lebron James', 1000000, 1, 1000000/1)
               for item in report_data)
    assert any(item == ('Elon Musk', 2000000, 1, 2000000/1)
               for item in report_data)
    assert any(item == ('Walter White', 500000, 1, 500000/1)
               for item in report_data)
    assert any(item == ('Gordon Ramsay', 1280000, 1, 1280000/1)
               for item in report_data)
    assert any(item == ('Alexander Boone', 1000, 1, 1000/1)
               for item in report_data)


def test_letters_to_all_1():
    """Test the letters_to_all function to ensure all files are in the dir."""

    mail.letters_to_all()
    for root, dirs, files_list in os.walk('./letters'):
        assert any(file == 'Arnold_Schwarzenegger.txt' for file in files_list)
        assert any(file == 'Lebron_James.txt' for file in files_list)
        assert any(file == 'Elon_Musk.txt' for file in files_list)
        assert any(file == 'Walter_White.txt' for file in files_list)
        assert any(file == 'Gordon_Ramsay.txt' for file in files_list)
        assert any(file == 'Alexander_Boone.txt' for file in files_list)


def test_letters_to_all_2():
    """Test the letters_to_all function for correct letter body."""

    donors_list = get_updated_donors_list()
    mail.letters_to_all()
    script_dir = os.path.dirname(__file__)

    # verify body of letter for each donor - loop since f-strings used
    for donor in donors_list:
        first_name = donor.split(" ")[0]
        last_name = donor.split(" ")[1]
        relative_path = "{0}_{1}.txt".format(first_name, last_name)
        abs_file_path = os.path.join(script_dir, 'letters', relative_path)
        letter_body = ('{0},\n\nThank you'
                       + ' for donating ${1:,.2f}. You '
                       + 'are so kind.\n\nBest,\n\nLocal Charity'
                       ).format(donor, mail.donors[donor][0])
        assert letter_body == get_text(abs_file_path)
