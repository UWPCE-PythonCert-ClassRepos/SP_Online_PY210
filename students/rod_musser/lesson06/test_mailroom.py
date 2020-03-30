#!/usr/bin/env python3
import mailroom
from os import path

def test_get_report():
    expected = [
        ['CJ McCollum', 24475, 5, 4895.0],
        ['Damien Lillard', 10199.5, 3, 3399.83],
        ['Hassan Whiteside', 10000, 1, 10000.0],
        ['Terry Stotts', 1300, 5, 260.0],
        ['Carmelo Anthony', 51, 2, 25.50]
    ]
    assert expected == mailroom.get_report()


def test_list_donors():
    expected = 'Carmelo Anthony\nDamien Lillard\nCJ McCollum\nHassan Whiteside\nTerry Stotts'
    assert expected == mailroom.list_donors()


def test_add_donation_existing_donor():
    existing_donor = 'Carmelo Anthony'
    expected_donations = [1, 50, 100]
    mailroom.add_donation(existing_donor, 100)
    assert expected_donations == mailroom.donors[existing_donor]


def test_add_donation_new_donor():
    new_donor = 'Mike Rice'
    expected_donations = [3.50]
    mailroom.add_donation(new_donor, 3.50)
    assert expected_donations == mailroom.donors[new_donor]


def test_get_letter_text():
    expected = "Dear Damien Lillard,\n\n\
Thank you for your generous support of Rod's Early \
Retirement Fund.\n\nYour 3 donation(s) \
totaling $10199.50 makes Rod's early retirement \
dreams a reality.  Your generous support will enable Rod \
to perform critical early retirement tasks like \n\n\t- \
Mai Tais on the beach \n\t- First class airline travel \
\n\t- Alpine skiing.  \n\nAgain, thank you Damien \
for your generous support. \n\nSincerely, \n\nRod Musser \
\nChairperson\nRod's Early Retirement Fund"

    letter_data = {}
    letter_data['first_name'] = 'Damien'
    letter_data['last_name'] = 'Lillard'
    letter_data['total_donation'] = 10199.5
    letter_data['num_donations'] = 3
    assert expected == mailroom.get_letter_text(letter_data)


def test_write_letter():
    letter_data = {}
    letter_data['first_name'] = 'Damien'
    letter_data['last_name'] = 'Lillard'
    letter_data['total_donation'] = 10199.5
    letter_data['num_donations'] = 3
    mailroom.write_letters('./', [letter_data])
    assert path.isfile('./Damien_Lillard.txt')
