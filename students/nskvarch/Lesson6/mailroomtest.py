#!usr/bin/env python3
# Unit Test script for the mailroom exercise created by Niels Skvarch

from mailroom4 import print_report, run_report, thanks, print_thankyou, create_thankyou_all, add_new_donor
import os
import unittest
import io
from contextlib import redirect_stdout
from unittest import mock
import sys

test_datalines = [('Name', 'Total Donated', 'Times Donated', 'Average Donation'),
                  ('Old Gregg', '16396.1', '3', '5465.366666666666'), ('Bob Johnson', '4284.49', '2', '2142.245'),
                  ('Fred Billyjoe', '1356.28', '3', '452.0933333333333'),
                  ('Jerry Vars', '772.6100000000001', '3', '257.5366666666667'), ('Harry Richard', '1.5', '1', '1.5')]


class test_case_one(unittest.TestCase):
    def test_print_report(self):
        test_report = ("""Name             $    Total Donated        Times Donated    	     Average Donation
Old Gregg        $    16396.1                          3    	    5465.366666666666
Bob Johnson      $    4284.49                          2    	             2142.245
Fred Billyjoe    $    1356.28                          3    	    452.0933333333333
Jerry Vars       $    772.6100000000001                3    	    257.5366666666667
Harry Richard    $    1.5                              1    	                  1.5


""")
        output = io.StringIO()
        with redirect_stdout(output):
            print_report(test_datalines)
        output.seek(0)
        output1 = output.read()
        assert output1 == test_report


class test_case_two(unittest.TestCase):
    def test_run_report(self):
        test_datastring = ("""Name             $    Total Donated        Times Donated    	     Average Donation
Old Gregg        $    16396.1                          3    	    5465.366666666666
Bob Johnson      $    4284.49                          2    	             2142.245
Fred Billyjoe    $    1356.28                          3    	    452.0933333333333
Jerry Vars       $    772.6100000000001                3    	    257.5366666666667
Harry Richard    $    1.5                              1    	                  1.5


""")
        output2 = io.StringIO()
        with redirect_stdout(output2):
            run_report()
        output2.seek(0)
        output3 = output2.read()
        assert output3 == test_datastring


class test_case_three(unittest.TestCase):
    def test_thanks(self):
        donor_db = {"Bob Johnson": [3772.32, 512.17],
                    "Fred Billyjoe": [877.33, 455.50, 23.45],
                    "Harry Richard": [1.50],
                    "Old Gregg": [1663.23, 4300.87, 10432.0],
                    "Jerry Vars": [19.95, 653.21, 99.45],
                    }

        def mock_input(prompt):
            if " name" in prompt.lower():
                return "Harry Richard"
            if "amount" in prompt.lower():
                return 500

        with mock.patch("builtins.input", mock_input):
            thanks(donor_db)
        assert donor_db["Harry Richard"][-1] == 500.0


class test_case_four(unittest.TestCase):
    def test_print_thankyou(self):
        test_name = "Old Gregg"
        test_letter = ("Dear Old Gregg,\n" +
                       "    Thank you for your donation of $ 10432.0. We \n" +
                       "appreciate your contribution.\n\n    Your total donation amount is now " +
                       "$ 16396.1.\n\n" +
                       "Sincerely,\n" +
                       "Your Charity of Choice\n")
        output6 = io.StringIO()
        with redirect_stdout(output6):
            print_thankyou(test_name)
        output6.seek(0)
        output7 = output6.read()
        assert output7 == test_letter


class test_case_five(unittest.TestCase):
    def test_create_thankyou_all(self):
        cwd = os.getcwd()

        def mock_input(prompt):
            if "directory" in prompt.lower():
                return os.getcwd()

        with mock.patch("builtins.input", mock_input):
            create_thankyou_all()

        files = os.listdir(cwd)
        txt_files = {f for f in files if f.endswith('.txt')}
        expected_files = {'FredBillyjoe.txt', 'HarryRichard.txt', 'JerryVars.txt', 'BobJohnson.txt', 'OldGregg.txt'}
        assert expected_files == txt_files


class test_case_six(unittest.TestCase):
    def test_add_new_donor(self):
        donor_db = {"Bob Johnson": [3772.32, 512.17],
                    "Fred Billyjoe": [877.33, 455.50, 23.45],
                    "Harry Richard": [1.50],
                    "Old Gregg": [1663.23, 4300.87, 10432.0],
                    "Jerry Vars": [19.95, 653.21, 99.45],
                    }
        name = "Franky Jazzhands"
        amount = 600.0
        add_new_donor(donor_db, name, amount)  # keyerror on franky, donor_db returns without him in it still even though he is in it as he starts showing up in the other test reports
        assert donor_db["Franky Jazzhands"][-1] == 600.0


# main program name-space
if __name__ == "__main__":
    unittest.main()
