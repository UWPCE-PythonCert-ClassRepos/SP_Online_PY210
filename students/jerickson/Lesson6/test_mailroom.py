"""Unit Tests for rfb_station.scale_reader module"""

# pylint: disable=redefined-outer-name
# pylint: disable=invalid-name
# pylint: disable=no-self-use
# pylint: disable=missing-class-docstring
# pylint: disable=too-few-public-methods
import pytest
from pytest_mock import mocker  # pylint: disable=unused-import

import mailroom


class Test_Sort_Donation_Data:
    """
    Tests the mailroom.sort_donation_data function.

    donation_data(dict) is mocked to provide an isolated state for each test
    """

    @pytest.mark.parametrize(
        "name_list, amount_list, goal",
        [
            pytest.param(
                ["a", "d", "c", "b"],
                [9001, 1, 42, 300.2],
                ["a", "b", "c", "d"],
                id="non-empty",
            ),
            pytest.param([], [], [], id="empty"),
        ],
    )
    def test_sort_donation_data_positive(self, mocker, name_list, amount_list, goal):
        """Sort Donation Data, positive-test-cases"""
        existing_record = {}
        for name, amount in zip(name_list, amount_list):
            existing_record[name] = {"total given": amount}

        mocker.patch.object(mailroom, "donation_data", new=existing_record)
        actual_list = mailroom.sort_donation_data()

        assert actual_list == goal


class Test_New_Donation:
    """
    Tests the mailroom.new_donation function.

    donation_data(dict) is mocked to provide an isolated state for each test
    """

    @pytest.mark.parametrize(
        "name, amount",
        [
            pytest.param("Spam Eggs", 42, id="2words_int"),
            pytest.param("Cheese", 42.42, id="1word_float"),
            pytest.param(23.3, 42.42, id="number_float"),
        ],
    )
    def test_new_donation_new_donor_positive(self, mocker, name, amount):
        """New Donor, positive-test-cases"""
        mocker.patch.object(mailroom, "donation_data", new={})
        mailroom.new_donation(name, amount)
        assert mailroom.donation_data == {name: {"total given": amount, "num gifts": 1}}

    def test_new_donation_new_donor_negative(self, mocker):
        """Negative-test-case, amount can't be string"""
        mocker.patch.object(mailroom, "donation_data", new={})
        with pytest.raises(TypeError):
            mailroom.new_donation(donor_name="spam", amount="eggs")

    @pytest.mark.parametrize(
        "new_amount", [pytest.param(42, id="int"), pytest.param(42.42, id="float"),],
    )
    def test_new_donation_existing_donor_existing(self, mocker, new_amount):
        """Existing Donor, positive-test-cases"""
        name = "Existing Donor"
        existing_amount = 1
        existing_gifts = 3
        total_amount = existing_amount + new_amount
        total_gifts = existing_gifts + 1
        existing_record = {
            name: {"total given": existing_amount, "num gifts": existing_gifts}
        }

        mocker.patch.object(mailroom, "donation_data", new=existing_record)
        mailroom.new_donation(name, new_amount)

        assert mailroom.donation_data == {
            name: {"total given": total_amount, "num gifts": total_gifts}
        }


class Test_Donor_List:
    """
    Tests the mailroom.donor_list function.

    sort_donation_data(function) is mocked to provide an isolated state for each test
    """

    @pytest.mark.parametrize(
        "name_list, goal",
        [
            pytest.param(["a", "b", "c"], " a, b, c", id="non-empty"),
            pytest.param([], "", id="empty"),
        ],
    )
    def test_new_donation_donor_list_positive(self, mocker, name_list, goal):
        """donor_list, positive-test-cases"""
        mocker.patch.object(mailroom, "sort_donation_data", return_value=name_list)
        assert mailroom.donor_list() == goal


class Test_Compose_All_Donors_Emails:
    """
    Tests the mailroom.compose_all_donors_emails function.

    donation_data(dict) is mocked to provide an isolated state for each test
    open() is mocked to allow intercept of email file
    """

    def test_compose_all_donors_emails_positive(self, mocker):
        """Compose All Donors Emails, positive-test-cases

        Ensures that all required data is in the email; name, new-amount, #gifts, total-amount
        """
        name = "Donor Name"
        gifts = 42
        total_amount = 400.2
        record = {name: {"total given": total_amount, "num gifts": gifts}}
        email_components = f"{name} {gifts} {total_amount:.2f}".split()

        class mock_file:
            def write(self, string):
                """Mocks the write to allow access to what was written to assert against"""
                self.written = string  # pylint: disable=attribute-defined-outside-init

            def __enter__(self):
                return self

            def __exit__(self, *args):
                return self

        mocked_file = mock_file()

        mocker.patch.object(mailroom, "donation_data", new=record)
        mocker.patch.object(mailroom, "open", return_value=mocked_file)

        mailroom.compose_all_donors_emails()
        for email_component in email_components:
            assert email_component in mocked_file.written


class Test_Compose_New_Donation_Email:
    """
    Tests the mailroom.compose_new_donation_email function.

    donation_data(dict) is mocked to provide an isolated state for each test
    """

    def test_compose_new_donation_email_positive(self, mocker):
        """Compose New Donation Email, positive-test-cases

        Ensures that all required data is in the email; name, new-amount, #gifts, total-amount
        """
        name = "New Donation"
        new_amount = 30
        gifts = 42
        total_amount = 400.2
        record = {name: {"total given": total_amount, "num gifts": gifts}}
        email_components = f"{name} {new_amount:.2f} {gifts} {total_amount:.2f}".split()

        mocker.patch.object(mailroom, "donation_data", new=record)
        actual_email = mailroom.compose_new_donation_email(name, new_amount)

        for email_component in email_components:
            assert email_component in actual_email


class Test_Quit_Menu:
    """Tests the mailroom.quit_menu function."""

    def test_quit_menu(self):
        "The quite quiet quit test."
        assert mailroom.quit_menu() == "quit"


class Test_Menu_Selection:
    """
    Tests the mailroom.menu_selection function.

    dispatch_dict(dict) is mocked to provide an isolated state for each test
    """

    def test_menu_selection_positive(self, mocker):
        """Menu Selection, positive-test-cases

        Ensures that the menu selection loop runs as expected
        Mocks input() to simulate user-interaction
        """
        called_once = mocker.MagicMock()
        called_twice = mocker.MagicMock()
        called_quit = mocker.MagicMock(return_value="quit")

        command_dispatch = {
            "1": called_once,
            "2": called_twice,
            "3": called_quit,
        }

        mocked_input_list = (n for n in ["unrecognized", "1", "2", "2", "3", "3"])

        def mocked_input(*_):
            return next(mocked_input_list)

        mocker.patch.object(mailroom, "input", new=mocked_input)
        mailroom.menu_selection("", dispatch_dict=command_dispatch)

        assert called_once.call_count == 1
        assert called_twice.call_count == 2
        assert called_quit.call_count == 1


class Test_Main:
    """
    Tests the mailroom.main function.

    menu_selection(func) is mocked to provide an isolated state for each test
    """

    def test_main(self, mocker):
        """Main, positive-test-cases"""

        mocker.patch.object(mailroom, "menu_selection")
        mailroom.main()

        assert mailroom.menu_selection.call_count == 1  # pylint: disable=no-member
