#test suite

import mailroom4
from collections import OrderedDict
import os

#Send thank you tests
#test donor list

donors2 = {"Paul Allen": [175, 200],
          "Tim Cook": [200, 75],
          "Eric Grandeo": [50]}
 

#test adding a new donor and donation
def test_add_donor():
    donors = {"Paul Allen": [175, 200], "Tim Cook": [200]}
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
def test_create_report_data():
    report = mailroom4.create_report_data(donors2)
    expected = OrderedDict([('Paul Allen', [375, 2, 187.5]),
                            ('Tim Cook', [275, 2, 137.5]),
                            ('Eric Grandeo', [50, 1, 50.0])])
    assert report == expected


#Create send letter test

#tests that files are created with proper name
def test_send_letters():
    mailroom4.send_letters(donors2)
    for name in [*donors2]:
        name2 = name.replace(" ", "_")
        assert os.path.isfile(name2 + ".txt") is True

#test content of file

def test_get_letter_text():
    f = open("Eric_Grandeo.txt", "r")
    contents = f.read()
    expected = """Dear Eric Grandeo,

           Thank you very much for the generous total donation of $50.00

           It is very much appreciated.

                Respectfully,
                Eric G."""

    assert expected == contents
