"""
Programming In Python - Lesson 9 Assignment 1: Object Oriented Mail Room
Code Poet: Anthony McKeever
Start Date: 09/10/2019
End Date: 09/15/2019
"""

import io
import sys

from unittest import TestCase
from unittest import mock
from unittest.mock import patch

from donor_models import Donor
from donor_models import Donor_Collection


class TestHelpers():

    donor_list = ["Sophia McLoaphia,50.00,100.00",
                  "Cresenta Starchelle,50.00,100.00",
                  "Anthony Crowley,10.20,30.40",
                  "Aziraphale,50000.00,10000.00",
                  "Anathema Device,60.00,70.00"]


    @staticmethod
    def get_donor_collection():
        open_mock = mock.mock_open(read_data="{} -- {}")
        with patch("builtins.open", open_mock, create=True):
            donors = [Donor.from_string(d) for d in TestHelpers.donor_list]
            collection = Donor_Collection(donors, "idk_some_file_okay.txt")
        
        return collection


    @staticmethod
    def intercept_stdout():
        hold_stdout = sys.stdout
        interceptor = io.StringIO()
        sys.stdout = interceptor

        return interceptor, hold_stdout


    @staticmethod
    def multi_open_mock(file_name, __):
        if file_name == "probably_not_a_file.txt":
            content = "\n".join(TestHelpers.donor_list)
        elif file_name == "totes_a_real_file.txt":
            content = "{} -- {}"
        else:
            raise FileNotFoundError(f"Fuck {file_name}")
        
        file_object = mock.mock_open(read_data=content).return_value
        file_object.__iter__.return_value = TestHelpers.donor_list
        return file_object

    
    @staticmethod
    def mock_open_errors(file_name, __):
        if file_name.count("pls_fail") > 0:
            content = Exception("Test Failure")
        else:
            content = ""
        
        file_object = mock.mock_open(read_data=content).return_value
        return file_object


class DonorTests(TestCase):

    def test_donor_init(self):
        donor = Donor("Sophia McLoaphia", [99.00])
        assert donor.name == "Sophia McLoaphia"
        assert donor.donations[0] == 99.0
        assert len(donor.donations) == 1


    def test_append(self):
        donor = Donor("Sophia McLoaphia", [99.00])
        donor.accept_donation(200.23)
        assert donor.donations[-1] == 200.23


    def test_total(self):
        donor = Donor("Sophia McLoaphia", [99.00])
        donor.accept_donation(1.00)
        assert donor.total_donations == 100.0


    def test_avg(self):
        donor = Donor("Sophia McLoaphia", [50.00, 100.00])
        assert donor.average_donation == 75.0


    def test_summary(self):
        donor = Donor("Sophia McLoaphia", [50.00, 100.00])
        s = ("Sophia McLoaphia", "150.00", 2, "75.00")
        assert donor.to_summary == s


    def test_get_email(self):
        donor = Donor("Sophia McLoaphia", [50.00, 100.00])
        test_email = f"{donor.name} - {donor.donations[-1]:.02f}"
        assert donor.get_email("{} - {}") == test_email


    def test_len(self):
        donor = Donor("Sophia McLoaphia", [50.00, 100.00])
        assert len(donor) == 2


    def test_str(self):
        donor = Donor("Sophia McLoaphia", [50.00, 100.00])
        assert str(donor) == "Sophia McLoaphia,50.00,100.00"


    def test_lt(self):
        donor = Donor("Sophia McLoaphia", [50.00, 100.00])
        donor2 = Donor("Sophia McLoaphia", [100.00, 100.00])
        assert donor < donor2
        assert donor2 > donor


    def test_eq(self):
        donor = Donor("Sophia McLoaphia", [50.00, 100.00])
        donor2 = Donor("Sophia McLoaphia", [50.00, 100.00])
        assert donor == donor2


    def test_from_string(self):
        donor = Donor.from_string("Sophia McLoaphia,50.00,100.00")
        assert donor.name == "Sophia McLoaphia"
        assert donor.donations == [50.0, 100.0]


