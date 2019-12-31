#test suite

#import pytest
import mailroom4
from collections import OrderedDict

#Send thank you tests
#test donor list
test_addDonors = {"Bill Gates": [653772.32, 12.17],
          "Jeff Bezos": [877.33],
          "Paul Allen": [663.23, 43.87, 1.32],
          "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
          "Tim Cook": [1563.32, 8976.54, 75000],
          "Eric Grandeo": [50000.00]}

#test adding a new donor and donation
def test_add_donor():
    mailroom4.add_donation("Tim Cook", 75000)    
    mailroom4.add_donation("Eric Grandeo", 50000)
    assert mailroom4.donors == test_addDonors

#test letter
letter = """
    Dear Tim Cook,
    Thank you very much for the generous donation of $75,000.00
    It is very much appreciated.
    Respectfully,

    Eric G.
    """

#test thank you email text
def test_thankyou_email():
    expected = mailroom4.thankyou_email("Tim Cook", 75000) 
    assert expected == letter 

#test listing donors here
def test_display_donors():
    assert mailroom4.display_donors() == list(test_addDonors.keys())


#Create a report tests

test_ordered_dict = OrderedDict([('Bill Gates', [653784.49, 2, 326892.24]),
                                 ('Tim Cook', [85539.86, 3, 28513.29]),
                                 ('Eric Grandeo', [50000.00, 1, 50000.00]),
                                 ('Mark Zuckerberg', [16396.1, 3, 5465.37]),
                                 ('Jeff Bezos', [877.33, 1, 877.33]),
                                 ('Paul Allen', [708.42, 3, 236.14])])


def test_create_report():
    expected_report = mailroom4.create_report()
    assert expected_report == test_ordered_dict

