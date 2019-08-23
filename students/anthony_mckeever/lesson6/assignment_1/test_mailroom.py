"""
Programming In Python - Lesson 6 Assignment 1: Mailroom Part 4
Code Poet: Anthony McKeever
Start Date: 08/22/2019
End Date: 08/22/2019
"""

import io
import os
import sys
import tempfile
import unittest

import mailroom

from importlib import reload
from unittest import TestCase
from unittest import mock
from unittest.mock import patch
from unittest.mock import MagicMock


def intercept_stdout():
    hold_stdout = sys.stdout
    interceptor = io.StringIO()
    sys.stdout = interceptor

    return interceptor, hold_stdout


def invalid_option_raise_error(user_choice):
    raise Exception(user_choice)

expected_email = str("Studio Starchelle - A Fizzworks Studios Company\n"
                     "123 Starshine Ln.\n"
                     "Suite 200\n"
                     "New Sophiesville, WA, 99999\n"
                     "StudioStarchelle@fakeemail.com\n\n"
                     "Dear {},\n"
                     "\tThank you for your generous donation of ${} to our organization, Studio Starchelle.\n"
                     "This kind offering will help us grow and expand the creative operations at Fizzworks\n"
                     "Studios as well as finance the creation of new and exciting stories.\n\n"
                     "\tYour donation gives you access to exclusive content from the Starchelle*Project universe.\n"
                     "To view this content, please visit https://www.*********.com/donors and create an account using\n"
                     "the code STARCHELLE1234.\n\n"
                     "\tThank you once again for your kind donation.  With your help, we'll be able to make our next\n"
                     "graphic novel, Starchelle*Project: Shooting Star, a reality!\n\n"
                     "Sincerely,\n\n"
                     "Sophia McKeever")


expected_report = str("|-----------------------------------------------------------------------|\n"
                      "|                             Donor Report                              |\n"
                      "|---------------------+--------------+------------------+---------------|\n"
                      "| Name:               | Total Given: | Number of Gifts: | Average Gift: |\n"
                      "|---------------------+--------------+------------------+---------------|\n"
                      "| Cresenta Starchelle |    $16475.21 |                4 |      $4118.80 |\n"
                      "|---------------------+--------------+------------------+---------------|\n"
                      "| Kima Metoyo         |     $4800.00 |                2 |      $2400.00 |\n"
                      "|---------------------+--------------+------------------+---------------|\n"
                      "| Delilah Matsuka     |     $2599.98 |                3 |       $866.66 |\n"
                      "|---------------------+--------------+------------------+---------------|\n"
                      "| Katie Starchelle    |      $600.00 |                1 |       $600.00 |\n"
                      "|---------------------+--------------+------------------+---------------|\n"
                      "| Astra Matsume       |      $599.99 |                1 |       $599.99 |\n"
                      "|---------------------+--------------+------------------+---------------|\n"
                      "| Kayomi Matsuka      |        $0.01 |                1 |         $0.01 |\n"
                      "|---------------------+--------------+------------------+---------------|")


expected_donors = str("List of Donors:"
                      "\n\tCresenta Starchelle"
                      "\n\tDelilah Matsuka"
                      "\n\tAstra Matsume"
                      "\n\tKima Metoyo"
                      "\n\tKayomi Matsuka"
                      "\n\tKatie Starchelle")

