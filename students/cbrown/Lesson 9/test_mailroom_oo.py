#!/usr/bin/env python

# testing module for mailroom part4
import os
import mailroom_oo as mail

# testing for Donor_Collection Class


def test_donor_instance():

    '''
    tests that a new donor can be created with attributes
    properly assigned
    '''

    new_donor = mail.Donor('George Washington', 10000)

    new_donor.name == 'George Washington'
    new_donor.amount == 10000


def test_donor_verify():
    '''
    tests donor_verify successfully updates dictionary depending on name given
    '''
    new_donor = mail.Donor('Bill Gates', 500)

    mail.donor_verify(new_donor)

    # checks to see 500 was added to Gates
    assert mail.donor_collection.donor_dict.get('Bill Gates') == [539000, 235642, 500]

    next_donor = mail.Donor('Bob', 100)

    mail.donor_verify(next_donor)

    # checks to verify Bob was added to donor_dict
    assert mail.donor_collection.donor_dict.get('Bob') == [100]


def test_update_donor():

    '''
    Verifies a donation amount is added to donor_collection if method update donor called
    '''

    donor = mail.Donor('Bill Gates', 500)
    donor_collection = mail.DonorCollection()

    donor_collection.update_donor(donor)

    assert 500 in donor_collection.donor_dict.get('Bill Gates')

def test_add_donor():

    '''
    Verifies a new donor can be added to donor_collection if method update add_donor called
    '''

    donor = mail.Donor('Jimi Hendrix', 1000)
    donor_collection = mail.DonorCollection()

    donor_collection.add_donor(donor)

    assert 'Jimi Hendrix' in donor_collection.donor_dict
    assert 1000 in donor_collection.donor_dict.get('Jimi Hendrix')


def test_sort_donors():
    '''
    Verifies the sorting method works to sort donor_collections by total donated
    '''

    donor_dict = {"Bill Gates": [539000, 235642],
          "Jeff Bezos": [108356, 204295, 897345],
          "Satya Nadella": [236000, 305352],
          "Mark Zuckerberg": [153956.35],
          "Mark Cuban":[459035, 369.50, 570.89]}


    donor_collection = mail.DonorCollection()

    sorted_donors = donor_collection.sort_donors()

    assert sorted_donors[0][0] == "Jeff Bezos"
    assert sorted_donors[1][0] == "Bill Gates"
    assert sorted_donors[2][0] == "Satya Nadella"
    assert sorted_donors[3][0] == "Mark Cuban"
    assert sorted_donors[4][0] == "Mark Zuckerberg"


def test_sum_amount():
    '''
    Verifies sum_amount method properly adds up a donation total for a donor
    '''
    new_donor = mail.Donor('Chaz', [1000, 1000, 1000])

    total_donated = new_donor.sum_amount()

    assert total_donated == 3000


def test_thank_you_note():
    '''
    Tests formatted message is displayed properly
    '''

    joe = mail.Donor('Joe Biden',5000)

    exp_output = ('Dear Joe Biden, \n\nThank you for your show of support and generosity. '
      'Your Donation of $5000 will contribute to saving Olympic Marmots '
      'in Washington State. These Marmota are special and a unique gift to the Olympic '
      'National Park ecosystem. As a way of saying thank you. '
      'You will be receiving your very own Olympic Marmot t-shirt in the mail!\n\n'
      'Sincerely,\n\nThe Olympic Marmot Wildlife Foundation\n')

    assert mail.thank_you_note(joe) == exp_output


def test_report_rows():
    '''
    Checks to see if each line in donor report produces expected results
    '''

    exp_result = '{:<25}${:^15}{:^15}${:^15}'.format('Bill Gates','774,642',2,'387,321')

    assert mail.report_rows('Bill Gates', [539000, 235642]) == exp_result


def test_file_created():
    '''checks to see if the file was created properly'''

    name = 'Bill Gates'
    test_message = 'This is a test'
    mail.write_file(name, test_message)
    fname = 'Bill Gates.txt'

    assert os.path.isfile(fname) is True
