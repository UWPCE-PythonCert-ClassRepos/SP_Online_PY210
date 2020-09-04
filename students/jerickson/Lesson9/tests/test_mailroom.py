"""Integration Tests for mailroom package

Test Cases:
    Positive: Case that runs without errors
    Negative: Case that raises unhandled errors
"""
# pylint: disable=invalid-name
# pylint: disable=no-self-use
# pylint: disable=redefined-outer-name
# pylint: disable=too-few-public-methods

import pytest

from pytest_mock import mocker  # pylint: disable=unused-import

from mailroom import cli_main


def generate_mocked_input(command_list):
    """
    Return a mocked input() that will run through command_list once.

    Use by calling mocker.patch.object(obj,method,new=mocked_input)
    """
    input_list = (n for n in command_list)

    # Mock
    def mocked_input(*_):
        return next(input_list)

    return mocked_input


def count_empty_donors(inst):
    """Return number of donors with donations in the record."""
    non_empty_donors = 0
    for donor, data in inst.record.donors.items():
        if data.total_given:
            non_empty_donors += 1
    return non_empty_donors


@pytest.fixture
def mocked_print(mocker):
    """Mocked version of print to simulate user interaction."""
    return mocker.patch.object(cli_main, "print")


@pytest.fixture
def inst_populated():
    """Cli instance pre-populated with 2 donors"""
    inst = cli_main.Cli()
    inst.record.add_donor("spam")
    inst.record.add_donor("eggs")
    inst.record.donors["spam"].add_donation(4242)
    inst.record.donors["eggs"].add_donation(42)

    inst.record.add_donor("cheese")  # Empty Donor
    return inst


class Test_Mailroom_Main_Menu:
    """Tests the cli_main.cli.main_menu"""

    def test_mailroom_main_menu_empty(self, mocker):
        """Positive-Test-Cases"""
        # Setup
        command_list = [
            "",  # empty
            "0",  # quit
        ]

        # Mock
        mocked_input = generate_mocked_input(command_list)
        mocked_input = mocker.patch.object(cli_main, "input", new=mocked_input)

        # Execute
        cli_main.main()

        # # Assert
        with pytest.raises(StopIteration):  # Assert command list was emptied
            mocked_input()


