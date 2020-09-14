#!/usr/bin/env python3
from mailroom_pt4 import db, thank_you_tmp
from mailroom_pt4 import add_donor, add_donation
from mailroom_pt4 import msg_vars, get_letter_text
from mailroom_pt4 import list_of_donors, get_report
from mailroom_pt4 import send_letters_to_all_donors

import os


def test_add_donor1():
    """Test addition of new donor to database.  Message text."""
    assert add_donor('kyle test') == ('Kyle Test',
                                      '\nAdding donor to database : Kyle Test')


def test_add_donor2():
    """Test check for existing donor name in database.  Message text."""
    assert add_donor('callum fuller') == ('Callum Fuller', '\nFound donor '
                                          'Callum Fuller in database.')


def test_add_donor3():
    """Test if new donor is in database."""
    add_donor('kyle test')
    assert 'Kyle Test' in db.keys()


def test_add_donation1():
    """Test if new donation added to database."""
    name = 'Kyle Test'
    add_donation(name, 199.)
    assert db[name][-1] == 199.


def test_add_donation2():
    """Test if new donation is added to database."""
    name = 'Kyle Test'
    add_donation(name, 101.)
    assert db[name][-1] == 101.


def test_add_donation3():
    """Test exception if zero or negative donation amount given."""
    name = 'Kyle Test'
    expected = ('\nZero or negative donation amount provided. '
                'Returning to menu...')
    assert add_donation(name, 0) == expected
    assert add_donation(name, -1) == expected


def test_msg_vars():
    """Test that the correct message variables are returned."""
    name = 'Kyle Test'
    assert msg_vars(name) == {'name': 'Kyle Test',
                              'donation_amt': 101.,
                              'donation_num': 2,
                              'donation_sum': 300.}


def test_get_letter_txt():
    """Test Thank You letter text."""
    name = 'Kyle Test'
    expected = ("\n Subject: Thank You !!!\n"
                "\n Dear Kyle Test,\n"
                "\n Thank you for your latest donation of $101.00.\n"
                " We are so glad you have made 2 donation(s)"
                " totaling $300.00.\n"
                " Your continued support will help our"
                " foundation achive our goals.\n\n"
                " Regards,\n       Foundation Leadership Team\n"
                )
    assert get_letter_text(name) == expected


def test_list_donors():
    """Test creation of alphabetical list of donor names."""
    assert list_of_donors() == ['Callum Fuller', 'David Anderson',
                                'Edward Harvik', 'Katherine Elmhurst',
                                'Kyle Test', 'Rebecca Manriquez']


def test_get_report():
    """Test report text generation."""
    assert get_report() == [
     ' David Anderson            $   16615.00           2  $     8307.50',
     ' Katherine Elmhurst        $    4400.00           3  $     1466.67',
     ' Rebecca Manriquez         $    3250.00           2  $     1625.00',
     ' Edward Harvik             $     600.00           3  $      200.00',
     ' Kyle Test                 $     300.00           2  $      150.00',
     ' Callum Fuller             $     101.00           1  $      101.00']


def test_send_letters_to_all_donors():
    """Test if all donor letter files were created."""
    send_letters_to_all_donors()
    for file in db.keys():
        assert os.path.isfile(file.replace(' ', '_') + '.txt') is True


def test_letter_text():
    """Test individual letter text."""
    expected = ("\n Subject: Thank You !!!\n"
                "\n Dear David Anderson,\n"
                "\n Thank you for your latest donation of $5,750.00.\n"
                " We are so glad you have made 2 donation(s)"
                " totaling $16,615.00.\n"
                " Your continued support will help our"
                " foundation achive our goals.\n\n"
                " Regards,\n       Foundation Leadership Team\n"
                )
    with open('David_Anderson.txt', 'r') as letter_text:
        assert letter_text.read() == expected
