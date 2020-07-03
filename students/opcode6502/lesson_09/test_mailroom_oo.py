# test_mailroom.py
# opcode6502: SP_Online_PY210

import pytest
from donor_models import *

def test_donor():
    donor = Donor('Archie Adams')
    assert donor.name == 'Archie Adams'