class Test_Mailroom_Thanks_Menu:
    """Tests the cli_main thanks menu"""

    def test_mailroom_add_single_donor(self, mocker):
        """Positive-Test-Cases"""
        # Setup
        inst = cli_main.Cli()
        donor_name = "spam"
        donor_amount = "42"

        command_list = [
            "1",  # thanks
            donor_name,  # donor name
            donor_amount,  # donor amount
            "0",  # quit
        ]
        inst = cli_main.Cli()

        # Mock
        mocked_input = generate_mocked_input(command_list)
        mocked_input = mocker.patch.object(cli_main, "input", new=mocked_input)

        # Execute
        inst.run_menu()

        # Assert
        assert len(inst.record.donor_list) == 1
        assert donor_name in inst.record.donors
        assert inst.record.donors[donor_name].total_given == float(donor_amount)
        with pytest.raises(StopIteration):  # Assert command list was emptied
            mocked_input()

    def test_mailroom_add_multiple_donors(self, mocker):
        """Positive-Test-Cases"""
        # Setup
        inst = cli_main.Cli()
        donor_names = ["spam", "eggs"]
        donor_amount = "42"

        command_list = [
            "1",  # thanks
            donor_names[0],  # donor name
            donor_amount,  # donor amount
            "1",  # thanks
            donor_names[1],  # donor name
            donor_amount,  # donor amount
            "0",  # quit
        ]
        inst = cli_main.Cli()

        # Mock
        mocked_input = generate_mocked_input(command_list)
        mocked_input = mocker.patch.object(cli_main, "input", new=mocked_input)

        # Execute
        inst.run_menu()

        # Assert
        assert len(inst.record.donor_list) == 2
        for donor_name in donor_names:
            assert donor_name in inst.record.donors
        assert inst.record.donors[donor_name].total_given == float(donor_amount)
        with pytest.raises(StopIteration):  # Assert command list was emptied
            mocked_input()

    def test_mailroom_thanks_quits(self, mocker):
        """Positive-Test-Cases"""
        # Setup
        inst = cli_main.Cli()
        donor_name = "spam"
        donor_amount = "42"

        command_list = [
            "1",  # thanks_menu
            "1",  # thanks_menu
            "0",  # quit thanks_menu
            "1",  # thanks_menu
            donor_name,  # thanks_menu
            "0",  # quit amount_menu
            "1",  # thanks_menu
            donor_name,  # thanks_menu
            donor_amount,  # amount_menu
            "0",  # quit main_menu
        ]
        inst = cli_main.Cli()

        # Mock
        mocked_input = generate_mocked_input(command_list)
        mocked_input = mocker.patch.object(cli_main, "input", new=mocked_input)

        # Execute
        inst.run_menu()

        # Assert
        assert len(inst.record.donor_list) == 1
        assert donor_name in inst.record.donors
        assert inst.record.donors[donor_name].total_given == float(donor_amount)
        with pytest.raises(StopIteration):  # Assert command list was emptied
            mocked_input()

    def test_mailroom_thanks_donor_id_valid(self, mocker, mocked_print, inst_populated):
        """Positive-Test-Cases"""
        # Setup
        inst = inst_populated
        donor_0 = inst.record.donor_list[0]

        command_list = [
            "1",  # thanks_menu
            "D0",  # thanks_menu enter donor_id
            "0",  # quit amount_menu
            "0",  # quit thanks_menu
            "0",  # quit
        ]

        # Mock
        mocked_input = generate_mocked_input(command_list)
        mocked_input = mocker.patch.object(cli_main, "input", new=mocked_input)

        # Execute
        inst.run_menu()

        # Assert
        assert donor_0 in mocked_print.call_args[0][0]
        assert mocked_print.call_count == 1
        with pytest.raises(StopIteration):  # Assert command list was emptied
            mocked_input()

    def test_mailroom_thanks_donor_id_invalid(
        self, mocker, mocked_print, inst_populated
    ):
        """Positive-Test-Cases"""
        # Setup
        inst = inst_populated

        command_list = [
            "1",  # thanks_menu
            "D10",  # thanks_menu enter donor_id that is invalid
            "0",  # quit thanks_menu
            "0",  # quit
        ]

        # Mock
        mocked_input = generate_mocked_input(command_list)
        mocked_input = mocker.patch.object(cli_main, "input", new=mocked_input)

        # Execute
        inst.run_menu()

        # Assert
        assert "unrecognized" in mocked_print.call_args[0][0].lower()
        assert mocked_print.call_count == 1
        with pytest.raises(StopIteration):  # Assert command list was emptied
            mocked_input()

    def test_mailroom_thanks_donor_list(self, mocker, mocked_print, inst_populated):
        """Positive-Test-Cases"""
        # Setup
        inst = inst_populated

        command_list = [
            "1",  # thanks_menu
            "1",  # thanks_menu list
            "0",  # quit thanks_menu
            "0",  # quit
        ]

        # Mock
        mocked_input = generate_mocked_input(command_list)
        mocked_input = mocker.patch.object(cli_main, "input", new=mocked_input)

        # Execute
        inst.run_menu()

        # Assert
        assert mocked_print.call_count == len(inst.record.donor_list)
        with pytest.raises(StopIteration):  # Assert command list was emptied
            mocked_input()

    def test_mailroom_add_donation_invalid(self, mocker, mocked_print, inst_populated):
        """Positive-Test-Cases"""
        # Setup
        inst = inst_populated

        command_list = [
            "1",  # thanks
            "foo",  # thanks_menu
            "not-money",  # amount_menu invalid-entry
            "0",  # quit amount_menu
            "0",  # quit thanks_menu
            "0",  # quit main_menu
        ]
        inst = cli_main.Cli()

        # Mock
        mocked_input = generate_mocked_input(command_list)
        mocked_input = mocker.patch.object(cli_main, "input", new=mocked_input)

        # Execute
        inst.run_menu()

        # Assert
        assert "unrecognized" in mocked_print.call_args[0][0].lower()
        with pytest.raises(StopIteration):  # Assert command list was emptied
            mocked_input()

    def test_mailroom_add_donation_help(self, mocker, mocked_print, inst_populated):
        """Positive-Test-Cases"""
        # Setup
        inst = inst_populated

        command_list = [
            "1",  # thanks
            "foo",  # thanks_menu
            "help",  # amount_menu invalid-entry
            "0",  # quit amount_menu
            "0",  # quit thanks_menu
            "0",  # quit
        ]
        inst = cli_main.Cli()

        # Mock
        mocked_input = generate_mocked_input(command_list)
        mocked_input = mocker.patch.object(cli_main, "input", new=mocked_input)

        # Execute
        inst.run_menu()

        # Assert
        assert "help" in mocked_print.call_args[0][0].lower()
        with pytest.raises(StopIteration):  # Assert command list was emptied
            mocked_input()


