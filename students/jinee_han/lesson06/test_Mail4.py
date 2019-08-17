'''
Unit tests for Mailroom 4
Dev: Jinee Han
Date: 2019-08-14
'''

from Mail4 import *


def test_donor_not_present_should_return_false():
    '''
    Tests that a name not present in the donor_db object returns false
    :return: No return value
    '''
    assert donor_present("Jinee") == False


def test_donor_not_present_then_add_donor_and_should_be_present():
    '''
    Tests that initially the new donor is not present, then donor is added and present
    :return: No return value
    '''
    donor_name = "Jinee"
    assert donor_present(donor_name) == False
    add_donor(donor_name)
    assert donor_present(donor_name) == True


def test_donor_present_should_return_true():
    '''
    Tests that a name present in the donor_db object returns true
    :return: No return value
    '''
    assert donor_present("Will Smith") == True


def test_add_donation_amount_succeeds():
    '''
    Tests that added a new donation amount is appended to the donation list
    :return: No return value
    '''
    expected_donator = "Will Smith"
    expected_donation_amount = 100.00
    add_donation_amount(expected_donator, expected_donation_amount)
    donation_amounts = donor_db[expected_donator]
    assert expected_donation_amount == donation_amounts[-1]


def expected_thank_you_note_format(donator, donation_amount):
    '''
    Note: this isn't ideal because my code is duplicated but it helps in
    creating an "expected" thank you note format.
    :param donator: The current donator
    :param donation_amount: The donation amount
    :return: a formatted thank you note
    '''
    list_object = []
    list_object.append("Dear {},\n\n".format(donator.title()))
    list_object.append("\tThank you for your very kind donation of  ${:10.2f}!\n".format(donation_amount))
    list_object.append("\tIt will be put to very good use.\n\n")
    list_object.append("\t\t\tSincerely,\n")
    list_object.append("\t\t\t\t\t - The Team")

    return " ".join(list_object)


def test_thank_you_note_formatted_properly():
    '''
    Tests that the thank you note is formatted as expected
    :return: No return value
    '''
    donor = "Will Smith"
    donation_amount = 100.00
    assert expected_thank_you_note_format(donor, donation_amount) == format_thank_you_note(donor, donation_amount)


def test_add_new_donor_key_exists():
    '''
    Tests that adding a new donor adds them to donor_db
    :return: No return value
    '''
    expected_donor = "Jinee"
    add_donor(expected_donor)
    assert expected_donor in donor_db.keys()


def test_add_new_donor_initializes_empty_donation_list():
    '''
    Tests that adding a new donor adds them to donor_db with empty donation list
    :return: No return value
    '''
    expected_donor = "Jinee"
    add_donor(expected_donor)
    assert len(donor_db[expected_donor]) == 0


def test_donation_report_line_matches_expected_values():
    '''
    Test that the report line is formatted correctly
    :return: No return value
    '''
    donor = ("Jinee", [1, 2, 3])
    donation_report_line = get_donation_report_for_donor(donor[0], donor[1])
    assert "Jinee" in donation_report_line
    assert "6.00" in donation_report_line
    assert "3" in donation_report_line

