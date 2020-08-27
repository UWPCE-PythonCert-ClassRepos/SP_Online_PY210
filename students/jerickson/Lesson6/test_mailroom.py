"""Unit Tests for rfb_station.scale_reader module

Test Cases:
    Positive: Case that runs without errors
    Negative: Case that raises unhandled errors
"""

# pylint: disable=redefined-outer-name
# pylint: disable=invalid-name
# pylint: disable=no-self-use
# pylint: disable=too-few-public-methods
# pylint: disable=too-many-locals
# pylint: disable=too-many-arguments

import pytest
from pytest_mock import mocker  # pylint: disable=unused-import

import mailroom


class Test_Report_CLI:
    """
    Tests the mailroom.menu_selection function.

    __builtins__.print() is mocked to simulate user-interaction
    mailroom.report() is mocked to provide an isolated state for each test
    """

    @pytest.mark.parametrize(
        "list_len",
        [
            pytest.param(0, id="empty_report"),
            pytest.param(1, id="one_line"),
            pytest.param(10, id="ten_lines"),
        ],
    )
    def test_report_cli(self, mocker, list_len):
        """Positive-Test-Cases"""
        # Mock
        mocked_report_list = range(1, list_len + 1)
        mocked_print = mocker.patch.object(mailroom, "print")
        mocker.patch.object(mailroom, "report", return_value=mocked_report_list)

        # Execute
        mailroom.report_cli()

        # Assert
        for _call in mocked_print.call_args_list:  # Report printed in order
            _call_arg = _call.args[0]  # Argument print was called with
            assert _call_arg == mocked_report_list[_call_arg - 1]


class Test_Report:
    """
    Tests the mailroom.report function.

    mailroom.donation_data is mocked to provide an isolated state for each test
    mailroom.sort_donation_data() is mocked to remove testing dependency
    """

    @pytest.mark.parametrize(
        "name_list, amount_list, num_gifts_list",
        [
            pytest.param(
                ["aaa", "ddd", "ccc", "bbb"],
                [9001, 1, 42, 300.2],
                [42, 1, 9, 1000],
                id="non-empty",
            ),
            pytest.param([], [], [], id="empty"),
            pytest.param(["Long" * 10, "short"], [3, 2], [3, 2], id="LongNameFormat",),
        ],
    )
    def test_report(self, mocker, name_list, amount_list, num_gifts_list):
        """Positive-Test-Cases"""
        # Setup
        mocked_donation_data = {}
        report_components = {}
        for name, amount, num_gifts in zip(name_list, amount_list, num_gifts_list):
            mocked_donation_data[name] = {"total given": amount, "num gifts": num_gifts}
            average_computed = float(amount / num_gifts)
            report_components[
                name
            ] = f"{name} {num_gifts} {amount:.2f} {average_computed:.2f}".split()

        # Mock
        mocker.patch.object(mailroom, "sort_donation_data", return_value=name_list)
        mocker.patch.object(mailroom, "donation_data", new=mocked_donation_data)

        # Execute
        actual_report_list = mailroom.report()
        actual_report_gen = (line for line in actual_report_list)

        # Assert
        for name in name_list:  # Test all rows are in order
            while True:
                report_line = next(actual_report_gen)
                if name not in report_line:  # Skip ASCII format-lines and headers
                    continue
                for report_component in report_components[name]:
                    assert report_component in report_line
                else:
                    break
        assert all(
            [len(row) == len(actual_report_list[0]) for row in actual_report_list]
        )  # Test the rows are all the same length


