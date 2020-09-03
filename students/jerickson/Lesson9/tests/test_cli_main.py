"""Unit Tests for mailroom.cli_main module

Test Cases:
    Positive: Case that runs without errors
    Negative: Case that raises unhandled errors
"""
# pylint: disable=invalid-name
# pylint: disable=no-self-use
# pylint: disable=redefined-outer-name
# pylint: disable=too-few-public-methods

import regex
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


@pytest.fixture
def mocked_print(mocker):
    """Mocked version of print to simulate user interaction."""
    return mocker.patch.object(cli_main, "print")


class Test_Cli_Main_Cli_Init:
    """Tests the mailroom.cli_main.Cli.__init__ method."""

    def test_cli_main_cli_init(self):
        """Positive-Test-Cases"""
        # Setup
        inst = cli_main.Cli()

        # Assert
        assert inst.record
        assert inst.main_menu_model
        assert inst.main_menu_prompt


class Test_Cli_Main_Cli_Define_Menus:
    """Tests the mailroom.cli_main.Cli._define_menus method."""

    def test_cli_main_cli_define_menus(self):
        """Positive-Test-Cases"""
        # Setup
        inst = cli_main.Cli()

        # Execute/Assert
        menu_attributes = [
            "main_menu_model",
            "main_menu_prompt",
            "name_menu_model",
            "name_menu_prompt",
            "amount_menu_model",
            "amount_menu_prompt",
        ]
        for menu_attribute in menu_attributes:
            first = getattr(inst, menu_attribute)  # Capture original value
            setattr(inst, menu_attribute, 1)  # Change value
            second = getattr(inst, menu_attribute)  # Capture second value
            inst._define_menus()  # Reset values. pylint: disable=protected-access
            third = getattr(inst, menu_attribute)  # Capture third value

            assert second != first  # Assert changed
            assert third == first  # Assert reset


class Test_Cli_Main_Cli_Report:
    """
    Tests the cli_main.Cli.report method.

    __builtins__.print() is mocked to simulate user-interaction
    inst.record.compose_report() is mocked to provide an isolated state for each test
    """

    @pytest.mark.parametrize(
        "report_len",
        [
            pytest.param(0, id="empty_report"),
            pytest.param(1, id="one_line"),
            pytest.param(10, id="ten_lines"),
        ],
    )
    def test_cli_main_cli_report(self, mocker, report_len):
        """Positive-Test-Cases"""
        # Setup
        report_list = range(1, report_len + 1)
        inst = cli_main.Cli()

        # Mock
        mocked_print = mocker.patch.object(cli_main, "print")
        mocker.patch.object(inst.record, "compose_report", return_value=report_list)

        # Execute
        inst.report()

        # Assert
        for i, line in enumerate(report_list):  # Report printed in order
            assert mocked_print.call_args_list[i].args[0] == line


class Test_Cli_Main_cli_Quit_Menu:
    """Tests the cli_main.Cli.quit_menu method."""

    def test_cli_main_cli_quit_menu(self):
        "The quite quiet quit test."
        # Setup
        inst = cli_main.Cli()

        # Assert
        assert inst.quit_menu() == "quit"


class Test_Cli_Main_cli_Unrecognized_Command:
    """Tests the cli_main.Cli.unrecognized_command method."""

    @pytest.mark.parametrize(
        "command, goal",
        [
            pytest.param("", "“”", id="empty"),
            pytest.param("spam", "“spam”", id="non-empty"),
        ],
    )
    def test_cli_main_cli_unrecognized_command(
        self, mocker, mocked_print, command, goal
    ):
        """Positive-Test-Cases"""

        # Setup
        inst = cli_main.Cli()

        # Mock
        mocked_print = mocker.patch.object(cli_main, "print")

        # Execute
        inst.unrecognized_command(command)

        # Assert
        assert mocked_print.call_count == 1
        printed_item = mocked_print.call_args[0][0]
        assert goal in printed_item


