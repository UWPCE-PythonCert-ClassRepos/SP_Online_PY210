"""
test code for SparseArray.py

"""

import io
import pytest

# import * is often bad form, but makes it easier to test everything in a module.
from SparseArray import *


def test_init():
    sa = SparseArray()
    sa = SparseArray([1,2,0,0,0,0,3,0,0,4])
