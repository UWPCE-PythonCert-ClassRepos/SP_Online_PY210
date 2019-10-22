"""
Programming In Python - Lesson 9 Assignment 1: Object Oriented Mail Room
Code Poet: Anthony McKeever
Start Date: 09/10/2019
End Date: 09/15/2019
"""

import os.path
import sys
import tempfile

from unittest import TestCase
from unittest import mock
from unittest.mock import patch

import cli_main
from test_donor_model import TestHelpers
from support import Helpers


class mock_args():
    donors = "./donor_list.csv"
    email = "./email_template.csv"


class TestMain(TestCase):

    def test_main_golden_path(self):
        with patch('builtins.input') as handle_input:
            handle_input.return_value = "4"
            open_mock = mock.mock_open()
            cli_main.donor_list = TestHelpers.get_donor_collection()
            
            with patch("os.path.isdir") as is_dir:
                is_dir.return_value = True

                with patch("builtins.open", open_mock, create=True):
                    with self.assertRaises(SystemExit):
                        cli_main.main(mock_args)


    def test_main_invalid_opt(self):
        interceptor, hold_stdout = TestHelpers.intercept_stdout()

        with patch('builtins.input') as handle_input:
            handle_input.side_effect = ["Self Destruct", "4"]
            open_mock = mock.mock_open()
            cli_main.donor_list = TestHelpers.get_donor_collection()
            
            with patch("os.path.isdir") as is_dir:
                is_dir.return_value = True

                with patch("builtins.open", open_mock, create=True):
                    with self.assertRaises(SystemExit):
                        cli_main.main(mock_args)

                        expected = "Invalid choice.  Please select from the available options."
                        assert interceptor.getvalue().count(expected) == 1

        sys.stdout = hold_stdout
        

    def test_send_thanks(self):
        interceptor, hold_stdout = TestHelpers.intercept_stdout()
        donors = TestHelpers.get_donor_collection()
        cli_main.donor_list = donors

        with patch('builtins.input') as handle_input:
            handle_input.side_effect = ["1", "2"]
            cli_main.send_thanks()

            assert interceptor.getvalue().count(donors.get_names) == 1

        sys.stdout = hold_stdout


    def test_send_thanks_invalid_opt(self):
        interceptor, hold_stdout = TestHelpers.intercept_stdout()
        donors = TestHelpers.get_donor_collection()
        cli_main.donor_list = donors

        with patch('builtins.input') as handle_input:
            current_donors = len(donors)
            handle_input.side_effect = ["1", "Andromeda Starchelle", "200.00"]
            cli_main.send_thanks()

            assert len(donors) == current_donors + 1
            donor = donors["Andromeda Starchelle"]
            assert len(donor) == 1
            assert interceptor.getvalue().count(donor.get_email(donors.email_template)) == 1

        sys.stdout = hold_stdout


    def test_create_report(self):
        interceptor, hold_stdout = TestHelpers.intercept_stdout()

        donors = TestHelpers.get_donor_collection()
        cli_main.donor_list = donors

        headers = ["Name:", "Total Given:", "Number of Gifts:", "Average Gift:"]
        summary = [d.to_summary for d in donors] 
        lengths = Helpers.get_legnths(summary, headers) 
    
        cli_main.create_report()
        
        for s in summary:
            expected = Helpers.format_line(s, lengths)
            assert interceptor.getvalue().count(expected) == 1
        
        expected = Helpers.format_line(headers, lengths)
        assert interceptor.getvalue().count(expected) == 1

        sys.stdout = hold_stdout


    def test_send_to_all_golden_path(self):
        donors = TestHelpers.get_donor_collection()
        cli_main.donor_list = donors

        with patch('builtins.input') as handle_input:
            handle_input.return_value = ""

            open_mock = mock.mock_open()
            with patch("builtins.open", open_mock, create=True):
                cli_main.send_to_all()
                
                tmp_dir = tempfile.gettempdir()
                handle = open_mock()
                
                for d in donors.donors:
                    file_name = os.path.join(tmp_dir, f"{d.name}.txt")
                    open_mock.assert_any_call(file_name, "w")
                    handle.write.assert_any_call(d.get_email(donors.email_template))


    def test_send_to_all_cancel(self):
        donors = TestHelpers.get_donor_collection()
        cli_main.donor_list = donors

        interceptor, hold_stdout = TestHelpers.intercept_stdout()

        with patch('builtins.input') as handle_input:
            handle_input.return_value = "CaNcEl"
            cli_main.send_to_all()
            expected = "Cancelling send to all.  Returning to main menu..."
            assert interceptor.getvalue().count(expected) == 1

        sys.stdout = hold_stdout
