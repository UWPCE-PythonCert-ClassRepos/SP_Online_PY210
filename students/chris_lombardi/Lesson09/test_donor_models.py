from donor_models import Donor
from donor_models import DonorCollection

#Test Support Functions

def initialize_donors():
    """Add preset entries into the donor log."""
    d1, d2, d3 = Donor('George Washington'), Donor('Abraham Lincoln'), Donor('James Madison')
    d4, d5 = Donor('Theodore Roosevelt'), Donor('Dwight Eisenhower')
    d1.add_donation(1789.0, 1.0, 1797.0)
    d2.add_donation(1861.0, 16.0)
    d3.add_donation(1809.0,4.0)
    d4.add_donation(1901.0, 26.0, 60.0)
    d5.add_donation(1953.00, 34.0)
    return (d1, d2, d3, d4, d5)

#Test Donor Class

def test_create_donor():
    d = Donor('Mike Jones')
    assert d.name == 'Mike Jones'

def test_add_donation():
    d = Donor('Mike Jones')
    d.add_donation(400.0)
    assert d.total_donation == 400.0
    assert d.num_donation == 1

def test_multiple_donations():
    d = Donor('Mike Jones')
    d.add_donation(400.0)
    d.add_donation(1000)
    assert d.total_donation == 1400.0
    assert d.num_donation == 2
    assert d.ave_donation == 700.0

def compare_donors():
    d1, d2 = Donor('John Smith'), Donor('Ted Williams')
    d1.add_donation(200.0)
    d1.add_donation(300.0)
    d2.add_donation(650.0)
    assert d1 < d2

def test_return_name():
    d1 = Donor('John Smith')
    assert d1.name == 'John Smith'

def test_thank_you():
    d1 = Donor('John Smith')
    ty_str = ('\nDear John Smith,\nThank you for your generous donation of '
              '$400.00!\nWe appreciate your contribution to our charity.'
              '\n\nSincerley,\nThe Mailroom\n')
    assert d1.send_thank_you(400) == ty_str

#Test DonorCollection

def test_create_donor_collection():
    dc = DonorCollection()
    assert isinstance(dc, DonorCollection)

def add_donor_to_collection():
    d1, d2 = Donor('John Smith'), Donor('Mike Jones')
    dc = DonorCollection()
    dc.add_donor(d1, d2)
    assert dc.list_donors == ['John Smith', 'Mike Jones']

def test_create_report():
    test_data = initialize_donors()
    dc = DonorCollection()
    dc.add_donor(*test_data)
    test_string = ('\nDonor Name        | Total Given |  '
                   'Num Gifts  | Average Gift\n'
                   '--------------------------------------------------------------\n'
                   'George Washington  $    3,587.00            3  $    1,195.67\n'
                   'Theodore Roosevelt $    1,987.00            3  $      662.33\n'
                   'Dwight Eisenhower  $    1,987.00            2  $      993.50\n'
                   'Abraham Lincoln    $    1,877.00            2  $      938.50\n'
                   'James Madison      $    1,813.00            2  $      906.50\n')
    assert dc.create_report() == test_string