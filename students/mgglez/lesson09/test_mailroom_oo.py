#!/usr/bin/env python

# -------------------------------------------------------------------------------------- #
# Title: Lesson09 - Mailroom - Object Oriented
# Description: Assignment from Lesson09 - Mailroom - Object Oriented
# ChangeLog (Who,When,What):
# Mercedes Gonzalez Gonzalez,02-06-2021, Created Unit Tests for donor_models.py Classes
# -------------------------------------------------------------------------------------- #

import unittest
import pytest
from unittest import mock
from donor_models import Donor, DonorCollection


class TestDonor(unittest.TestCase):

    def test_init(self):
        donor = Donor("jeff bezos", [200000])
        self.assertEqual(donor.full_name, "Jeff Bezos")
        self.assertEqual(donor.donation_history, [200000])
        self.assertEqual(donor.total_donation_sum, 200000)
        self.assertEqual(donor.num_donation, 1)
        self.assertEqual(donor.average_donation, 200000)

        assert str(donor) == "Jeff Bezos total donation sum is : 200000"
        assert donor == eval(repr(donor))

        donor = Donor("jeff bezos")
        self.assertEqual(donor.full_name, "Jeff Bezos")
        self.assertEqual(donor.donation_history, [])
        self.assertEqual(donor.total_donation_sum, 0)
        self.assertEqual(donor.num_donation, 0)
        self.assertEqual(donor.average_donation, 0)

        with pytest.raises(ValueError) as error:
            donor = Donor("jeff bezos", 200000)
            assert "An invalid data type was provided" in error

    def test_generate_thank_you_email_to_single_donor(self):
        donor = Donor("jeff bezos", [200000, 75000])
        email_to_donor = (
            "Dear Jeff Bezos,\nWe would like to thank you for your donation. "
            "So far, you have donated $ 275000.00 to our organization and for "
            "that, we are grateful.You are helping us continue our work supporting "
            "and growing our community.\nYou truly make a difference! We could not "
            "do this work without your support.\n\n"
        )
        result = donor.generate_thank_you_email_to_single_donor()
        self.assertEqual(result, email_to_donor)

    def test_add_donation(self):
        donor = Donor("jeff bezos", [200000, 75000])
        donor.add_donation(15000)
        self.assertEqual(donor.donation_history, [200000, 75000, 15000])