class Test_Cli_Main_Cli_Run_Menu:
    """
    Tests the cli_main_cli.run_menu method.

    __builtins__.input() is mocked to simulate user-interaction
    __builtins__.print() is mocked to simulate user-interaction
    """

    @pytest.fixture
    def command_dispatch(self, mocker):
        """Dispatch Menu Fixture"""
        called_once = mocker.MagicMock()
        called_twice = mocker.MagicMock()
        called_quit = mocker.MagicMock(return_value="quit")
        command_dispatch = {
            "1": called_once,
            "2": called_twice,
            "0": called_quit,
        }
        return command_dispatch

    def test_cli_main_cli_run_menu_custom(self, mocker, command_dispatch):
        """Positive-Test-Cases, custom menu and prompt"""
        # Setup
        command_list = ["1", "2", "2", "0"]
        inst = cli_main.Cli()

        # Mock
        mocked_input = generate_mocked_input(command_list)
        mocked_input = mocker.patch.object(cli_main, "input", new=mocked_input)

        # Execute
        inst.run_menu(menu_prompt="spam", menu_model=command_dispatch)

        # Assert
        for command in set(command_list):  # Every command called correct # of times
            assert command_dispatch[command].call_count == command_list.count(command)
        with pytest.raises(StopIteration):  # Assert command list was emptied
            mocked_input()

    def test_cli_main_cli_run_menu_invalid_input_unrecognized(
        self, mocker, command_dispatch,
    ):
        """Positive-Test-Cases, invalid input: unrecognized command"""
        # Setup
        inst = cli_main.Cli()
        command_list = ["spam", "0"]

        # Mock
        mocked_input = generate_mocked_input(command_list)
        mocked_input = mocker.patch.object(cli_main, "input", new=mocked_input)
        inst.unrecognized_command = mocker.MagicMock()

        # Execute
        inst.run_menu(menu_prompt="spam", menu_model=command_dispatch)

        # Assert
        assert command_dispatch["0"].call_count == 1  # quit called once
        assert inst.unrecognized_command.call_count == 1
        assert inst.unrecognized_command.call_args[0][0] == command_list[0]
        with pytest.raises(StopIteration):  # Assert command list was emptied
            mocked_input()

    def test_cli_main_cli_run_menu_invalid_input_empty(self, mocker, command_dispatch):
        """
        Positive-Test-Cases, invalid input: empty command

        Empty command (user just pressed enter) re-prompts, doesn't call menu_key_error
        """
        # Setup
        inst = cli_main.Cli()
        command_list = ["", "0"]

        # Mock
        mocked_input = generate_mocked_input(command_list)
        mocked_input = mocker.patch.object(cli_main, "input", new=mocked_input)
        inst.unrecognized_command = mocker.MagicMock()

        # Execute
        inst.run_menu(menu_prompt="spam", menu_model=command_dispatch)

        # Assert
        assert command_dispatch["0"].call_count == 1  # quit called once
        assert inst.unrecognized_command.call_count == 0
        with pytest.raises(StopIteration):  # Assert command list was emptied
            mocked_input()

    def test_cli_main_cli_run_menu_main_menu(self, mocker, command_dispatch):
        """Positive-Test-Cases, use main_menu attributes first reassigning them."""

        # Setup
        command_list = ["0"]
        inst = cli_main.Cli()
        inst.main_menu_model = command_dispatch
        inst.main_menu_prompt = "spam"

        # Mock
        mocked_input = generate_mocked_input(command_list)
        mocked_input = mocker.patch.object(cli_main, "input", new=mocked_input)

        # Execute
        inst.run_menu()  # No args passed to use main_menu_x

        # Assert
        assert command_dispatch["0"].call_count == 1  # quit called once
        with pytest.raises(StopIteration):  # Assert command list was emptied
            mocked_input()

    @pytest.mark.parametrize(
        "queue_input",
        [
            pytest.param(["0"], id="run_zero"),
            pytest.param(["2", "2", "0"], id="run_2_twice"),
            pytest.param("0", id="run_zero_string"),
        ],
    )
    def test_cli_main_cli_run_menu_queue(self, mocker, command_dispatch, queue_input):
        """
        Positive-Test-Cases, menu can return a queue of callables.

        Overrides command "1" to return a queue of commands to run next without
        requiring user input. Assert these commands are called the correct number
        of times without having to put them into the command_list that gets put into
        mocked_input to simulate user entry.
        """

        # Setup
        command_list = ["1"]
        inst = cli_main.Cli()

        # Mock
        command_dispatch["1"] = mocker.MagicMock(return_value=queue_input)

        mocked_input = generate_mocked_input(command_list)
        mocked_input = mocker.patch.object(cli_main, "input", new=mocked_input)

        # Execute
        inst.run_menu(menu_prompt="spam", menu_model=command_dispatch)

        # Assert
        assert command_dispatch["1"].call_count == 1
        assert command_dispatch["2"].call_count == queue_input.count("2")
        assert command_dispatch["0"].call_count == 1
        with pytest.raises(StopIteration):  # Assert command list was emptied
            mocked_input()

    def test_cli_main_cli_run_menu_key_error_default(self, mocker, command_dispatch):
        """Positive-Test-Cases, custom menu and prompt"""
        # Setup
        unrecognized_command = "spam"
        command_list = [unrecognized_command]
        inst = cli_main.Cli()

        # Mock
        mocked_input = generate_mocked_input(command_list)
        mocked_input = mocker.patch.object(cli_main, "input", new=mocked_input)
        inst.unrecognized_command = mocker.MagicMock(return_value="quit")

        # Execute
        inst.menu_prompt = "spam"
        inst.menu_model = command_dispatch
        inst.run_menu()

        # Assert
        assert inst.unrecognized_command.call_count == 1
        assert inst.unrecognized_command.call_args[0][0] == unrecognized_command
        with pytest.raises(StopIteration):  # Assert command list was emptied
            mocked_input()

    def test_cli_main_cli_run_menu_key_error_argument(self, mocker, command_dispatch):
        """Positive-Test-Cases, custom menu and prompt"""
        # Setup
        unrecognized_command = "spam"
        command_list = [unrecognized_command]
        inst = cli_main.Cli()

        # Mock
        mocked_input = generate_mocked_input(command_list)
        mocked_input = mocker.patch.object(cli_main, "input", new=mocked_input)
        mocked_menu_key_error = mocker.MagicMock(return_value="quit")

        # Execute
        inst.run_menu(
            menu_prompt="spam",
            menu_model=command_dispatch,
            menu_key_error=mocked_menu_key_error,
        )

        # Assert
        assert mocked_menu_key_error.call_count == 1
        assert mocked_menu_key_error.call_args[0][0] == unrecognized_command
        with pytest.raises(StopIteration):  # Assert command list was emptied
            mocked_input()

    @pytest.mark.parametrize(
        "queue_input",
        [
            pytest.param("", id="empty_queue"),
            pytest.param(["2", "2"], id="run_2_twice"),
            pytest.param("2", id="run_2_string"),
        ],
    )
    def test_cli_main_cli_run_menu_key_error_queue(
        self, mocker, command_dispatch, queue_input
    ):
        """
        Positive-Test-Cases, menu_key_error can return a queue of callables.

        Overrides the unrecognized command to send a queue of commands to be run by the
        parent menu.
        """

        # Setup
        command_list = ["1", "eggs", "0"]
        inst = cli_main.Cli()

        # Mock
        mocked_input = generate_mocked_input(command_list)
        mocked_input = mocker.patch.object(cli_main, "input", new=mocked_input)
        mocked_menu_key_error = mocker.MagicMock(return_value=queue_input)

        # Execute
        inst.run_menu(
            menu_prompt="spam",
            menu_model=command_dispatch,
            menu_key_error=mocked_menu_key_error,
        )

        # Assert
        assert command_dispatch["1"].call_count == 1
        assert "2" not in command_list  # Assert test-case is setup properly
        assert command_dispatch["2"].call_count == queue_input.count("2")
        assert command_dispatch["0"].call_count == 1
        with pytest.raises(StopIteration):  # Assert command list was emptied
            mocked_input()


