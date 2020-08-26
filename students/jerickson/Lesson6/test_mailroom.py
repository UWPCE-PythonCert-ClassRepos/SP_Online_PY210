"""Unit Tests for rfb_station.scale_reader module"""

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

    Mocks print() to simulate user-interaction
    """

    @pytest.mark.parametrize(
        "list_len",
        [
            pytest.param(0, id="empty"),
            pytest.param(1, id="one"),
            pytest.param(10, id="ten"),
        ],
    )
    def test_report_cli(self, mocker, list_len):
        """
        Report CLI, positive-test-cases

        report(func) is mocked to provide an isolated state for each test
        """
        # Mock
        mocked_report_list = [0] * list_len
        mocked_print = mocker.MagicMock()
        mocker.patch.object(mailroom, "print", new=mocked_print)
        mocker.patch.object(mailroom, "report", return_value=mocked_report_list)

        # Execute
        mailroom.report_cli()

        # Assert
        assert mocked_print.call_count == list_len


class Test_Report:
    """
    Tests the mailroom.report function.

    donation_data(dict) is mocked to provide an isolated state for each test
    """

    @pytest.mark.parametrize(
        "name_list, amount_list, num_gifts_list, sorted_name_goal",
        [
            pytest.param(
                ["aaa", "ddd", "ccc", "bbb"],
                [9001, 1, 42, 300.2],
                [42, 1, 9, 1000],
                ["aaa", "bbb", "ccc", "ddd"],
                id="non-empty",
            ),
            pytest.param([], [], [], [], id="empty"),
        ],
    )
    def test_report(
        self, mocker, name_list, amount_list, num_gifts_list, sorted_name_goal
    ):
        """Sort Donation Data, positive-test-cases"""
        # Setup
        existing_record = {}
        report_components = {}
        for name, amount, num_gifts in zip(name_list, amount_list, num_gifts_list):
            existing_record[name] = {"total given": amount, "num gifts": num_gifts}
            average_computed = float(amount / num_gifts)
            report_components[
                name
            ] = f"{name} {num_gifts} {amount:.2f} {average_computed:.2f}".split()

        # Mock
        mocker.patch.object(mailroom, "donation_data", new=existing_record)

        # Execute
        actual_report_list = mailroom.report()
        actual_report_gen = (line for line in actual_report_list)

        # Assert
        for name in sorted_name_goal:  # Test all rows are in sorted order
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
        # Setup
        existing_record = {}
        for name, amount in zip(name_list, amount_list):
            existing_record[name] = {"total given": amount}

        # Mock
        mocker.patch.object(mailroom, "donation_data", new=existing_record)

        # Execute
        actual_list = mailroom.sort_donation_data()

        # Assert
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
            pytest.param("Still Adds", -42.42, id="negative_donation"),
        ],
    )
    def test_new_donation_new_donor_positive(self, mocker, name, amount):
        """New Donor, positive-test-cases"""
        # Mock
        mocker.patch.object(mailroom, "donation_data", new={})

        # Execute
        mailroom.new_donation(name, amount)

        # Assert
        assert mailroom.donation_data == {
            name: {"total given": abs(amount), "num gifts": 1}
        }

    def test_new_donation_new_donor_negative(self, mocker):
        """Negative-test-case, amount can't be string"""
        # Mock
        mocker.patch.object(mailroom, "donation_data", new={})

        # Assert
        with pytest.raises(TypeError):
            mailroom.new_donation(donor_name="spam", amount="eggs")

    @pytest.mark.parametrize(
        "new_amount", [pytest.param(42, id="int"), pytest.param(42.42, id="float"),],
    )
    def test_new_donation_existing_donor_existing(self, mocker, new_amount):
        """Existing Donor, positive-test-cases"""
        # Setup
        name = "Existing Donor"
        existing_amount = 1
        existing_gifts = 3
        total_amount = existing_amount + new_amount
        total_gifts = existing_gifts + 1

        # Mock
        existing_record = {
            name: {"total given": existing_amount, "num gifts": existing_gifts}
        }
        mocker.patch.object(mailroom, "donation_data", new=existing_record)

        # Execute
        mailroom.new_donation(name, new_amount)

        # Assert
        assert mailroom.donation_data == {
            name: {"total given": total_amount, "num gifts": total_gifts}
        }