class TestDonorCollection(unittest.TestCase):

    def test_init(self):
        dc = DonorCollection()
        assert dc.donor_list == []

        with pytest.raises(ValueError) as error:
            dc = DonorCollection({'full_name': 'Jeff Bezos', 'donation_history': 200000})
            assert "An invalid data type was provided" in error

        donor1 = Donor("jeff bezos", [200000])
        donor2 = Donor("Bill Gates", [150000])
        dc = DonorCollection([donor1, donor2])
        assert dc.donor_list == [donor1, donor2]
        donor3 = Donor("Steve Jobs", [150000])
        dc.donor_list += [donor3]
        assert dc.donor_list == [donor1, donor2, donor3]

        with pytest.raises(ValueError) as error:
            dc.donor_list = donor3
            assert "An invalid data type was provided" in error

    def test_add_donor(self):
        donor1 = Donor("jeff bezos", [200000])
        donor2 = Donor("Bill Gates", [150000])
        dc = DonorCollection([donor1, donor2])
        donor3 = Donor("Steve Jobs", [150000])
        dc.add_donor(donor3)
        assert dc.donor_list == [donor1, donor2, donor3]

        with pytest.raises(ValueError) as error:
            dc.add_donor({'full_name': 'Jeff Bezos', 'donation_history': 200000})
            assert "invalid type" in error

    def test_get_donor_records(self):
        donor1 = Donor("jeff bezos", [200000])
        donor2 = Donor("Bill Gates", [150000])
        dc = DonorCollection([donor1, donor2])
        assert dc.get_donor_records("Jeff Bezos") ==  donor1
        assert dc.get_donor_records("Steve Jobs") is None

    def test_generate_donor_report(self):
        donor_records_is_empty = "There are no donors in our current database records. Please add them"
        dc = DonorCollection()
        result = dc.generate_donor_report()
        assert result == donor_records_is_empty

        donor_report = (
            "******* The current donors are: *******\nDonor Full Name"
            "      |      Total Given |    Num Gifts    |     Average "
            "Gift\n---------------------------------------------------"
            "--------------------------\nJeff Bezos             $      "
            "200000.00                 1   $      200000.00\nBill Gates"
            "             $      150000.00                 1   $      "
            "150000.00"
        )
        donor1 = Donor("jeff bezos", [200000])
        donor2 = Donor("Bill Gates", [150000])
        dc = DonorCollection([donor1, donor2])
        result = dc.generate_donor_report()
        assert result == donor_report


    def test_load_donor_data_from_file(self):

        donor1 = Donor("jeff bezos", [200000])
        donor2 = Donor("Bill Gates", [150000])
        dc = DonorCollection([donor1, donor2])
        msg = "File donors.txt does not exist. The donors record history is currently empty!"

        with mock.patch("builtins.open", mock.mock_open()) as mock_open:
            mock_open.side_effect = FileNotFoundError()
            result = dc.load_donor_data_from_file('donors.txt')
            assert result == msg
            assert dc.donor_list == []
            mock_open.assert_called_with('donors.txt', 'r')

        dc = DonorCollection()
        msg = "Donors records successfully loaded from donors.txt !"
        donor_text = "jeff bezos;30000.0,50000.0\nbill gates;20000.0,80000.0\n"
        mock_open = mock.mock_open(read_data=donor_text)
        with mock.patch("builtins.open", mock_open):
            result = dc.load_donor_data_from_file('donors.txt')
            assert result == msg
            assert dc.donor_list == [Donor('bill gates', [20000.0, 80000.0]), Donor('jeff bezos', [30000.0, 50000.0])]
            assert dc.donor_list[0] > dc.donor_list[1]
            mock_open.assert_called_with('donors.txt', 'r')

    def test_build_donor_collection_from_file(self):
        msg = "Donors records successfully loaded from donors.txt !"
        donor_text = "jeff bezos;30000.0,50000.0\nbill gates;20000.0,80000.0\n"
        mock_open = mock.mock_open(read_data=donor_text)
        with mock.patch("builtins.open", mock_open):
            dc, msg_result = DonorCollection.build_donor_collection_from_file('donors.txt')
            assert msg_result == msg
            assert dc.donor_list == [Donor('bill gates', [20000.0, 80000.0]), Donor('jeff bezos', [30000.0, 50000.0])]
            mock_open.assert_called_with('donors.txt', 'r')

    def test_save_donor_data_to_file(self):
        donor1 = Donor("jeff bezos", [200000])
        donor2 = Donor("Bill Gates", [150000])
        dc = DonorCollection([donor1, donor2])
        with mock.patch("builtins.open", mock.mock_open()) as mock_open:
            dc.save_donor_data_to_file('donors.txt')
            mock_open.assert_called_with('donors.txt', 'w+')
            call_1 = mock.call('Jeff Bezos;200000\n')
            call_2 = mock.call('Bill Gates;150000\n')
            calls = [call_1, call_2]
            mock_open().write.assert_has_calls(calls)


    def test_generate_letter_to_all_donors_list_empty(self):
        dc = DonorCollection()
        msg = "There are no donors in our current database records. Please add them"
        assert dc.generate_letter_to_all_donors() == msg

    @mock.patch('builtins.open', new_callable=mock.mock_open)
    @mock.patch('donor_models.Donor.generate_thank_you_email_to_single_donor')
    def test_generate_letter_to_all_donors(self, mock_email_generator, mock_open):
        donor1 = Donor("jeff bezos", [200000])
        donor2 = Donor("Bill Gates", [150000])
        dc = DonorCollection([donor1, donor2])

        handlers = [
            mock.mock_open().return_value,
            mock.mock_open().return_value,
        ]
        mock_open.side_effect = handlers

        msg = "A letter has been successfully sent to every donor in our records!"
        assert dc.generate_letter_to_all_donors() == msg

        assert mock_email_generator.call_count == 2

        fcall_1 = mock.call('jeff_bezos.txt', 'w+')
        fcall_2 = mock.call('bill_gates.txt', 'w+')
        fcalls = [fcall_1, fcall_2]
        mock_open.assert_has_calls(fcalls)


if __name__ == "__main__":
    unittest.main()
