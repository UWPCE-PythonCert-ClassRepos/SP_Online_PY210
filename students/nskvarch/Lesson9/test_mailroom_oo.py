#!usr/bin/env python3
# Mailroom OO exercise, unit testing module, created by Niels Skvarch

# import modules used in test
from donor_models import *
from cli_main import thanks, print_donor_list, run_report, create_thank_you_all
import os
import unittest
from unittest import mock
import io


class TestDonorModels(unittest.TestCase):
    """Test the donor_models module"""
    def test_donor(self):
        """initialize the donor object, add a few donations and test the math"""
        # test the object initialization
        d = Donor("Bob Johnson")
        assert d.name == "Bob Johnson"
        # add a donation and verify the value
        d.add_donation(50.00)
        assert d.total_donated == 50.00
        # add a second donation and verify the math for average, mean, and total
        d.add_donation(50)
        assert d.avg_donated == 50
        assert d.times_donated == 2
        assert d.total_donated == 100
        # add a donation and test the positional data call as well as the object report property
        d.add_donation(135.00)
        assert d.last_donation == 135
        assert d.report_tuple == ('Bob Johnson', '235.0', '3', '78.33333333333333')

    def test_donor_collections(self):
        """initialize a collection of donor objects and test the reporting functions"""
        # Initializing the database tests the add donor function of the collection
        data_base = DonorCollections()
        d1 = Donor("Bob Johnson")
        d1.add_donation(3772.32)
        d1.add_donation(512.17)
        data_base.add_donor(d1)
        d2 = Donor("Fred Billyjoe")
        d2.add_donation(877.33)
        d2.add_donation(455.50)
        d2.add_donation(23.45)
        data_base.add_donor(d2)
        d3 = Donor("Harry Richard")
        d3.add_donation(1.50)
        data_base.add_donor(d3)
        d4 = Donor("Old Gregg")
        d4.add_donation(1663.23)
        d4.add_donation(4300.87)
        d4.add_donation(10432.0)
        data_base.add_donor(d4)
        d5 = Donor("Jerry Vars")
        d5.add_donation(19.95)
        d5.add_donation(653.21)
        d5.add_donation(99.45)
        data_base.add_donor(d5)
        # test to see that all of the objects were added to the collection and test the donor_names function
        donor_list = data_base.donor_names
        assert donor_list == ('Bob Johnson', 'Fred Billyjoe', 'Harry Richard', 'Old Gregg', 'Jerry Vars')
        # Initialize a database collection to test the create_letter function with only 1 letter
        data_base2 = DonorCollections()
        d6 = Donor("Phil Lanthropy")
        d6.add_donation(100.00)
        d6.add_donation(100.0)
        data_base2.add_donor(d6)
        cwd = os.getcwd()
        data_base2.create_letters(cwd)
        files = os.listdir(cwd)
        txt_files = {f for f in files if f.endswith('.txt')}
        expected_files = {'PhilLanthropy.txt'}
        assert expected_files == txt_files
        # test to get donor by name
        harry_object = data_base.get_donor_by_name("Harry Richard")
        assert harry_object == d3
        # test the donor object tuple function
        donor_objects = data_base.donors
        assert donor_objects == (d1, d2, d3, d4, d5)
        # test the report list function
        report = data_base.report_list
        assert report == [('Name', 'Total Donated', 'Times Donated', 'Average Donation'), ('Old Gregg', '16396.1', '3',
                          '5465.366666666666'), ('Bob Johnson', '4284.49', '2', '2142.245'), ('Fred Billyjoe',
                          '1356.28', '3', '452.0933333333333'), ('Jerry Vars', '772.6100000000001', '3',
                          '257.5366666666667'), ('Harry Richard', '1.5', '1', '1.5')]


""" The exercise instructions said not to worry too much about testing this part of the mailroom program but I took a
crack at it anyways and quickly realized I have a data base scoping issue that I'm not sure how to resolve, I think I
need to generalize the functions in the CLI_main more so that I can unify the data base being used in the test with
the database the cli_main is returning

class TestCliMain(unittest.TestCase):
    "test the interface of the mailroom program"

    def test_thanks(self):
        data_base = DonorCollections()
        d1 = Donor("Bob Johnson")
        d1.add_donation(3772.32)
        d1.add_donation(512.17)
        data_base.add_donor(d1)
        d2 = Donor("Fred Billyjoe")
        d2.add_donation(877.33)
        d2.add_donation(455.50)
        d2.add_donation(23.45)
        data_base.add_donor(d2)
        d3 = Donor("Harry Richard")
        d3.add_donation(1.50)
        data_base.add_donor(d3)
        d4 = Donor("Old Gregg")
        d4.add_donation(1663.23)
        d4.add_donation(4300.87)
        d4.add_donation(10432.0)
        data_base.add_donor(d4)
        d5 = Donor("Jerry Vars")
        d5.add_donation(19.95)
        d5.add_donation(653.21)
        d5.add_donation(99.45)
        data_base.add_donor(d5)

        def mock_input(prompt):
            if " name" in prompt.lower():
                return "Harry Richard"
            if "amount" in prompt.lower():
                return 500

        with mock.patch("builtins.input", mock_input):
            thanks()
        most_recent_donation = d3.last_donation
        # assert most_recent_donation == 500.0 this is returning the wrong data_base object for the assertion

    def test_print_donor_list(self):
        data_base2 = DonorCollections()
        d6 = Donor("Phil Lanthropy")
        d6.add_donation(100.00)
        d6.add_donation(100.0)
        data_base2.add_donor(d6)

        donor_list_output = print_donor_list()
        assert donor_list_output == "Phil Lanthropy"
"""


# main program name-space
if __name__ == "__main__":
    unittest.main()
