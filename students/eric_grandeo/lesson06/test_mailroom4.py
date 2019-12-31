#test suite

#import pytest
import mailroom4

#send thank you unit tests. Your unit tests should test the data manipulation
#logic code: generating thank you text, adding or updating donors, and listing donors.

#adding or updating donors
test_addDonation = {"Bill Gates": [653772.32, 12.17],
          "Jeff Bezos": [877.33],
          "Paul Allen": [663.23, 43.87, 1.32],
          "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
          "Tim Cook": [1563.32, 8976.54, 75000]}

test_addDonors = {"Bill Gates": [653772.32, 12.17],
          "Jeff Bezos": [877.33],
          "Paul Allen": [663.23, 43.87, 1.32],
          "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
          "Tim Cook": [1563.32, 8976.54, 75000],
          "Eric Grandeo": [50000.00]}

#return donors?
def test_add_donation():
    mailroom4.add_donation("Tim Cook", 75000)
    assert mailroom4.donors == test_addDonation


def test_add_donor():
    mailroom4.add_donation("Eric Grandeo", 50000)
    assert mailroom4.donors == test_addDonors

#test thank you text
letter = """
    Dear Tim Cook,
    Thank you very much for the generous donation of $75,000.00
    It is very much appreciated.
    Respectfully,

    Eric G.
    """

def test_thankyou_email():
    expected = mailroom4.thankyou_email("Tim Cook", 75000) 
    assert expected == letter 

#test listing donors here
def test_
