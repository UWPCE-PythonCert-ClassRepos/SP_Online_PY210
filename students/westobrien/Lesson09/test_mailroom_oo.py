from donor_models import *

bob = Donor('Bob', [5.00, 10.00, 20.00, 15000.00])
kathy = Donor('Kathy', [20])
sherry = Donor('Sherry', [50.00, 100.00])
sophia = Donor('Sophia', [1000.00])
chet = Donor('Chet', [10000.00, 10000.00])

d = DonorCollection([bob, kathy, sherry, sophia])

def test_1():
    assert bob.donation_list == [5.00, 10.00, 20.00, 15000.00]
    assert bob.average_donation == 3758.75
    assert bob.sum_donations == (5.00 + 10.00 + 20.00 + 15000.00)
    assert bob.name == 'Bob'

def test_2():
    assert d.list_donors == [bob, kathy, sherry, sophia]

def test_3():
    d.add_donor(chet)
    assert d.list_donors == [bob, kathy, sherry, sophia, chet]

def test_4():
    assert d.is_in_list('Chet') is True
    assert d.is_in_list('Natalie') is False

def test5():
    expected = "\n".join(("Dear {},".format(bob.name),
                          "Thank you for your very kind donation of ${:.2f}".format(
                              bob.sum_donations),
                          "\nIt will be put to very good use",
                          "Sincerely, \n\t The Team",
                          ))
    assert bob.letter_write() == expected

def test_6():
    assert bob > kathy

def test_7():
    assert d.donor_names() == ['Bob', 'Kathy', 'Sherry', 'Sophia', 'Chet']

def test_8():
    assert d.get_donor('Bob') == bob
