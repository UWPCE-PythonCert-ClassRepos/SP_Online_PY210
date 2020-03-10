#!/usr/bin/env python3

from pytest import mark, raises
from donor_models import Donor, DonorCollection


@mark.Donor
class DonorTests:

    @mark.donor
    @mark.parametrize("test_input, expected", [
        (["Bill Ackerman", [1818.18, 72.00, 54, 363636.36]])
    ])
    def test_donor_creation(self, test_input, expected):
        donor = Donor(test_input[0], test_input[1])
        print(donor)

    def test_donor_add_donation(self, test_input, expected):
        pass



@mark.DonorCollection
class DonorCollectionTests:
    """
    DonorCollection unit tests
    """
    def test_donor_collection_creation(self):
        pass