class Test_Mailroom_Report:
    """Tests the cli_main report menu"""

    def test_mailroom_report_empty(self, mocker, mocked_print):
        """Positive-Test-Cases"""
        # Setup
        inst = cli_main.Cli()
        report_general_rows = 5
        command_list = [
            "2",  # report
            "0",  # quit
        ]

        # Mock
        mocked_input = generate_mocked_input(command_list)
        mocked_input = mocker.patch.object(cli_main, "input", new=mocked_input)

        # Execute
        inst.run_menu()

        # Assert
        assert mocked_print.call_count == report_general_rows
        with pytest.raises(StopIteration):  # Assert command list was emptied
            mocked_input()

    def test_mailroom_report_populated(self, mocker, inst_populated, mocked_print):
        """Positive-Test-Cases"""
        # Setup
        inst = inst_populated
        non_empty_donors = count_empty_donors(inst)
        report_general_rows = 5
        report_donor_rows = non_empty_donors * 2
        command_list = [
            "2",  # report
            "0",  # quit
        ]

        # Mock
        mocked_input = generate_mocked_input(command_list)
        mocked_input = mocker.patch.object(cli_main, "input", new=mocked_input)

        # Execute
        inst.run_menu()

        # Assert
        assert mocked_print.call_count == report_general_rows + report_donor_rows
        with pytest.raises(StopIteration):  # Assert command list was emptied
            mocked_input()


class Test_Mailroom_Save_Emails:
    """Tests the cli_main.save_emails method"""

    def test_mailroom_save_emails_populated(self, mocker, mocked_print, inst_populated):
        """Positive-Test-Cases"""
        # Setup
        inst = inst_populated
        command_list = [
            "3",  # save_emails
            "0",  # quit
        ]
        non_empty_donors = count_empty_donors(inst)

        # Mock
        mocked_input = generate_mocked_input(command_list)
        mocked_input = mocker.patch.object(cli_main, "input", new=mocked_input)
        mocked_open = mocker.patch.object(cli_main.donor_models, "open")

        # Execute
        inst.run_menu()

        # Assert
        assert mocked_print.call_count == 1
        assert mocked_open.call_count == non_empty_donors
        with pytest.raises(StopIteration):  # Assert command list was emptied
            mocked_input()


class Test_Mailroom_Donor_Misc:
    """Tests the Donor interactions not covered by CLI interaction above"""

    def test_mailroom_donor_negative_unrecognized(self, mocked_print, inst_populated):
        """Positive-Test-Cases"""
        # Setup
        inst = inst_populated
        donor_0 = inst.record.donor_list[0]
        initial_amount = inst.record.donors[donor_0].total_given
        inst._thank_you_donor = donor_0  # pylint: disable=protected-access

        # Execute
        inst.amount_menu_input("-42")
        final_amount = inst.record.donors[donor_0].total_given

        assert mocked_print.call_count == 1
        assert "Unrecognized" in mocked_print.call_args[0][0]
        assert initial_amount == final_amount

    def test_mailroom_donor_no_donor_name(self, inst_populated):
        """Positive-Test-Cases"""
        # Setup
        inst = inst_populated

        # Execute/Assert
        with pytest.raises(ValueError):
            inst.add_donor()