class Test_Cli_Main_Cli_Donor_List:
    """
    Tests the cli_main.Cli.donor_list method.

    __builtins__.print() is mocked to simulate user-interaction
    inst.record.donor_list is mocked to provide an isolated state for each test
    """

    @pytest.mark.parametrize(
        "donor_list",
        [
            pytest.param(["aaa", "bbb", "ccc"], id="non-empty"),
            pytest.param([], id="empty"),
        ],
    )
    def test_cli_main_cli_donor_list(self, mocker, donor_list):
        """Positive-Test-Cases"""
        # Setup
        inst = cli_main.Cli()

        # Mock
        inst.record = mocker.MagicMock()
        inst.record.donor_list = donor_list
        mocked_print = mocker.patch.object(cli_main, "print")

        # Execute
        inst.donor_list()

        # Assert
        for i, donor in enumerate(donor_list):  # List printed in order
            printed_item = mocked_print.call_args_list[i].args[0]
            assert f"{i:d}" in printed_item
            assert donor in printed_item
        if not donor_list:  # Empty List prints special message
            printed_item = mocked_print.call_args[0][0]
            assert "No donors" in printed_item


class Test_Cli_Main_Cli_Thank_You:
    """Tests the cli_main.Cli.thank_you method."""

    def test_cli_main_cli_thank_you_no_print(self, mocker, mocked_print):
        """Positive-Test-Cases, no print thank-you"""
        # Setup
        inst = cli_main.Cli()

        # Mock
        mocked_print = mocker.patch.object(cli_main, "print")
        inst.run_menu = mocker.MagicMock()

        # Execute
        inst.thank_you()

        # Assert
        assert inst.run_menu.call_count == 2
        assert mocked_print.call_count == 0

    def test_cli_main_cli_thank_you_print(self, mocker, mocked_print):
        """Positive-Test-Cases, print thank-you"""
        # Setup
        donor_name = "spam"
        message = "eggs"
        inst = cli_main.Cli()

        # Mock
        inst._thank_you_donor = donor_name  # pylint: disable=protected-access
        inst.record = mocker.MagicMock()
        mocked_donor = mocker.MagicMock()
        mocked_donor.thank_you_latest = mocker.MagicMock(return_value=message)
        inst.record.donors = {donor_name: mocked_donor}

        mocked_print = mocker.patch.object(cli_main, "print")
        inst.run_menu = mocker.MagicMock()

        # Execute
        inst.thank_you()

        # Assert
        assert inst.run_menu.call_count == 2
        assert mocked_print.call_count == 1
        assert mocked_print.call_args[0][0] == message


