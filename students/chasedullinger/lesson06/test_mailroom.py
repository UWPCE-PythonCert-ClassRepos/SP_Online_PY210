"""
Test suite for mailroom.py
"""

import mailroom
import os


def test_get_donor_text():
    """Check that default donor list text matches"""
    assert mailroom.get_donor_list_text() == "\nCurrent donors are:\nWilliam \
Gates, III\nJeff Bezos\nPaul Allen\nMark Zuckerberg\n"


def test_email_text():
    """Check that the email text is as expected"""
    new_text = mailroom.compose_email("Willie Nelson", 12.34)
    reference_text = "\nDear Willie Nelson,\n\
Thank you for your generous gift of $12.34! It will help Local Charity\
 achieve our mission.\n\
Best regards,\n\
Local Charity\n\n"
    assert new_text == reference_text


def test_get_donor_stats():
    """Check math on donor stats"""
    total_given, total_gifts, average_gift = mailroom.get_donor_stats(
                                                                "Paul Allen")
    # Use round to ensure the precision is as good as we need
    assert round(total_given, 2) == 708.42
    assert total_gifts == 3
    assert round(average_gift, 2) == round(708.42 / 3, 2)


def test_get_total_gift_dict():
    """Check function of get_total_gift_dict"""
    donor_stats, total_gift_dict = mailroom.get_total_gift_dict()

    reference_donor_stats = {'name': 'Paul Allen', 'total_given': 708.42,
                             'total_gifts': 3, 'average_gift': 236.14}

    assert donor_stats['Paul Allen'].keys() == reference_donor_stats.keys()
    for k in donor_stats:
        if isinstance(donor_stats[k], str):
            assert donor_stats[k] == reference_donor_stats[k]
        if isinstance(donor_stats[k], int):
            assert donor_stats[k] == reference_donor_stats[k]
        if isinstance(donor_stats[k], float):
            assert round(donor_stats[k], 2) == round(reference_donor_stats[k])

    assert total_gift_dict[653784.49] == ['William Gates, III']


def test_create_report():
    """Test the create report function"""
    text_string = mailroom.create_report()
    reference_text = "Paul Allen                 $      708.42          3  \
$      236.14"
    assert text_string.split("\n")[-2] == reference_text


def test_add_donor():
    """Add a new donor using the add_donor method and ensure it's in the
    donor db and is equal to an empty list """
    mailroom.add_donor("New Donor")
    assert "New Donor" in mailroom.donor_db
    assert mailroom.donor_db["New Donor"] == []


def test_add_donation():
    """Add a new donation to an existing donor"""
    mailroom.add_donation("William Gates, III", 100.0)
    assert mailroom.donor_db["William Gates, III"] == [653772.32, 12.17, 100.0]


def test_create_all_letters():
    """Test that all the expected letters were created on disk.
    Note that the letter text was tested in test_email_text
    """
    mailroom.create_all_letters()
    for donor in mailroom.donor_db:
        assert os.path.exists(f"{donor}.txt") is True
