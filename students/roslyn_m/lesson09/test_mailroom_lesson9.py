#!/usr/bin/env python3
# Title: Mailroom Part 4 Test (Lesson 6)
# Dev: Roslyn Melookaran
# Date: 10/28/20
# Change Log: (Who, When, What)
# R. Melookaran, 10/28/20, created script)
import mailroom_lesson9 as mail
import unittest
from unittest.mock import patch
import os

option_input_tester = 1
person_input_tester = "William Gates"
donation_input_tester = 400
ty_input_tester = "Sarah Paulson"
ty_donation_tester = 5000
donor_dict = {'William Gates': [100.00, 100.00, 100.00], 'Mark Zuckerberg': [20.00, 20.00],
              'Jeff Bezos': [50.00, 50.00, 50.00, 50.00, 50.00], 'Paul Allen': [200.00]}
donor_dict_new = {'William Gates': [100.00, 100.00, 100.00], 'Mark Zuckerberg': [20.00, 20.00],
                  'Jeff Bezos': [50.00, 50.00, 50.00, 50.00, 50.00], 'Paul Allen': [200.00], "Sarah Paulson": [5000.0]}
donor_dict_new2 = {'William Gates': [100.00, 100.00, 100.00, 500.00], 'Mark Zuckerberg': [20.00, 20.00],
                   'Jeff Bezos': [50.00, 50.00, 50.00, 50.00, 50.00], 'Paul Allen': [200.00], "Sarah Paulson": [5000.0]}
ty_input_tester2 = "William Gates"
ty_donation_tester2 = 500.0
ty_test2_assertion = "Name: William Gates, Donations: [100.0, 100.0, 100.0, 500.0]"

donor_list_sorted = [[300.0, 'William Gates', 3, 100.0], [250.0, 'Jeff Bezos', 5, 50.0],
                     [200.0, 'Paul Allen', 1, 200.0], [40.0, 'Mark Zuckerberg', 2, 20.0]]

donor1 = mail.Donor('William', 'Gates', [100.00, 100.00, 100.00])
donor2 = mail.Donor('Mark', 'Zuckerberg', [20.00, 20.00])
donor3 = mail.Donor('Jeff', 'Bezos', [50.00, 50.00, 50.00, 50.00, 50.00])
donor4 = mail.Donor('Paul', 'Allen', [200.00])
donor5 = mail.Donor('Sarah', 'Paulson', [5000.0])
donor_list = [donor1, donor2, donor3, donor4]
donor_list_new = [donor1, donor2, donor3, donor4, donor5]
donor_list_sorted = [donor1, donor3, donor4, donor2]


class TestListSum(unittest.TestCase):

    def test_run_parameters(self):
        donor1 = mail.Donor('William', 'Gates', [100.00, 100.00, 100.00])
        donor2 = mail.Donor('Mark', 'Zuckerberg', [20.00, 20.00])
        donor3 = mail.Donor('Jeff', 'Bezos', [50.00, 50.00, 50.00, 50.00, 50.00])
        donor4 = mail.Donor('Paul', 'Allen', [200.00])
        donor5 = mail.Donor('Sarah', 'Paulson', [5000])
        donor_list = [donor1, donor2, donor3, donor4]
        donor_list_new = [donor1, donor2, donor3, donor4, donor5]
        return donor_list, donor_list_new

    @patch('builtins.input', return_value=option_input_tester)
    def test_option_input(self, mock_inputs):
        """ Mock input testing the option input function
            """
        result = mail.IO.option_input()
        assert result == option_input_tester
        return

    @patch('builtins.input', return_value=person_input_tester)
    def test_person_input(self, mock_inputs):
        """ Mock input testing the person input function
            """
        result = mail.IO.person_input()
        assert result == person_input_tester
        return

    @patch('builtins.input', return_value=donation_input_tester)
    def test_donation_input(self, mock_inputs):
        """ Mock input testing the donation input function
            """
        result = mail.IO.donation_input()
        assert result == donation_input_tester
        return

    @patch('builtins.input', side_effect=[ty_input_tester, ty_donation_tester])
    def test_thank_you_note(self, mock_inputs):
        """ Mock inputs used, testing to see if new donor and their donation is added to the dict
            """
        test_ty_list = mail.Processing.thank_you_note(donor_list)
        assert str(test_ty_list[4]) == str(donor_list_new[4])
        return

    @patch('builtins.input', side_effect=[ty_input_tester2, ty_donation_tester2])
    def test_thank_you_note2(self, mock_inputs):
        """ Mock inputs used, testing to see if existing donor and their new donation is added to the dict
            """

        test_ty_list = mail.Processing.thank_you_note(donor_list)
        print(test_ty_list[0])
        assert str(test_ty_list[0]) == ty_test2_assertion
        return

    @staticmethod
    def test_sorted_list():
        result = mail.Processing.create_report(donor_list)
        assert str(result[0]) == "[300.0, 'William Gates', 3, 100.0]"
        assert str(result[1]) == "[250.0, 'Jeff Bezos', 5, 50.0]"
        assert str(result[2]) == "[200.0, 'Paul Allen', 1, 200.0]"
        assert str(result[3]) == "[40.0, 'Mark Zuckerberg', 2, 20.0]"
        return

    @staticmethod
    def test_file_creation():
        mail.Processing.send_all_thank_you(donor_list)
        current = os.getcwd()
        list_files = os.listdir(current)
        filename1 = "Paul_Allen.txt"
        filename2 = "Mark_Zuckerberg.txt"
        filename3 = "William_Gates.txt"
        filename4 = "Jeff_Bezos.txt"
        assert filename1 in list_files
        assert filename2 in list_files
        assert filename3 in list_files
        assert filename4 in list_files