class Test_Cli_Main_Cli_Name_Menu_Input:
    """Tests the cli_main.Cli.name_menu_input method."""

    # pylint: disable=protected-access

    @pytest.mark.parametrize(
        "result_goal",
        [pytest.param("quit", id="existing"), pytest.param("new_donor", id="new"),],
    )
    def test_cli_main_cli_name_menu_input_name(self, mocker, result_goal):
        """Positive-Test-Cases, name entered"""
        # Setup
        command = "spam"
        inst = cli_main.Cli()

        # Mock
        inst.find_donor = mocker.MagicMock(return_value=(command, result_goal))

        # Execute
        first_value = inst._thank_you_donor
        result = inst.name_menu_input(command)
        second_value = inst._thank_you_donor

        # Assert
        assert first_value == ""
        assert second_value == command
        assert result == result_goal

    @pytest.mark.parametrize(
        "command",
        [
            pytest.param("D0", id="zero"),
            pytest.param("D1", id="positive"),
            pytest.param("D-1", id="negative"),
        ],
    )
    def test_cli_main_cli_name_menu_input_valid_donor_id(self, mocker, command):
        """Positive-Test-Cases, valid donor_id"""
        # Setup
        donor_list = ["spam", "eggs"]
        inst = cli_main.Cli()
        donor_id = abs(int(command[1:]))

        # Mock
        inst.record = mocker.MagicMock()
        inst.record.donor_list = donor_list

        # Execute
        first_value = inst._thank_you_donor
        result = inst.name_menu_input(command)
        second_value = inst._thank_you_donor

        # Assert
        assert result == "quit"
        assert first_value == ""
        assert second_value == donor_list[donor_id]

    def test_cli_main_cli_name_menu_input_invalid_donor_id(self, mocker):
        """Positive-Test-Cases, invalid donor_id"""
        # Setup
        command = "D3"
        donor_list = ["spam", "eggs"]
        inst = cli_main.Cli()

        # Mock
        inst.record = mocker.MagicMock()
        inst.record.donor_list = donor_list
        inst.unrecognized_command = mocker.MagicMock()

        # Execute
        result = inst.name_menu_input(command)

        # Assert
        assert inst._thank_you_donor == ""
        assert result == ""
        assert inst.unrecognized_command.call_count == 1
        assert inst.unrecognized_command.call_args[0][0] == command