class MainTests(TestCase):
    def test_reach_menu_and_exit(self):
        with patch('builtins.input') as handle_input:
            handle_input.return_value = "4"
            
            with self.assertRaises(SystemExit):
                mailroom.main()


    def test_main_menu_loop(self):
        with patch('builtins.input') as handle_input:
            handle_input.side_effect = ["1",                    # Send Thanks
                                        "Cresenta Starchelle",  # Start Donation
                                        "cancel",               # Return to Main Menu
                                        "4"]                    # Exit
            
            with self.assertRaises(SystemExit):
                mailroom.main()

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
                                     include_main=True, invalid_opt=mailroom.accept_donation)


    def test_thank_return_to_main(self):
        with patch('builtins.input') as handle_input:
            handle_input.return_value = "2"
            menu_dict = mailroom.list_dict
            
            mailroom.menu_system(menu_dict, "Test Menu", "Test Prompt",
                                 include_main=True, invalid_opt=invalid_option_raise_error)


    def test_invalid_option_overriden(self):
        exception_msg = "this should throw exception"
        with patch('builtins.input') as handle_input:
            handle_input.return_value = exception_msg
            menu_dict = mailroom.list_dict
            
            try:
                mailroom.menu_system(menu_dict, "Test Menu", "Test Prompt",
                                     include_main=True, invalid_opt=invalid_option_raise_error)
            except Exception as e:
                assert str(e).count(exception_msg) == 1


    def test_invalid_option_not_overridden(self):
        interceptor, hold_stdout = intercept_stdout()

        with patch('builtins.input') as handle_input:
            handle_input.side_effect = ["200", "4"]
            menu_dict = mailroom.main_menu_dict
            
            with self.assertRaises(SystemExit):
                mailroom.menu_system(menu_dict, "Test Menu", "Test Prompt")

            assert interceptor.getvalue().strip().count("Invalid choice.  Please select from available options.") == 1

        sys.stdout = hold_stdout

    def test_menu_print_donors_logic(self):
        interceptor, hold_stdout = intercept_stdout()

        with patch('builtins.input') as handle_input:
            handle_input.side_effect = ["1", "3"]
            menu_dict = mailroom.list_dict

            with self.assertRaises(SystemExit):
                mailroom.menu_system(menu_dict, "Test Menu", "Test Prompt",
                                     include_main=True, invalid_opt=mailroom.accept_donation)

            assert interceptor.getvalue().strip().count(expected_donors) == 1            
      
        sys.stdout = hold_stdout


class AcceptDonationTests(TestCase):
    def test_donation_existing_donor(self):
        interceptor, hold_stdout = intercept_stdout()
        cresenta = "Cresenta Starchelle"
        donation = 9999.99
        with patch('builtins.input') as handle_input:
            handle_input.return_value = f"{donation:0.02f}"
            mailroom.accept_donation(cresenta)

            assert mailroom.donor_dict[cresenta][-1] == donation
            assert interceptor.getvalue().strip().count(expected_email.format(cresenta, f"{donation:0.02f}")) == 1
        sys.stdout = hold_stdout
        reload(mailroom)

    
    def test_donation_new_donor(self):
        interceptor, hold_stdout = intercept_stdout()
        jelissa = "Jelissa Jelly"
        donation = 0.10
        with patch('builtins.input') as handle_input:
            handle_input.return_value = f"{donation:0.02f}"
            mailroom.accept_donation(jelissa)

            assert mailroom.donor_dict[jelissa][-1] == donation
            assert interceptor.getvalue().strip().count(expected_email.format(jelissa, f"{donation:0.02f}")) == 1
        sys.stdout = hold_stdout
        reload(mailroom)

    
    def test_donation_cancel(self):
        interceptor, hold_stdout = intercept_stdout()
        with patch('builtins.input') as handle_input:
            handle_input.return_value = "cancel"
            mailroom.accept_donation("Cresenta Starchelle")

            assert interceptor.getvalue().strip().count(expected_email.format("cancel", "0.00")) == 0
        sys.stdout = hold_stdout
        reload(mailroom)


    def test_donation_invalid_amount(self):
        interceptor, hold_stdout = intercept_stdout()
        cresenta = "Cresenta Starchelle"
        donation = 9999.99
        with patch('builtins.input') as handle_input:
            handle_input.side_effect = [cresenta, f"{donation:0.02f}"]
            mailroom.accept_donation(cresenta)

            assert mailroom.donor_dict[cresenta][-1] == donation
            assert interceptor.getvalue().strip().count("Invalid amount.  Try again.") == 1
            assert interceptor.getvalue().strip().count(expected_email.format(cresenta, f"{donation:0.02f}")) == 1
        sys.stdout = hold_stdout
        reload(mailroom)

            
