# ------------------------------------------------------------------------#
# !/usr/bin/env python3
# Title: test_mailroom_oo.py
# Desc: Unit Testing
# ------------------------------------------------------------------------#
from donor_models import Donor
from donor_models import DonorCollection as DC
import os


def test_donor_init_():
    donor = Donor("Jimmy Johns")
    assert type(donor) is Donor


def test_donor_name():
    donor = Donor("Jimmy Johns")
    assert donor.name == "Jimmy Johns"


def test_add_donation():
    donor = Donor("Jimmy Johns")
    donor.add_donation(100)
    assert donor.total_donations == 100


def test_previous_donation():
    donor = Donor("Jimmy Johns")
    donor.add_donation(100)
    donor.add_donation(200)
    assert donor.previous_donations == 200


def test_num_donations():
    donor = Donor("Jimmy Johns")
    donor.add_donation(100)
    donor.add_donation(200)
    assert donor.num_donations == 2


def test_total_donation():
    donor = Donor("Jimmy Johns")
    donor.add_donation(100)
    donor.add_donation(200)
    assert donor.total_donations == 300


def test_avg_donation():
    donor = Donor("Jimmy Johns")
    donor.add_donation(100)
    donor.add_donation(200)
    assert donor.avg_donation == 150


def test_create_email():
    donor = Donor("Jimmy Johns")
    donor.add_donation(100)
    result = donor.create_email
    assert result == 'Dear Jimmy Johns,\n\nThank you for your generosity, ' \
                     'your donation of $100.00 will be put' \
                     ' to good use.\n\n''Warm regards,\nMailroom Staff'


def test_donorcollection_init_():
    donor_collection = DC()
    assert type(donor_collection) is DC


def test_add_donor():
    donor_collection = DC()
    donor_collection.add_donor("Jimmy Johns", 100)
    assert donor_collection.donor_exists("Jimmy Johns") is True


def test_get_donor():
    donor_collection = DC()
    donor_collection.add_donor("Jimmy Johns", 100)
    assert donor_collection.get_donor("Jimmy Johns").name == "Jimmy Johns"
    assert donor_collection.get_donor("Jimmy Johns").donations == [100]


def test_donor_exists():
    donor_collection = DC()
    donor_collection.add_donor("Jimmy Johns", 100)
    assert donor_collection.donor_exists('Jimmy Johns') is True
    assert donor_collection.donor_exists('Dummy name1') is False
    assert donor_collection.donor_exists('Dummy name2') is False


def test_add_new_donation():
    donor_collection = DC()
    # testing adding donation to a new donor
    donor_collection.add_new_donation("Jimmy Johns", 100)
    donor_collection.add_new_donation("Jimmy Johns", 200)
    # testing adding  donation to an exsiting donor
    donor_collection.add_new_donation("Jack Ma", 200)
    assert donor_collection.get_donor("Jimmy Johns").total_donations == 300
    assert donor_collection.get_donor("Jack Ma").total_donations == 2200


def test_show_donor_list():
    donor_collection = DC()
    donor_collection.add_donor("Jimmy Johns", 100)
    assert "Jimmy Johns" in donor_collection.show_donor_list
    assert "Jeff Bezos" in donor_collection.show_donor_list
    assert "Warren Buffet" in donor_collection.show_donor_list
    assert "Bill Gates" in donor_collection.show_donor_list
    assert "Tim Cook" in donor_collection.show_donor_list
    assert "Jack Ma" in donor_collection.show_donor_list


def test_create_report():
    donor_collection = DC()
    donor_collection.add_donor("Jimmy Johns", 50)
    report = donor_collection.create_report()
    assert report[0] == 'Donor Name                | Total Given | Num Gifts | Average Gift'
    assert report[1] == '------------------------------------------------------------------'
    assert report[2] == 'Jack Ma                    $    2000.00           1  $     2000.00'
    assert report[3] == 'Warren Buffet              $    1100.00           2  $      550.00'
    assert report[4] == 'Bill Gates                 $     600.00           2  $      300.00'
    assert report[5] == 'Tim Cook                   $     300.00           1  $      300.00'
    assert report[6] == 'Jeff Bezos                 $      51.00           2  $       25.50'
    assert report[7] == 'Jimmy Johns                $      50.00           1  $       50.00'


def get_letter_text(name):
    """Get letter text for file content"""
    with open('{}.txt'.format(name), 'r') as file:
        letter = file.readlines()
    return letter


def test_send_all():
    """Test the send_all function"""
    donor_collection = DC()
    donor_collection.send_all()
    assert os.path.isfile('Jeff_Bezos.txt')
    assert os.path.isfile('Warren_Buffet.txt')
    assert os.path.isfile('Bill_Gates.txt')
    assert os.path.isfile('Tim_Cook.txt')
    assert os.path.isfile('Jack_Ma.txt')
    expected_letter = ['Dear Jeff Bezos,\n', '\n',
                       'Thank you for your generosity, your total donation amount is '
                       '$51.00.\n', '\n', 'Warm regards,\n', 'Mailroom Staff']
    assert get_letter_text('Jeff_Bezos') == expected_letter


if __name__ == "__main__":
    test_donor_init_()
    test_donor_name()
    test_add_donation()
    test_previous_donation()
    test_num_donations()
    test_total_donation()
    test_avg_donation()
    test_create_email()
    test_donorcollection_init_()
    test_send_all()
    test_add_donor()
    test_get_donor()
    test_donor_exists()
    test_show_donor_list()
    test_add_new_donation()
    test_create_report()
    test_send_all()
    print("Passed")

