#!/usr/bin/env python

# ------------------------------------------------------------------------------ #
# Title: Lesson06 - Mailroom Part 4 Unit Tests
# Description: Unit Tests for Mailroom Part 4
# ChangeLog (Who,When,What):
# Mercedes Gonzalez Gonzalez,01-30-2021, Created Unit Tests for Mailroom Part 4
# ------------------------------------------------------------------------------ #

import unittest
from unittest import mock
from mailroom import mailroom


class TestMailroom(unittest.TestCase):

    def setUp(self):
        self.filename = 'donors.txt'
        self.donor_list = [
            {"full_name": "jeff bezos", "donation_history": [30000.0, 50000.0]},
            {"full_name": "bill gates", "donation_history": [20000.0, 80000.0]},
            {"full_name": "mark zuckerberg", "donation_history": [15000.0]},
            {"full_name": "paul allen", "donation_history": [120000.0]},
            {"full_name": "steve jobs", "donation_history": [650000.0]},
        ]
        self.donor_text = (
            "jeff bezos;30000.0,50000.0\nbill gates;20000.0,80000.0\n"
            "mark zuckerberg;15000.0\npaul allen;120000.0\nsteve jobs;650000.0\n"
        )

    def test_generate_email(self):
        email_content = email_to_donor = (
            "Dear Jeff Bezos,\nWe would like to thank you for your donation. So far, you "
            "have donated $100000.00 to our organization and for that, we are grateful."
            "You are helping us continue our work supporting and growing our "
            "community.\nYou truly make a difference! We could not do this work "
            "without your support.\n\n"
        )
        result = mailroom.generate_email('jeff bezos', 100000.0)
        self.assertEqual(result, email_content)

    def test_generate_donor_records_empty(self):
        donor_records_is_empty = "There are no donors in our current database records. Please add them"
        result = mailroom.generate_donor_records([])
        self.assertEqual(donor_records_is_empty, result)

    def test_create_donor_report(self):
        sorted_donor_list = [
            {'full_name': 'steve jobs', 'donation_history': [650000.0]},
            {'full_name': 'paul allen', 'donation_history': [120000.0]},
            {'full_name': 'bill gates', 'donation_history': [20000.0, 80000.0]},
            {'full_name': 'jeff bezos', 'donation_history': [30000.0, 50000.0]},
            {'full_name': 'mark zuckerberg', 'donation_history': [15000.0]}
        ]
        with mock.patch("mailroom.mailroom.generate_donor_records") as mock_record_generator:
            mailroom.create_donor_report(self.donor_list)
            mock_record_generator.assert_called_with(sorted_donor_list)

    def test_generate_donor_records_successfully(self):
        text = ("******* The current donors are: *******\n"
                "Donor Full Name      |      Total Given |    Num Gifts    |     Average Gift\n"
                "-----------------------------------------------------------------------------"
                "\nJeff Bezos             $       80000.00                 2   $       40000.00"
                "\nBill Gates             $      100000.00                 2   $       50000.00"
                "\nMark Zuckerberg        $       15000.00                 1   $       15000.00"
                "\nPaul Allen             $      120000.00                 1   $      120000.00"
                "\nSteve Jobs             $      650000.00                 1   $      650000.00"
                )
        result = mailroom.generate_donor_records(self.donor_list)
        self.assertEqual(result, text)

    def test_read_data_from_file_successfully(self):
        mock_open = mock.mock_open(read_data=self.donor_text)
        with mock.patch("builtins.open", mock_open):
            result = mailroom.read_data_from_file(self.filename, [])
            self.assertEqual(result, self.donor_list)
            mock_open.assert_called_with('donors.txt', 'r')

    def test_read_data_from_file_no_file_found(self):
        with mock.patch("builtins.open", mock.mock_open()) as mock_open:
            mock_open.side_effect = FileNotFoundError()
            result = mailroom.read_data_from_file('donors.txt', [])
            self.assertEqual(result, [])
            mock_open.assert_called_with('donors.txt', 'r')

    def test_write_data_to_file(self):
        with mock.patch("builtins.open", mock.mock_open()) as mock_open:
            mailroom.write_data_to_file('donors.txt', self.donor_list)
            mock_open.assert_called_with('donors.txt', 'w+')
            call_1 = mock.call('jeff bezos;30000.0,50000.0\n')
            call_2 = mock.call('bill gates;20000.0,80000.0\n')
            call_3 = mock.call('mark zuckerberg;15000.0\n')
            call_4 = mock.call('paul allen;120000.0\n')
            call_5 = mock.call('steve jobs;650000.0\n')
            calls = [call_1, call_2, call_3, call_4, call_5]
            mock_open().write.assert_has_calls(calls)

    def test_say_goodbye(self):
        with mock.patch('mailroom.mailroom.write_data_to_file') as mock_write:
            mailroom.say_goodbye(self.filename, self.donor_list)
            mock_write.assert_called_with(self.filename, self.donor_list)

    def test_send_letter_to_all_donors_empty_list(self):
        with mock.patch('mailroom.mailroom.print_data_to_user') as mock_printer:
            self.assertFalse(mailroom.send_letter_to_all_donors([]))
            mock_printer.assert_called_with("There are no donors in our current database records. Please add them")

    @mock.patch('builtins.open', new_callable=mock.mock_open)
    @mock.patch('mailroom.mailroom.generate_email')
    def test_send_letter_to_all_donors(self, mock_email_generator, mock_open):
        handlers = [
            mock.mock_open().return_value,
            mock.mock_open().return_value,
            mock.mock_open().return_value,
            mock.mock_open().return_value,
            mock.mock_open().return_value,
        ]
        mock_open.side_effect = handlers

        self.assertTrue(mailroom.send_letter_to_all_donors(self.donor_list))

        call_1 = mock.call('jeff bezos', 80000.0)
        call_2 = mock.call('bill gates', 100000.0)
        call_3 = mock.call('mark zuckerberg', 15000.0)
        call_4 = mock.call('paul allen', 120000.0)
        call_5 = mock.call('steve jobs', 650000.0)
        calls = [call_1, call_2, call_3, call_4, call_5]
        mock_email_generator.assert_has_calls(calls)

        fcall_1 = mock.call('jeff_bezos.txt', 'w+')
        fcall_2 = mock.call('bill_gates.txt', 'w+')
        fcall_3 = mock.call('mark_zuckerberg.txt', 'w+')
        fcall_4 = mock.call('paul_allen.txt', 'w+')
        fcall_5 = mock.call('steve_jobs.txt', 'w+')
        fcalls = [fcall_1, fcall_2, fcall_3, fcall_4, fcall_5]
        mock_open.assert_has_calls(fcalls)

    @mock.patch('mailroom.mailroom.print_data_to_user')
    @mock.patch('mailroom.mailroom.input_choice')
    def test_send_thank_you_to_single_donor_choice_invalid(self, mock_input, mock_print):
        mock_input.side_effect = ["10", "3"]
        mailroom.send_thank_you_to_single_donor(self.donor_list)
        mock_print.assert_called_with("Your selection is invalid. Please select a menu option from 1 to 3")

    @mock.patch('mailroom.mailroom.generate_donor_records')
    @mock.patch('mailroom.mailroom.input_choice')
    def test_send_thank_you_to_single_donor_choice_list(self, mock_input, mock_record_generator):
        mock_input.side_effect = ["2", "3"]
        mailroom.send_thank_you_to_single_donor(self.donor_list)
        mock_record_generator.assert_called_with(self.donor_list)

    @mock.patch('mailroom.mailroom.generate_email')
    @mock.patch('mailroom.mailroom.print_data_to_user')
    @mock.patch('mailroom.mailroom.input_choice')
    def test_send_thank_you_to_single_donor_choice_add_new(self, mock_input, mock_print, mock_email_generator):
        mock_input.side_effect = ["1", "andrew jassy", "170000", "3"]
        mailroom.send_thank_you_to_single_donor(self.donor_list)
        mock_email_generator.assert_called_with("andrew jassy", 170000)

    @mock.patch('mailroom.mailroom.generate_email')
    @mock.patch('mailroom.mailroom.print_data_to_user')
    @mock.patch('mailroom.mailroom.input_choice')
    def test_send_thank_you_to_single_donor_choice_update_donor(self, mock_input, mock_print, mock_email_generator):
        mock_input.side_effect = ["1", "jeff bezos", "100000", "3"]
        mailroom.send_thank_you_to_single_donor(self.donor_list)
        mock_email_generator.assert_called_with("jeff bezos", 180000)

    @mock.patch('mailroom.mailroom.print_data_to_user')
    @mock.patch('mailroom.mailroom.input_choice')
    def test_send_thank_you_to_single_donor_choice_invalid_donation(self, mock_input, mock_print):
        mock_input.side_effect = ["1", "jeff bezos", "one million", "3"]
        mailroom.send_thank_you_to_single_donor(self.donor_list)
        mock_print.assert_called_with("\nThe donation amount introduced is not a valid number (i.e: 300.00). Please try again!")

    @mock.patch('mailroom.mailroom.print_data_to_user')
    @mock.patch('mailroom.mailroom.input_choice')
    def test_send_thank_you_to_single_donor_choice_zero_donation(self, mock_input, mock_print):
        mock_input.side_effect = ["1", "jeff bezos", "0", "3"]
        mailroom.send_thank_you_to_single_donor(self.donor_list)
        mock_print.assert_called_with("A donation needs to be higher than zero dollars in order to be added to the donor's records")



if __name__ == "__main__":
    unittest.main()
