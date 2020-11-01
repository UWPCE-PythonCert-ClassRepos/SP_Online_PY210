"""
test code for mailroom_OO.py

"""

import io
import pytest
import math
#import CLI_Main

# import * is often bad form, but makes it easier to test everything in a module.
from Donor_Models import *
from CLI_Main import *

##############################
# Step 1 - Donor Class Testing
##############################

def test_donor_init():
    '''Instantiate donors'''
    with pytest.raises(AttributeError):
        d = Donor()
    
    with pytest.raises(TypeError):
        d = Donor(15)

    d = Donor("Morgan Stanley")

@pytest.mark.parametrize(
    'a, b', [
        ('M_S', "Morgan Stanley"),
        ('C_V', "Cornelius Vanderbilt"),
        ('J_D_R', "John D. Rockefeller"),
        ('S_G', "Stephen Girard"),
        ('A_C', "Andrew Carnegie"),
    ]
)
def test_don_str(a, b):
    '''Donor class string'''
    a = Donor(b)

    assert str(a) == b

@pytest.mark.parametrize(
    'a, b', [
        ('M_S', "Morgan Stanley"),
        ('C_V', "Cornelius Vanderbilt"),
        ('J_D_R', "John D. Rockefeller"),
        ('S_G', "Stephen Girard"),
        ('A_C', "Andrew Carnegie"),
    ]
)
def test_don_repr(a, b):
    '''Donor class repr'''
    a = Donor(b)

    assert repr(a) == b

def test_init_donation():
    '''Creating first donation'''
    d = Donor('Paul')
    d.append(15)

    assert d.donations == [15]
    d.append([16, 17])
    assert d.donations == [15, 16, 17]

def test_thankyou_note():
    M_S = Donor("Morgan Stanley")
    M_S.donations = [10]
    M_S.append(7.50)

    assert M_S.thank_you() == "Thanks Morgan Stanley for your $17.50 in donations."

def test_thankyou_email():
    '''Test email text'''
    M_S = Donor("Morgan Stanley")
    M_S.donations = [10]
    M_S.append(7.5)

    assert M_S.email().startswith("Greetings Morgan Stanley")
    assert M_S.email().endswith("(DZCAWCRG)\n")

###################################
# Step 2 - Donor Collection Testing
###################################

# @pytest.mark.parametrize(
#     'a, expected', [
#         ("Morgan Stanley", True),
#         ("Cornelius Vanderbilt", True),
#         ("John D. Rockefeller", True),
#         ("Stephen Girard", True),
#         ("Andrew Carnegie", True),
#         ("William Gates", False),
#         ("Jeffery Bezos", False)
#     ]
# )
def test_col_init():
    dc = Donor_Collect()

    assert isinstance(dc.donors, list)
    '''
    assert isinstance(dc.donors[0], Donor)
    assert isinstance(dc.donors[1], Donor)
    assert isinstance(dc.donors[2], Donor)
    assert isinstance(dc.donors[3], Donor)
    assert isinstance(dc.donors[4], Donor)
    '''

def test_col_append():
    ''''Testing if Donor appends to Donor_Collection'''
    dc = Donor_Collect()
    JDR = Donor('John D. Rockefeller')
    dc.append(JDR)

    ans = False
    for i in dc.donors:
        if i == JDR:
            ans = True
        
    assert ans

    with pytest.raises(AttributeError):
        dc.append('False Item')

def test_sum_gift():
    dc = Donor_Collect()
    JDR = Donor('John D. Rockefeller')
    dc.append(JDR)
    new_dict = dc.calc_report()    

    print(new_dict)
    assert isinstance(new_dict, dict)
    assert new_dict[repr(JDR)] is not None
    assert new_dict[repr(JDR)][0] == 48.0
    assert new_dict[repr(JDR)][1] == 3 
    assert new_dict[repr(JDR)][2] == 16

def test_print_report():
    dc = Donor_Collect()
    JDR = Donor('John D. Rockefeller')
    dc.append(JDR)

    dc.print_report()
    out_file = io.StringIO()
    out_file.write(dc.print_report())
    file_contents = str(out_file)
    #print(file_contents)
    assert file_contents.startswith("Donor Name")
    assert file_contents.endswith('\n')

###################################
# Step 3 - CLI Testing
###################################

def test_cli_init():
    '''Confirms initial donor set is setup correctly'''
    assert isinstance(don_col.donors, list)
    assert MS in don_col.donors
    assert CV in don_col.donors
    assert JDR in don_col.donors
    assert SG in don_col.donors
    assert AC in don_col.donors

'''
create donor
track name?
track donations
append donation
init
str
repr


confirm starting list and values
confirm existance
don col str
don col repr
report calc
report print

CLI
'''