class OutputTests(TestCase):
    def test_create_report(self):
        interceptor, hold_stdout = intercept_stdout()

        mailroom.create_report()
        assert interceptor.getvalue().strip() == expected_report
        
        sys.stdout == hold_stdout


    def test_get_email(self):
        donors = mailroom.donor_dict
        for k, v in donors.items():
            donation = v[-1]
            email = mailroom.get_email(k, donation)
            assert email == expected_email.format(k, f"{donation:.02f}")


    def test_print_donors(self):
        interceptor, hold_stdout = intercept_stdout()

        mailroom.print_donors()
        assert interceptor.getvalue().strip() == expected_donors

        sys.stdout == hold_stdout
        

class OutputDirTests(TestCase):
    def test_empty_input(self):
        with patch('builtins.input') as handle_input:
            handle_input.return_value = ""
            output = mailroom.get_user_output_path()

        assert output is None


    def test_cancel_input(self):
        with patch('builtins.input') as handle_input:
            handle_input.return_value = "cancel"
            output = mailroom.get_user_output_path()

        assert output == "cancel"


    def test_existing_dir_input(self):
        with patch('builtins.input') as handle_input:
            handle_input.return_value = tempfile.gettempdir()
            output = mailroom.get_user_output_path()

        assert output == tempfile.gettempdir()


    def test_new_dir_no_input(self):
        with patch('builtins.input') as handle_input:
            tmp_dir = os.path.join(tempfile.gettempdir(), "am_mailroom_unittest")
            handle_input.side_effect = [tmp_dir, "n"]
            output = mailroom.get_user_output_path()

        assert output is None

    
    def test_new_dir_yes_input(self):
        with patch('builtins.input') as handle_input:
            tmp_dir = os.path.join(tempfile.gettempdir(), "am_mailroom_unittest")

            with patch("os.makedirs") as make_dirs:
                handle_input.side_effect = [tmp_dir, "y"]
                output = mailroom.get_user_output_path()

                assert output == tmp_dir
                make_dirs.assert_called_once_with(tmp_dir)


    def test_new_invalid_input(self):
        interceptor, hold_stdout = intercept_stdout()

        with patch('builtins.input') as handle_input:
            tmp_dir = os.path.join(tempfile.gettempdir(), "am_mailroom_unittest")
            handle_input.side_effect = [tmp_dir, "stuff", "n"]
            output = mailroom.get_user_output_path()

        assert output is None
        assert interceptor.getvalue().count("Invalid choice.  Please enter \"Yes\" or \"No\"") == 1
        
        sys.stdout = hold_stdout


class TestSendToAll(TestCase):
    def test_write_empty_dir_emails(self):
        donors = mailroom.donor_dict
        emails = {k: expected_email.format(k, f"{v[-1]:.02f}") for k, v in donors.items()}

        with patch('builtins.input') as handle_input:
            handle_input.return_value = ""
            open_mock = mock.mock_open()

            with patch("builtins.open", open_mock, create=True):
                mailroom.send_to_all()
                open_mock.assert_called()
                
                for k, v in emails.items():
                    temp_file = os.path.join(tempfile.gettempdir(), f"{k}.txt")
                    open_mock.assert_any_call(temp_file, "w")

                    handle = open_mock()
                    handle.write.assert_any_call(v)


    def test_write_user_dir_emails(self):
        donors = mailroom.donor_dict
        emails = {k: expected_email.format(k, f"{v[-1]:.02f}") for k, v in donors.items()}
        tmp_dir = tempfile.gettempdir()
        with patch('builtins.input') as handle_input:
            handle_input.return_value = tmp_dir
            open_mock = mock.mock_open()

            with patch("builtins.open", open_mock, create=True):
                mailroom.send_to_all()
                open_mock.assert_called()
                
                for k, v in emails.items():
                    temp_file = os.path.join(tmp_dir, f"{k}.txt")
                    open_mock.assert_any_call(temp_file, "w")

                    handle = open_mock()
                    handle.write.assert_any_call(v)


    def test_cancel(self):
        with patch('builtins.input') as handle_input:
            handle_input.return_value = "cancel"
            open_mock = mock.mock_open()

            with patch("builtins.open", open_mock, create=True):
                mailroom.send_to_all()
                open_mock.assert_not_called()
                