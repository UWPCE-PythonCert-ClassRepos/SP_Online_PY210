import mailroom
import io
import sys
import os
from datetime import date

#Test creation of report string
def test_create_report_row():
    donor = 'William'
    donations = [653772.32, 12.17]
    assert mailroom.create_individual_report_data(donor,donations) == 'William                    $   653784.49           2 $   326892.24'

#Test output for create report with default donors list
def test_create_report():
    capturedOutput = io.StringIO()                  # Create StringIO object
    sys.stdout = capturedOutput                     #  and redirect stdout.
    mailroom.create_report(mailroom.donor_db)                                     # Call function.
    sys.stdout = sys.__stdout__                     # Reset redirect.
    report_text = capturedOutput.getvalue()
    print (report_text)               # Now works as before.
    assert report_text == '''Donor Name                | Total Given | Num Gifts | Average Gift
------------------------------------------------------------------
William                    $   653784.49           2 $   326892.24
Mark                       $    16396.10           3 $     5465.37
Elon                       $    12782.12           3 $     4260.71
Jeff                       $      877.33           1 $      877.33
Paul                       $      708.42           3 $      236.14\n'''


#Test addition of real donation to donors list
def test_enter_donation():
    assert mailroom.enter_donation(mailroom.donor_db,'Jeff',20) == 20
    assert mailroom.donor_db['Jeff'] == [877.33, 20]

#Test rejection of bad donation value
def test_enter_donation():
    assert mailroom.enter_donation(mailroom.donor_db,'Jeff','Bad_String') == 0
    assert mailroom.donor_db['Jeff'] == [877.33]

#Test addirtion of donor to donor database
def test_add_donor():
    mailroom.add_donor('Kris',mailroom.donor_db)
    assert mailroom.donor_db['Kris'] == []

#Test output of listing of donosrs with donor databsae with one entry
def test_donor_list():
    donor_db = {"William": [653772.32, 12.17]}
    assert mailroom.donor_list(donor_db) == ['William']

#Test card text generator
def test_create_card_body():
    expected = '''Dear Kris:\n\n\tThank you for your generosity of your recent gift of $20.00.  It will go long way in supporting this charity.\n\n\t\tSincerely,\n\n\n\n\t\tKristoffer Jonson'''
    assert mailroom.create_card_body({'name':'Kris','donation':20}) == expected

#Test TRUE is returned after creation of card
#Test to make sure card was created
def test_create_card():
    assert mailroom.create_card('Kris',20) == True
    today = date.today()
    assert os.path.exists('./cards/Kris' + '_' + today.strftime("%b_%d_%Y") + '.txt')

#Test contents of card as expected by comparing to known good card
def test_created_card():
    today = date.today()
    filename = './cards/Sample_Card.txt'
    test_filename = './cards/Kris' + '_' + today.strftime("%b_%d_%Y") + '.txt'
    with open(filename, 'r') as f:
        with open(test_filename, 'r') as t:
            assert f.read() == t.read()
            print(f.read())
            print(t.read())
    f.closed
    t.closed