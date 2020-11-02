#!/usr/bin/env python3
# Title: Mailroom Part 4 Test (Lesson 6)
# Dev: Roslyn Melookaran
# Date: 10/28/20
# Change Log: (Who, When, What)
# R. Melookaran, 10/28/20, created script)
import mailroom4
import unittest
from unittest.mock import patch
import os

option_input_tester = 1
person_input_tester = "William Gates"
donation_input_tester = 400
ty_input_tester = "Sarah Paulson"
ty_donation_tester = 5000
donor_dict = {'William Gates': [100.00, 100.00, 100.00], 'Mark Zuckerberg': [20.00, 20.00], 'Jeff Bezos': [50.00, 50.00, 50.00, 50.00, 50.00], 'Paul Allen': [200.00]}
donor_dict_new = {'William Gates': [100.00, 100.00, 100.00], 'Mark Zuckerberg': [20.00, 20.00], 'Jeff Bezos': [50.00, 50.00, 50.00, 50.00, 50.00], 'Paul Allen': [200.00], "Sarah Paulson":[5000.0]}
donor_dict_new2 = {'William Gates': [100.00, 100.00, 100.00, 500.00], 'Mark Zuckerberg': [20.00, 20.00], 'Jeff Bezos': [50.00, 50.00, 50.00, 50.00, 50.00], 'Paul Allen': [200.00], "Sarah Paulson":[5000.0]}
ty_input_tester2 = "William Gates"
ty_donation_tester2 = 500.00
donor_list_sorted = [[300.0, 'William Gates', 3, 100.0], [250.0, 'Jeff Bezos', 5, 50.0], [200.0, 'Paul Allen', 1, 200.0], [40.0, 'Mark Zuckerberg', 2, 20.0]]


class TestListSum(unittest.TestCase):
    @patch('builtins.input', return_value=option_input_tester)
    def test_option_input(self,mock_inputs):
        """ Mock input testing the option input function
            """
        result = mailroom4.option_input()
        assert result == option_input_tester
        return

    @patch('builtins.input', return_value=person_input_tester)
    def test_person_input(self, mock_inputs):
        """ Mock input testing the person input function
            """
        result = mailroom4.person_input()
        assert result == person_input_tester
        return

    @patch('builtins.input', return_value=donation_input_tester)
    def test_donation_input(self, mock_inputs):
        """ Mock input testing the donation input function
            """
        result = mailroom4.donation_input()
        assert result == donation_input_tester
        return

    @patch('builtins.input', side_effect=[ty_input_tester, ty_donation_tester])
    def test_thank_you_note(self, mock_inputs):
        """ Mock inputs used, testing to see if new donor and their donation is added to the dict
            """
        test_ty_dict = mailroom4.thank_you_note(donor_dict)
        assert test_ty_dict == donor_dict_new
        return

    @patch('builtins.input', side_effect=[ty_input_tester2, ty_donation_tester2])
    def test_thank_you_note2(self, mock_inputs):
        """ Mock inputs used, testing to see if existing donor and their new donation is added to the dict
            """
        test_ty_dict = {}
        print(test_ty_dict)
        test_ty_dict = mailroom4.thank_you_note(donor_dict)
        print(test_ty_dict)
        print(donor_dict_new2)
        assert test_ty_dict == donor_dict_new2
        return

    @staticmethod
    def test_sorted_list(donor_all, donor_sorted):
        result = mailroom4.create_report(donor_all)
        print(donor_all)
        print(result)
        print(donor_sorted)
        assert result == donor_sorted
        return

    @staticmethod
    def test_file_creation(donor_all):
        mailroom4.send_all_thank_you(donor_all)
        current = os.getcwd()
        list_files = os.listdir(current)
        filename1 = "PaulAllen.txt"
        filename2 = "MarkZuckerberg.txt"
        filename3 = "WilliamGates.txt"
        filename4 = "JeffBezos.txt"
        assert filename1 in list_files
        assert filename2 in list_files
        assert filename3 in list_files
        assert filename4 in list_files


TestListSum.test_file_creation(donor_dict)
TestListSum.test_sorted_list(donor_dict, donor_list_sorted)
TestListSum.test_option_input(option_input_tester)
TestListSum.test_person_input(person_input_tester)
TestListSum.test_donation_input(donation_input_tester)
TestListSum.test_thank_you_note(ty_input_tester)
TestListSum.test_thank_you_note2(ty_input_tester2)