class DonorCollectionTests(TestCase):
    

    def test_init(self):
        donors = TestHelpers.get_donor_collection()
        assert len(donors) == 5
    

    def test_from_file(self):
        with patch("os.path.isfile") as is_file:
            with patch("builtins.open", new=TestHelpers.multi_open_mock, create=True):
                is_file.return_value = True
                donors = Donor_Collection.from_file("probably_not_a_file.txt",
                                                    "totes_a_real_file.txt")
                assert len(donors) == 5
                assert donors.email_template == "{} -- {}"


    def test_from_file_exception(self):
        with patch("os.path.isfile") as is_file:
            is_file.return_value = True
        with self.assertRaises(FileNotFoundError):
            Donor_Collection.from_file("a_legit_file.txt", "temporal_filament.tmpOrl")


    def test_handle_donation_gold_path(self):
        donors = TestHelpers.get_donor_collection()
        interceptor, hold_stdout = TestHelpers.intercept_stdout()

        with patch('builtins.input') as handle_input:
            handle_input.return_value = "200.00"

            donors.handle_donation("Sophia McLoaphia")
            donor = donors["Sophia McLoaphia"]
            assert interceptor.getvalue().count(donor.get_email(donors.email_template)) == 1
        
        sys.stdout = hold_stdout


    def test_handle_donation_add_donor(self):
        donors = TestHelpers.get_donor_collection()
        interceptor, hold_stdout = TestHelpers.intercept_stdout()

        with patch('builtins.input') as handle_input:
            handle_input.return_value = "200.00"

            donors.handle_donation("Suzukaze Aoba")
            donor = donors["Suzukaze Aoba"]
            assert donor is not None
            assert donor == donors[-1]
            assert interceptor.getvalue().count(donor.get_email(donors.email_template)) == 1
        
        sys.stdout = hold_stdout


    def test_handle_donation_invalid_choices(self):
        donors = TestHelpers.get_donor_collection()
        interceptor, hold_stdout = TestHelpers.intercept_stdout()

        with patch('builtins.input') as handle_input:
            handle_input.side_effect = ["stuff", "-20", "200.00"]

            donors.handle_donation("Sophia McLoaphia")
            donor = donors["Sophia McLoaphia"]
            assert interceptor.getvalue().count(donor.get_email(donors.email_template)) == 1
            assert interceptor.getvalue().count("Invalid amount.  Try again.") == 2
        
        sys.stdout = hold_stdout


    def test_handle_donation_cancel(self):
        donors = TestHelpers.get_donor_collection()
        interceptor, hold_stdout = TestHelpers.intercept_stdout()

        with patch('builtins.input') as handle_input:
            handle_input.return_value = "cancel"
            donor = donors["Anthony Crowley"]
            current_donations = len(donor)

            donors.handle_donation("Anthony Crowley")
            assert len(donor) == current_donations
            assert interceptor.getvalue().count(donor.get_email(donors.email_template)) == 0
            assert interceptor.getvalue().count("Invalid amount.  Try again.") == 0
        
        sys.stdout = hold_stdout
    

    def test_donor_summary(self):
        donors = TestHelpers.get_donor_collection()
        summaries = [d.to_summary for d in donors.donors]

        assert summaries == donors.donor_summary

    
    def test_print_donors(self):
        donors = TestHelpers.get_donor_collection()
        donor_names = "\n\t".join([d.name for d in donors.donors])
        donor_names = f"\t{donor_names}"
        assert donors.get_names == donor_names


    def test_save_to_file_golden_path(self):
        interceptor, hold_stdout = TestHelpers.intercept_stdout()
        donors = TestHelpers.get_donor_collection()
        path = "not_path/sure.txt"
        content = "\n".join(TestHelpers.donor_list)
        open_mock = mock.mock_open()

        with patch("os.path.isdir") as is_dir:
            with patch("builtins.open", open_mock, create=True):
                is_dir.return_value = True

                donors.save_to_file(path)
                open_mock.assert_any_call(path, "w")
                
                handle = open_mock()
                handle.write.assert_any_call(content)
                
                expected = f"Donor list backed up to: {path} successfully."
                assert interceptor.getvalue().count(expected) == 1

        sys.stdout = hold_stdout


    def test_save_to_file_not_dir(self):
        donors = TestHelpers.get_donor_collection()
        with patch("os.path.isdir") as is_dir:
            is_dir.return_value = False
            
            with self.assertRaises(NotADirectoryError):
                donors.save_to_file("lol")

    
    def test_save_to_file_save_fail(self):
        interceptor, hold_stdout = TestHelpers.intercept_stdout()
        donors = TestHelpers.get_donor_collection()
        
        path = "pls_fail/oopsie.txt"
        content = "\n".join(TestHelpers.donor_list)
        
        open_mock = mock.mock_open()
        open_mock.side_effect = [Exception("Failure"), open_mock()]

        with patch("os.path.isdir") as is_dir:
            with patch("builtins.open", open_mock, create=True):
                is_dir.return_value = True
                
                with self.assertRaises(IOError):
                    new_path = "./donor_list.csv"
                    donors.save_to_file(path)
                    open_mock.assert_any_call(path, "w")
                    open_mock.assert_any_call(new_path, "w")
                    
                    handle = open_mock()
                    handle.write.assert_any_call(content)

                    expected = str(f"Could not write file to: {path}\n" 
                                   f"The donor list has been backed up to: {new_path}")
                    assert interceptor.getvalue().count(expected) == 1

        sys.stdout = hold_stdout
