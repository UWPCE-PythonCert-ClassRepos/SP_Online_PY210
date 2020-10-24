"""
test code for mailroom_OO.py

"""

import io
import pytest
import math

# import * is often bad form, but makes it easier to test everything in a module.
from Donor_Models import *

##############################
# Step 1 - Donor Class Testing
##############################

def test_donor_init():
    '''Instantiate with donation'''
    with pytest.raises(AttributeError):
        d = Donor(15)

'''
create donor
append donation
init
str
repr