class Test_Cli_Main_Cli_Find_Donor:
    """Tests the cli_main.Cli.find_donor method."""

    @pytest.mark.parametrize(
        "donor_entered",
        [
            pytest.param("spam", id="existing1"),
            pytest.param("eggs", id="existing2"),
            pytest.param("cheese", id="new"),
        ],
    )
    def test_cli_main_cli_find_donor(self, mocker, donor_entered):
        """Positive-Test-Cases"""
        donor_list = ["spam", "eggs"]
        inst = cli_main.Cli()

        # Mock
        inst.record = mocker.MagicMock()
        inst.record.donor_list = donor_list

        # Execute
        donor_name, result = inst.find_donor(donor_entered)

        # Assert
        assert donor_name == donor_entered
        if donor_entered in donor_list:
            assert result == "quit"
        else:
            assert result == "new_donor"


class Test_Cli_Main_Cli_Add_Donor:
    """Tests the cli_main.Cli.add_donor method."""

    def test_cli_main_Cli_add_donor(self, mocker):
        """Positive-Test-Cases"""
        donor_entered = "spam"
        inst = cli_main.Cli()

        # Mock
        inst.record = mocker.MagicMock()
        inst.record.donor_list = []
        inst._thank_you_donor = donor_entered  # pylint: disable=protected-access

        def mocked_add_donor(name):
            """Mocks the record.add_donor method"""
            inst.record.donor_list.append(name)

        inst.record.add_donor = mocked_add_donor

        # Execute
        inst.add_donor()

        # Assert
        assert donor_entered in inst.record.donor_list


