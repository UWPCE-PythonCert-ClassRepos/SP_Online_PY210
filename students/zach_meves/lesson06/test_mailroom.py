"""
Test suite for mailroom.py.

The following mailroom functions CAN be tested:
* _compose_thank_you
* _get_donor_names
* add_donation
* create_report
* all_thanks

The following mailroom functions accept user input and CANNOT be tested, but
all logic is contained in one of the above tested methods:
* _get_input -> simply a wrapper around Python ``input`` function
* _request_donation -> also a wrapper around Python ``input`` function
* _print_donors -> prints output of ``_get_donor_names``
* send_thank_you -> gets user input for donor and amount, passes arguments to ``add_donation``, and
  prints output of ``_compose_thank_you``
* _report_action -> Simply prints output of ``create_report`` surrounded by newline characters
"""

import pytest
import unittest
import mailroom
import copy
import os

# String that should be output for thanking an individual donor. First {} is donor name, second
# {} is last donation amount, third {} is total donation amount
correct_thank_string = "Dear {},\n" + \
                "    Thank you very much for your recent donation of $ {:.2f}. We truly \n" + \
                "appreciate your contribution.\n\n    Your total tax-deductible donation amount is now " + \
                "$ {:.2f}.\n\n" + \
                "Sincerely,\n" + \
                "    Zach"

correct_thank_string_no_donations = "Dear {},\n" + \
    "    Thank you for considering donating. You have currently not donated anything,\n" + \
    "but we look forward to receiving money soon.\n" + \
    "Sincerely\n    Zach"

donor_test = {"Name1": [1],
              "Name2": [1, 2]}


class TestMailroom(unittest.TestCase):

    def setUp(self) -> None:
        """Set up test by assigning donor dictionary to mailroom module"""
        self._cached_donors = mailroom._donors
        mailroom._donors = copy.deepcopy(donor_test)

    def tearDown(self) -> None:
        """Destroy test by reverting mailroom module's donors"""

        # Remove written letters, if they exist
        for name in mailroom._donors:
            try:
                os.remove(f"{name}_thanks.txt")
            except FileNotFoundError:
                pass

        mailroom._donors = self._cached_donors
        self._cached_donors = None

    def test_compose_thank_you(self):
        """Tests mailroom._compose_thank_you with existing donors"""

        # Name1 - 1 donation
        self.assertEqual(mailroom._compose_thank_you("Name1"), correct_thank_string.format("Name1", 1, 1))

        # Name2 - 2 donations
        self.assertEqual(mailroom._compose_thank_you("Name2"), correct_thank_string.format("Name2", 2, 3))

    def test_compose_thank_you_nonexistent(self):
        """Tests mailroom._compose_thank_you with a non-existent donor"""

        # NameFake - doesn't exist
        with self.assertRaises(NameError):
            mailroom._compose_thank_you("NameFake")

    def test_get_donor_names(self):
        """Tests mailroom._get_donor_names"""

        names = mailroom._get_donor_names()
        # Check that all names are contained in output
        for name in mailroom._donors.keys():
            self.assertIn(name, names)
        # Check that no other names are in the output
        self.assertEqual(len(names), len(mailroom._donors.keys()))

    def test_get_donation(self):
        """Tests mailroom.get_donation, which is called by mailroom.send_thank_you"""

        # Arguments are donor name and donation amount, modifies donor dictionary

        # Make a new donor
        mailroom.add_donation("Name0", 34.1)
        self.assertEqual(mailroom._donors["Name0"], [34.1])

        mailroom.add_donation("Name0", 21)
        self.assertEqual(mailroom._donors["Name0"], [34.1, 21])

        # Add donation to existing donor
        mailroom.add_donation("Name1", 2)
        self.assertEqual(mailroom._donors["Name1"], [1, 2])

    def test_create_report_baseline(self):
        """Tests mailroom.create_report with baseline donors"""

        # Baseline report
        report = mailroom.create_report()
        correct = "Donor Name                | Total Given | Num Gifts | Average Gift\n" + \
                  "------------------------------------------------------------------\n" + \
                  "Name2                       $      3.00           2   $       1.50\n" + \
                  "Name1                       $      1.00           1   $       1.00"
        self.assertEqual(report, correct)

    def test_create_report_added(self):
        """Tests mailroom.create_report after adding donors."""

        mailroom.add_donation("Name3", 23)
        correct = "Donor Name                | Total Given | Num Gifts | Average Gift\n" + \
                  "------------------------------------------------------------------\n" + \
                  "Name3                       $     23.00           1   $      23.00\n" + \
                  "Name2                       $      3.00           2   $       1.50\n" + \
                  "Name1                       $      1.00           1   $       1.00"
        self.assertEqual(correct, mailroom.create_report())

        mailroom.add_donation("Name3", 3)
        correct = "Donor Name                | Total Given | Num Gifts | Average Gift\n" + \
                  "------------------------------------------------------------------\n" + \
                  "Name3                       $     26.00           2   $      13.00\n" + \
                  "Name2                       $      3.00           2   $       1.50\n" + \
                  "Name1                       $      1.00           1   $       1.00"
        self.assertEqual(correct, mailroom.create_report())

        mailroom.add_donation("Name1", 50)
        correct = "Donor Name                | Total Given | Num Gifts | Average Gift\n" + \
                  "------------------------------------------------------------------\n" + \
                  "Name1                       $     51.00           2   $      25.50\n" + \
                  "Name3                       $     26.00           2   $      13.00\n" + \
                  "Name2                       $      3.00           2   $       1.50"
        self.assertEqual(correct, mailroom.create_report())

    def test_all_thanks_exist(self):
        """Tests mailroom.all_thanks creates required letters"""

        mailroom.all_thanks()
        for name in mailroom._donors.keys():
            fname = f"{name}_thanks.txt"
            self.assertTrue(os.path.exists(fname))

    def test_all_thanks_content(self):
        """Tests mailroom.all_thanks letters' content"""

        mailroom.all_thanks()

        for name in mailroom._donors.keys():
            with open(f"{name}_thanks.txt") as f:
                thanks = f.read()
            # mailroom._compose_thank_you is tested separately, can be assumed correct
            correct = mailroom._compose_thank_you(name)
            self.assertEqual(correct, thanks)


if __name__ == "__main__":
    os.chdir(os.path.abspath(os.path.dirname(__file__)))
    unittest.main()