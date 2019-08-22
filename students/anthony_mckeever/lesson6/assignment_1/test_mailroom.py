"""
Programming In Python - Lesson 6 Assignment 1: Mailroom Part 4
Code Poet: Anthony McKeever
Start Date: 08/22/2019
End Date: 
"""

import sys

import mailroom
import unittest

from unittest import TestCase
from unittest.mock import patch


class InputTests(TestCase):
    def test_safe_input(self):
        with patch('builtins.input') as handle_input:
            handle_input.return_value = "my test"
            output = mailroom.safe_input("test input")

            assert output == "my test"


    def test_safe_input_interupt(self):
        with patch('builtins.input') as handle_input:
            handle_input.side_effect = KeyboardInterrupt
            with self.assertRaises(SystemExit):
                mailroom.safe_input("test input")
    

    def test_safe_input_eof(self):
        with patch('builtins.input') as handle_input:
            handle_input.side_effect = EOFError
            with self.assertRaises(SystemExit):
                mailroom.safe_input("test input")


class MenuSystemTests(TestCase):
    def test_main_exit(self):
        with patch('builtins.input') as handle_input:
            handle_input.return_value = "4"
            menu_dict = mailroom.main_menu_dict

            with self.assertRaises(SystemExit):
                mailroom.menu_system(menu_dict, "Test Menu", "Test Prompt")

    
    def test_thanks_exit(self):
        with patch('builtins.input') as handle_input:
            handle_input.return_value = "3"
            menu_dict = mailroom.list_dict

            with self.assertRaises(SystemExit):
                mailroom.menu_system(menu_dict, "Test Menu", "Test Prompt",
                                     include_main=True, include_donors=True,
                                     invalid_opt=mailroom.accept_donation)


class ReportingTests(TestCase):
    
    def setUp(self):
        pass