class Test_Donor_List:
    """
    Tests the mailroom.donor_list function.

    donation_data(dict) is mocked to provide an isolated state for each test
    """

    @pytest.mark.parametrize(
        "name_list, goal",
        [
            pytest.param(["a", "b", "c"], "a, b, c", id="non-empty"),
            pytest.param([], "", id="empty"),
        ],
    )
    def test_new_donation_donor_list_positive(self, mocker, name_list, goal):
        """donor_list, positive-test-cases"""
        # Setup
        mocked_donation_data = {name: None for name in name_list}

        # Mock
        mocker.patch.object(mailroom, "donation_data", new=mocked_donation_data)

        # Execute & Assert
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
        # Setup
        name = "Donor Name"
        gifts = 42
        total_amount = 400.2
        email_components = f"{name} {gifts} {total_amount:.2f}".split()

        # Mock
        record = {name: {"total given": total_amount, "num gifts": gifts}}
        mocker.patch.object(mailroom, "donation_data", new=record)

        # Execute
        emails = mailroom.compose_all_donors_emails()

        # Assert
        for file_name, email_contents in emails.items():
            assert name in file_name
            for email_component in email_components:
                assert email_component in email_contents


class Test_Save_All_Donors_Emails:
    """
    Tests the mailroom.save_all_donor_emails function.

    compose_all_donors_emails(func) is mocked to provide an isolated state for each test
    open() is mocked to allow intercept of email file
    """

    def test_save_all_donors_emails_positive(self, mocker):
        """Save All Donors Emails, positive-test-cases"""
        # Setup
        file_contents = "contents"

        # Mock
        class mock_file:
            def write(self, string):
                """Mocks the write to allow access to what was written to assert against"""
                self.written = string  # pylint: disable=attribute-defined-outside-init

            def __enter__(self):
                return self

            def __exit__(self, *args):
                return self

        mocked_file = mock_file()
        mocker.patch.object(
            mailroom,
            "compose_all_donors_emails",
            return_value={"file_name": file_contents},
        )
        mocker.patch.object(mailroom, "open", return_value=mocked_file)

        # Execute
        mailroom.save_all_donor_emails()

        # Assert
        assert file_contents == mocked_file.written


class Test_Compose_New_Donation_Email:
    """
    Tests the mailroom.compose_new_donation_email function.

    donation_data(dict) is mocked to provide an isolated state for each test
    """

    def test_compose_new_donation_email_positive(self, mocker):
        """
        Compose New Donation Email, positive-test-cases

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
    """Tests the mailroom.thank_you_cli function."""

    @pytest.mark.parametrize(
        "command_list",
        [
            pytest.param(["A Name", "42.2"], id="name_float"),
            pytest.param(["A Name", "42"], id="name_int"),
        ],
    )
    def test_thank_you_cli_name_number(self, mocker, command_list):
        """Thank You CLI, positive-test-cases

        Ensures that the user selection loop runs as expected
        Mocks input() to simulate user-interaction
        Mocks print() to simulate user-interaction
        """
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
        """Thank You CLI, positive-test-cases

        Ensures that the user selection loop runs as expected
        Mocks input() to simulate user-interaction
        Mocks print() to simulate user-interaction
        """
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
        """Thank You CLI, positive-test-cases

        Ensures that the user selection loop runs as expected
        Mocks input() to simulate user-interaction
        Mocks print() to simulate user-interaction
        """
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

    new_donation(func) is mocked to provide an isolated state for each test
    compose_new_donation_email(func) is mocked to provide an isolated state for each test
    """

    def test_sort_donation_data_positive(self, mocker):
        """Sort Donation Data, positive-test-cases"""
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

    dispatch_dict(dict) is mocked to provide an isolated state for each test
    """

    def test_menu_selection_positive(self, mocker):
        """Menu Selection, positive-test-cases

        Ensures that the menu selection loop runs as expected
        Mocks input() to simulate user-interaction
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

    menu_selection(func) is mocked to provide an isolated state for each test
    """

    def test_main(self, mocker):
        """Main, positive-test-cases"""
        # Mock
        mocker.patch.object(mailroom, "menu_selection")

        # Execute
        mailroom.main()

        # Assert
        assert mailroom.menu_selection.call_count == 1  # pylint: disable=no-member
