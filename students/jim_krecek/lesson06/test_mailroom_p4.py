import mailroom_p4
from mailroom_p4 import *
import os
import pytest

def test_create_report():
    report = """Donor Name               | Total Given | Num Gifts | Average Gift
-----------------------------------------------------------------
Pat Carrier               $     106.00           2  $       53.00
Jim Krecek                $      93.00           3  $       31.00
Nate Secinaro             $      65.00           3  $       21.67
Zac Fisher                $      21.00           3  $        7.00
Jess Reid                 $       3.00           1  $        3.00"""
    assert mailroom_p4.create_report() == report
    

def test_list():
    data = {"Nate Secinaro":[12,44,9],"Jess Reid":[3],"Pat Carrier":[65,41]}
    assert mailroom_p4.donor_list(data) == """Nate Secinaro
Jess Reid
Pat Carrier
"""

def test_add_update():
    # tests the addition of new donors, update of existing donors, and sending of 
    # thank you message
    
    # tests addition of new donor
    data = {"Nate Secinaro":[12,44,9],"Jess Reid":[3],"Pat Carrier":[65,41]}
    assert mailroom_p4.thanks(data, 'joe', 44) == """
Dear joe,

Thank you for your generous donation of $44.

Sincerely, Jim"""
    
    # tests update of current donor
    assert mailroom_p4.thanks(data, 'Nate Secinaro', 39) == """
Dear Nate Secinaro,

Thank you for your generous donation of $39.

Sincerely, Jim"""

def test_letters():
    # test the amount of letters generated
    data = {"Nate Secinaro":[12,44,9],"Jess Reid":[3],"Pat Carrier":[65,41]}
    mailroom_p4.write_letters("Nate Secinaro",[12,44,9])
    directory = 'C:\\Users\\Jimmer\\Git Work\\SP_Online_PY210\\students\\jim_krecek\\lesson06'
    file_num = 0
    for file in os.listdir(directory):
        if file.endswith('.txt'):
            file_num = file_num + 1
            file_name = file
    assert file_num == 1
    assert 'Nate_Secinaro.txt' == file_name
    