class Test_Cli_Main_Cli_Amount_Menu_Input:
    """Tests the cli_main.Cli.amount_menu_input method."""

    @pytest.mark.parametrize(
        "donation_entries",
        [
            pytest.param(["42", "42"], id="multiple_int"),
            pytest.param(["42.42", "42.42"], id="multiple_float"),
            pytest.param(["42", "42.42"], id="multiple_mixed"),
            pytest.param(["42,420", "4,242.42"], id="multiple_commas"),
            pytest.param(["$42", "42.42€"], id="currency"),
        ],
    )
    def test_cli_main_cli_amount_menu_input(self, mocker, donation_entries):
        """Positive-Test-Cases"""
        # pylint: disable=protected-access
        # Setup
        donor_entered = "spam"
        inst = cli_main.Cli()
        donations_float = []
        result_list = []

        # Mock
        mocked_donor = mocker.MagicMock()
        mocked_donor.donations = []
        inst.record = mocker.MagicMock()
        inst.record.donors = {donor_entered: mocked_donor}
        inst._thank_you_donor = donor_entered

        def mocked_add_donation(amount):
            """Mocks the record.add_donor method"""
            mocked_donor.donations.append(amount)

        mocked_donor.add_donation = mocked_add_donation

        # Execute
        for donation_entry in donation_entries:
            result = inst.amount_menu_input(donation_entry)
            result_list.append(result)

            # Strip currency symbols and commas from amount
            donation_entry = regex.sub("\\p{Currency_Symbol}", "", donation_entry)
            donation_entry = regex.sub(",", "", donation_entry)
            donations_float.append(float(donation_entry))

        # Assert
        assert inst.record.donors[donor_entered].donations == donations_float
        assert all(res == "quit" for res in result_list)

    def test_cli_main_cli_amount_menu_input_unrecognized(self, mocker):
        """Positive-Test-Cases"""
        # Setup
        command = "spam"
        inst = cli_main.Cli()

        # Mock
        inst.record = mocker.MagicMock()
        inst.unrecognized_command = mocker.MagicMock()

        # Execute
        result = inst.amount_menu_input(command)

        # Assert
        assert result == ""
        assert inst.unrecognized_command.call_count == 1
        assert inst.unrecognized_command.call_args[0][0] == command

    @pytest.mark.parametrize(
        "command",
        [
            pytest.param("-42.42", id="negative_float"),
            pytest.param("-42", id="negative_int"),
            pytest.param("eggs", id="letters"),
            pytest.param("D0D", id="close_to_id"),
        ],
    )
    def test_cli_main_cli_amount_menu_input_invalid(self, mocker, command):
        """Positive-Test-Cases"""
        # Setup
        donor_entered = "spam"
        inst = cli_main.Cli()

        # Mock
        def mocked_add_donation(amount):
            if amount <= 0:
                raise ValueError

        mocked_donor = mocker.MagicMock()
        mocked_donor.donations = []
        mocked_donor.add_donation = mocked_add_donation
        inst.record = mocker.MagicMock()
        inst.record.donors = {donor_entered: mocked_donor}
        inst._thank_you_donor = donor_entered  # pylint: disable=protected-access

        inst.unrecognized_command = mocker.MagicMock()

        # Execute
        result = inst.amount_menu_input(command)

        # Assert
        assert result == ""
        assert inst.unrecognized_command.call_count == 1
        assert inst.unrecognized_command.call_args[0][0] == command


class Test_Cli_Main_Cli_Amount_Menu_Help:
    """Tests the cli_main.Cli.amount_menu_help method."""

    def test_cli_main_cli_amount_menu_help(self, mocker, mocked_print):
        """Positive-Test-Cases, no print thank-you"""
        # Setup
        inst = cli_main.Cli()

        # Mock
        mocked_print = mocker.patch.object(cli_main, "print")

        # Execute
        inst.amount_menu_help()

        # Assert
        assert mocked_print.call_count == 1
        assert "help" in mocked_print.call_args[0][0].lower()


class Test_Cli_Main_Cli_Save_Emails:
    """
    Tests the cli_main.Cli.save_emails method.

    __builtins__.print() is mocked to simulate user-interaction
    __builtins__.open() is mocked to simulate user-interaction and saving files
    inst.record.save_all_donor_emails() is mocked to provide an isolated state for each test
    """

    def test_cli_main_cli_save_emails(self, mocker):
        """Positive-Test-Cases"""
        # Setup
        inst = cli_main.Cli()

        # Mock
        inst.record = mocker.MagicMock()

        # Execute
        inst.save_all_donor_emails()

        # Assert
        assert inst.record.save_all_donor_emails.call_count == 1


class Test_Cli_Main_Main:
    """
    Tests the cli_main.main method.

    cli_main.main() is mocked to provide an isolated state for each test
    """

    def test_cli_main_main(self, mocker):
        """Positive-Test-Cases"""
        # Mock
        mocked_cli_instance = mocker.MagicMock()
        mocker.patch.object(cli_main, "Cli", return_value=mocked_cli_instance)

        # Execute
        cli_main.main()

        # Assert
        assert mocked_cli_instance.run_menu.call_count == 1
