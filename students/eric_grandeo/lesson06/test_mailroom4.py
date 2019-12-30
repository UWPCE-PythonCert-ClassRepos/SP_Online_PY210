#test suite

#import pytest
import mailroom4

#send thank you unit tests. Your unit tests should test the data manipulation
#logic code: generating thank you text, adding or updating donors, and listing donors.



#adding or updating donors

test_donors = {"Bill Gates": [653772.32, 12.17],
          "Jeff Bezos": [877.33],
          "Paul Allen": [663.23, 43.87, 1.32],
          "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
          "Tim Cook": [1563.32, 8976.54],
          "Eric Grandeo": [50000.00]}

def test_add_donation():
    mailroom4.add_donation("Eric Grandeo", 50000)
    assert mailroom4.donors == test_donors