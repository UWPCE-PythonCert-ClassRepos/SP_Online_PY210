'''
Andrew Garcia
Mailroom Test
8/22/19
'''

from donor_models import *


# Test Donor Class
def test_donor():  # adds single donor
    donator = Donor('Max Rivers', 1500)
    assert donator.name == 'Max Rivers'
    assert donator.donation == 1500


def test_thank_you_donor():  # checks thank you note
    donator = Donor('Max Rivers', 1500)
    assert donator.thank_you_donor() == """Dear Max Rivers,
        Thank you for your donation of $1500.00. It is greatly appreciated!
            From, Your Favorite Charity."""


# Test DonorCollection Class
def test_donorcollection():  # checks adding donors to a list
    donator = DonorCollection()
    donator.add_donor(Donor('Max Rivers', 1500))
    assert donator.all_donations == {'Max Rivers': [1500]}

    donator.add_donor(Donor('Steve Archie', 2250))
    assert donator.all_donations == {'Max Rivers': [1500], 'Steve Archie': [2250]}

    donator2 = Donor('Mark Twins', 250)
    donator.add_donor(donator2)
    assert donator.all_donations == {'Max Rivers': [1500], 'Steve Archie': [2250], 'Mark Twins': [250]}

    donator3 = Donor('Steve Archie', 175)
    donator.add_donor(donator3)
    assert donator.all_donations == {'Max Rivers': [1500], 'Steve Archie': [2250, 175], 'Mark Twins': [250]}


def test_list_donors():  # checks that donor names are listed
    donator = DonorCollection()
    donator.add_donor(Donor('Max Rivers', 1500))
    donator.add_donor(Donor('Steve Archie', 2250))
    donator.add_donor(Donor('Mark Twins', 250))
    print(donator.list_donors())
    assert donator.list_donors() == ['Max Rivers', 'Steve Archie', 'Mark Twins']


def test_sort_donors():  # checks that donors are sorted properly
    donator = DonorCollection()
    donator.add_donor(Donor('Max Rivers', 1500))
    donator.add_donor(Donor('Steve Archie', 2250))
    donator.add_donor(Donor('Mark Twins', 250))
    donator.add_donor(Donor('Max Rivers', 150))
    donator.add_donor(Donor('Steve Archie', 50))
    donator.add_donor(Donor('Mark Twins', 2500))
    print(donator.sort_donors())
    assert donator.sort_donors() == [['Mark Twins', 2750, 2, 1375.0], ['Steve Archie', 2300, 2, 1150.0], ['Max Rivers', 1650, 2, 825.0]]