class Test_Sort_Donation_Data:
    """
    Tests the mailroom.sort_donation_data function.

    mailroom.donation_data is mocked to provide an isolated state for each test
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
    def test_sort_donation_data(self, mocker, name_list, amount_list, goal):
        """Positive-Test-Cases"""
        # Setup
        mocked_donation_data = {
            name: {"total given": amount}
            for name, amount in zip(name_list, amount_list)
        }

        # Mock
        mocker.patch.object(mailroom, "donation_data", new=mocked_donation_data)

        # Execute
        actual_list = mailroom.sort_donation_data()

        # Assert
        assert actual_list == goal


class Test_New_Donation:
    """
    Tests the mailroom.new_donation function.

    mailroom.donation_data is mocked to provide an isolated state for each test
    """

    @pytest.mark.parametrize(
        "name, amount",
        [
            pytest.param("Spam Eggs", 42, id="2words_int"),
            pytest.param("Cheese", 42.42, id="1word_float"),
            pytest.param(23.3, 42.42, id="number_float"),
            pytest.param("Still Adds", -42.42, id="negative_donation"),
        ],
    )
    def test_new_donation_new_donor_positive(self, mocker, name, amount):
        """New Donor, Positive-Test-Cases"""
        # Mock
        mocker.patch.object(mailroom, "donation_data", new={})

        # Execute
        mailroom.new_donation(name, amount)

        # Assert
        assert mailroom.donation_data == {
            name: {"total given": abs(amount), "num gifts": 1}
        }

    @pytest.mark.parametrize(
        "amount",
        [
            pytest.param([42], id="list"),
            pytest.param((42,), id="tuple"),
            pytest.param("42", id="string"),
        ],
    )
    def test_new_donation_new_donor_negative(self, amount):
        """New Donor, Negative-Test-Cases"""
        # Assert
        with pytest.raises(TypeError):
            mailroom.new_donation(donor_name="spam", amount=amount)

    @pytest.mark.parametrize(
        "new_amount", [pytest.param(42, id="int"), pytest.param(42.42, id="float")],
    )
    def test_new_donation_existing_donor(self, mocker, new_amount):
        """Existing Donor, Positive-Test-Cases"""
        # Setup
        name = "Existing Donor"
        existing_amount = 1
        existing_gifts = 3
        total_amount = existing_amount + new_amount
        total_gifts = existing_gifts + 1
        mocked_donation_data = {
            name: {"total given": existing_amount, "num gifts": existing_gifts}
        }

        # Mock
        mocker.patch.object(mailroom, "donation_data", new=mocked_donation_data)

        # Execute
        mailroom.new_donation(name, new_amount)

        # Assert
        assert mailroom.donation_data == {
            name: {"total given": total_amount, "num gifts": total_gifts}
        }


class Test_Donor_List:
    """
    Tests the mailroom.donor_list function.

    mailroom.donation_data is mocked to provide an isolated state for each test
    """

    @pytest.mark.parametrize(
        "name_list, goal",
        [
            pytest.param(["a", "b", "c"], "a, b, c", id="non-empty"),
            pytest.param([], "", id="empty"),
        ],
    )
    def test_donor_list(self, mocker, name_list, goal):
        """Positive-Test-Cases"""
        # Setup
        mocked_donation_data = {name: None for name in name_list}

        # Mock
        mocker.patch.object(mailroom, "donation_data", new=mocked_donation_data)

        # Execute & Assert
        assert mailroom.donor_list() == goal


class Test_Compose_All_Donors_Emails:
    """
    Tests the mailroom.compose_all_donors_emails function.

    Ensures that all required data is in the email; name, new-amount, #gifts, total-amount

    mailroom.donation_data is mocked to provide an isolated state for each test
    """

    def test_compose_all_donors_emails(self, mocker):
        """Positive-Test-Cases"""
        # Setup
        name = "Donor Name"
        gifts = 42
        total_amount = 400.2
        email_components = f"{name} {gifts} {total_amount:.2f}".split()
        mocked_donation_data = {name: {"total given": total_amount, "num gifts": gifts}}

        # Mock
        mocker.patch.object(mailroom, "donation_data", new=mocked_donation_data)

        # Execute
        emails = mailroom.compose_all_donors_emails()

        # Assert
        for file_name, email_contents in emails.items():
            assert name in file_name  # Donor Name in the file_name
            for email_component in email_components:
                assert email_component in email_contents  # Donor details in the email


class Test_Save_All_Donors_Emails:
    """
    Tests the mailroom.save_all_donor_emails function.

    mailroom.compose_all_donors_emails() is mocked to provide an isolated state for each test
    __builtins__.open() is mocked to allow intercept of email file
        mocked_file created as context manager to get file.write() arguments
    """

    def test_save_all_donors_emails(self, mocker):
        """Positive-Test-Cases"""
        # Setup
        all_files = {"spam": "eggs", "foo": "bar"}

        # Mock
        mocked_file = mocker.MagicMock()
        mocked_file.__enter__.return_value = mocked_file  # Context Manager Mock
        mocker.patch.object(
            mailroom, "compose_all_donors_emails", return_value=all_files,
        )
        mocked_open = mocker.patch.object(mailroom, "open", return_value=mocked_file)

        # Execute
        mailroom.save_all_donor_emails()

        # Assert
        assert mocked_open.call_count == len(all_files)

        for i, (file_name, file_contents) in enumerate(all_files.items()):
            assert file_name in mocked_open.call_args_list[i].args[0]
            assert file_contents == mocked_file.write.call_args_list[i].args[0]


class Test_Compose_New_Donation_Email:
    """
    Tests the mailroom.compose_new_donation_email function.

    mailroom.donation_data is mocked to provide an isolated state for each test
    """

    def test_compose_new_donation_email(self, mocker):
        """
        Compose New Donation Email, Positive-Test-Cases

        Ensures that all required data is in the email; name, new-amount, #gifts, total-amount
        """
        # Setup
        name = "New Donation"
        new_amount = 30
        gifts = 42
        total_amount = 400.2
        email_components = f"{name} {new_amount:.2f} {gifts} {total_amount:.2f}".split()

        # Mock
        record = {name: {"total given": total_amount, "num gifts": gifts}}
        mocker.patch.object(mailroom, "donation_data", new=record)

        # Execute
        actual_email = mailroom.compose_new_donation_email(name, new_amount)

        # Assert
        for email_component in email_components:
            assert email_component in actual_email


class Test_Thank_You_CLI:
    """Tests the mailroom.thank_you_cli function.

    Ensures that the user selection loop runs as expected
    __builtins__.input() is mocked to simulate user-interaction
    __builtins__.print() is mocked to simulate user-interaction
    """

    @pytest.mark.parametrize(
        "command_list",
        [
            pytest.param(["A Name", "42.2"], id="name_float"),
            pytest.param(["A Name", "42"], id="name_int"),
        ],
    )
    def test_thank_you_cli_name_number(self, mocker, command_list):
        """Positive-Test-Cases"""
        # Mock
        mocked_input_list = (n for n in command_list)

        def mocked_input(*_):
            return next(mocked_input_list)

        mocker.patch.object(mailroom, "input", new=mocked_input)
        mocker.patch.object(mailroom, "print")
        mocked_thank_you = mocker.patch.object(mailroom, "thank_you")

        # Execute
        mailroom.thank_you_cli()

        # Assert
        mocked_thank_you.assert_called_with(command_list[0], float(command_list[1]))
        assert mailroom.print.call_count == 1  # pylint: disable=no-member
        with pytest.raises(StopIteration):
            mocked_input()

    @pytest.mark.parametrize(
        "command_list",
        [
            pytest.param(["list", "quit"], id="list_quit"),
            pytest.param(["list", "name", "quit"], id="list_name_quit"),
        ],
    )
    def test_thank_you_cli_list_quit(self, mocker, command_list):
        """Positive-Test-Cases"""
        # TODO Test the return of print during 'list'?
        # Mock
        mocked_input_list = (n for n in command_list)

        def mocked_input(*_):
            return next(mocked_input_list)

        mocker.patch.object(mailroom, "input", new=mocked_input)
        mocker.patch.object(mailroom, "print")
        mocker.patch.object(mailroom, "donor_list")
        mocked_thank_you = mocker.patch.object(mailroom, "thank_you")

        # Execute
        mailroom.thank_you_cli()

        # Assert
        assert mocked_thank_you.call_count == 0
        assert mailroom.donor_list.call_count == 1  # pylint: disable=no-member
        assert mailroom.print.call_count == 1  # pylint: disable=no-member
        with pytest.raises(StopIteration):
            mocked_input()

    @pytest.mark.parametrize(
        "command_list",
        [pytest.param(["name", "non-number", "quit"], id="name_non-number"),],
    )
    def test_thank_you_cli_non_number(self, mocker, command_list):
        """Positive-Test-Cases"""
        # Mock
        mocked_input_list = (n for n in command_list)

        def mocked_input(*_):
            return next(mocked_input_list)

        mocker.patch.object(mailroom, "input", new=mocked_input)
        mocker.patch.object(mailroom, "print")
        mocked_thank_you = mocker.patch.object(mailroom, "thank_you")

        # Execute
        mailroom.thank_you_cli()

        # Assert
        assert mocked_thank_you.call_count == 0
        assert mailroom.print.call_count == 1  # pylint: disable=no-member
        with pytest.raises(StopIteration):
            mocked_input()


class Test_Thank_You:
    """
    Tests the mailroom.thank_you function.

    mailroom.new_donation() is mocked to provide an isolated state for each test
    mailroom.compose_new_donation_email() is mocked to provide an isolated state for each test
    """

    def test_sort_donation_data(self, mocker):
        """Positive-Test-Cases"""
        # Setup
        email = "email"

        # Mock
        mocker.patch.object(mailroom, "new_donation")
        mocker.patch.object(mailroom, "compose_new_donation_email", return_value=email)

        # Execute
        thank_you_email = mailroom.thank_you("1", "2")

        # Assert
        assert thank_you_email == email


class Test_Quit_Menu:
    """Tests the mailroom.quit_menu function."""

    def test_quit_menu(self):
        "The quite quiet quit test."
        # Assert
        assert mailroom.quit_menu() == "quit"


class Test_Menu_Selection:
    """
    Tests the mailroom.menu_selection function.

    mailroom.dispatch_dict is mocked to provide an isolated state for each test
    """

    def test_menu_selection_positive(self, mocker):
        """Positive-Test-Cases
        
        __builtins__.input() is mocked to simulate user-interaction
        """
        # Mock
        called_once = mocker.MagicMock()
        called_twice = mocker.MagicMock()
        called_quit = mocker.MagicMock(return_value="quit")
        command_dispatch = {
            "1": called_once,
            "2": called_twice,
            "3": called_quit,
        }

        mocked_input_list = (n for n in ["unrecognized", "1", "2", "2", "3"])

        def mocked_input(*_):
            return next(mocked_input_list)

        mocker.patch.object(mailroom, "input", new=mocked_input)

        # Execute
        mailroom.menu_selection("", dispatch_dict=command_dispatch)

        # Assert
        assert called_once.call_count == 1
        assert called_twice.call_count == 2
        assert called_quit.call_count == 1
        with pytest.raises(StopIteration):
            mocked_input()


class Test_Main:
    """
    Tests the mailroom.main function.

    mailroom.menu_selection() is mocked to provide an isolated state for each test
    """

    def test_main(self, mocker):
        """Positive-Test-Cases"""
        # Mock
        mocker.patch.object(mailroom, "menu_selection")

        # Execute
        mailroom.main()

        # Assert
        assert mailroom.menu_selection.call_count == 1  # pylint: disable=no-member
