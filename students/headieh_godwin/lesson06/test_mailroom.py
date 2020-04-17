#!/usr/bin/env python3
import mailroom
import os
import time
import sys


## test:
#email
#thanks_all()
#report()

#test all thank you emails
def test_thanks_all():

 # tests existance of file
    mailroom.thanks_all()
    parent = os.getcwd()
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = os.path.join(parent, timestr + "/" + 'Mo.txt')
    assert os.path.exists(filename)

def test_email():
    # get text from the letter to be sent
    expected0 =  (f"""
Dear Nichole,

Thank you for your very kind donation of $3.00

It will be put to very good use.

                       Sincerely,
                          -The Team""")
    expected1 =  (f"""
Dear Mo,

Thank you for your very kind donation of $2.00

It will be put to very good use.

                       Sincerely,
                          -The Team""")
    expected2 =  (f"""
Dear Larry,

Thank you for your very kind donations totaling $90.00

It will be put to very good use.

                       Sincerely,
                          -The Team""")

    assert mailroom.email(donor_name='Nichole', donation_amt=3, freq=0) == expected0
    assert mailroom.email(donor_name='Mo', donation_amt=2, freq=1) == expected1
    assert mailroom.email(donor_name='Larry', donation_amt=90, freq=2) == expected2


#test report - input 2 donors and confirm theyre descending oder
def test_report(capsys):
    expected0 = "Curly                         $    140.99           3   $          47.00"
    expected_1 =  "Mo                            $      2.00           1   $           2.00"
    expected_total = expected0 + '\n' + expected_1 #expected_1 + '\n' + expected0 - should fail
    donor = {'Mo': (2,), 'Curly': (20.99,20,100)}
    out = mailroom.report(donor)#mailroom.donors
    captured = capsys.readouterr()
    assert expected_total in captured.out
