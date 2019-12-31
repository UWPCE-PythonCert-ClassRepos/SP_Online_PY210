#test suite

import mailroom4
from collections import OrderedDict
import os

#Send thank you tests
#test donor list
donors = {"Paul Allen": [175, 200],
          "Tim Cook": [200]}

donors2 = {"Paul Allen": [175, 200],
          "Tim Cook": [200, 75],
          "Eric Grandeo": [50]}
 

#test adding a new donor and donation
def test_add_donor():
    mailroom4.add_donation("Tim Cook", 75, donors)    
    mailroom4.add_donation("Eric Grandeo", 50, donors)
    assert donors == donors2


#test thank you email text
def test_thankyou_email():
    letter = """
    Dear Eric Grandeo,
    Thank you very much for the generous donation of $50.00
    It is very much appreciated.
    Respectfully,

    Eric G.
    """
    expected = mailroom4.thankyou_email("Eric Grandeo", 50) 
    assert expected == letter 


#test listing donors here
def test_display_donors():
    assert mailroom4.display_donors(donors2) == list(donors2.keys())


#Create a report tests

#test report dict, tests for (donor, [totals, len, avg])
def test_create_report():
    report = mailroom4.create_report(donors2)
    expected = OrderedDict([('Paul Allen', [375, 2, 187.5]),
                            ('Tim Cook', [275, 2, 137.5]),
                            ('Eric Grandeo', [50, 1, 50.0])])
    assert report == expected


'''
#Create a report tests

#test report dict
test_ordered_dict = OrderedDict([('Bill Gates', [653784.49, 2, 326892.24]),
                                 ('Tim Cook', [85539.86, 3, 28513.29]),
                                 ('Eric Grandeo', [50000.00, 1, 50000.00]),
                                 ('Mark Zuckerberg', [16396.1, 3, 5465.37]),
                                 ('Jeff Bezos', [877.33, 1, 877.33]),
                                 ('Paul Allen', [708.42, 3, 236.14])])

#test the report dict used to create the report
def test_create_report():
    expected_report = mailroom4.create_report()
    assert expected_report == test_ordered_dict


#Create send letter test
def test_send_letters():
    pass
'''