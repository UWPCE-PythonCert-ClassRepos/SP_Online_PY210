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
        assert inst.main_menu
        assert inst.thanks_menu
        assert inst.amount_menu


class Test_Cli_Main_Cli_Define_Menus:
    """Tests the mailroom.cli_main.Cli._define_menus method."""

    def test_cli_main_cli_define_menus(self):
        """Positive-Test-Cases"""
        # Setup
        inst = cli_main.Cli()

        # Execute/Assert
        menu_attributes = [
            "main_menu",
            "thanks_menu",
            "amount_menu",
        ]
        for menu_attribute in menu_attributes:
            first = getattr(inst, menu_attribute)  # Capture original value
            setattr(inst, menu_attribute, 1)  # Change value
            second = getattr(inst, menu_attribute)  # Capture second value
            inst._define_menus()  # Reset values. pylint: disable=protected-access
            third = getattr(inst, menu_attribute)  # Capture third value

            assert isinstance(first, dict)
            assert isinstance(second, int)
            assert isinstance(third, dict)


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
    def test_cli_main_cli_report(self, mocker, mocked_print, report_len):
        """Positive-Test-Cases"""
        # Setup
        report_list = range(1, report_len + 1)
        inst = cli_main.Cli()

        # Mock
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
        called_key_error = mocker.MagicMock()
        command_dispatch = {
            "1": called_once,
            "2": called_twice,
            "0": called_quit,
            "_prompt": "spam",
            "_key_error": called_key_error,
        }
        return command_dispatch

    def test_cli_main_cli_run_menu_custom(self, mocker, command_dispatch):
        """Positive-Test-Cases, custom menu and prompt"""
        # Setup
        command_list = ["1", "2", "2", "0"]
        inst = cli_main.Cli()

        # Mock
        mocked_input = mocker.patch.object(cli_main, "input", side_effect=command_list)

        # Execute
        inst.run_menu(menu=command_dispatch)

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
        mocked_input = mocker.patch.object(cli_main, "input", side_effect=command_list)
        command_dispatch["_key_error"] = mocker.MagicMock()

        # Execute
        inst.run_menu(menu=command_dispatch)

        # Assert
        assert command_dispatch["0"].call_count == 1  # quit called once
        assert command_dispatch["_key_error"].call_count == 1
        assert command_dispatch["_key_error"].call_args[0][0] == command_list[0]
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
        mocked_input = mocker.patch.object(cli_main, "input", side_effect=command_list)
        inst.unrecognized_command = mocker.MagicMock()

        # Execute
        inst.run_menu(menu=command_dispatch)

        # Assert
        assert command_dispatch["0"].call_count == 1  # quit called once
        assert inst.unrecognized_command.call_count == 0
        with pytest.raises(StopIteration):  # Assert command list was emptied
            mocked_input()

    def test_cli_main_cli_run_menu_main_menu(self, mocker,command_dispatch):
        """Positive-Test-Cases, use main_menu attributes first reassigning them."""

        # Setup
        command_list = ["0"]
        inst = cli_main.Cli()
        inst.main_menu = command_dispatch

        # Mock
        mocked_input = mocker.patch.object(cli_main, "input", side_effect=command_list)

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

        mocked_input = mocker.patch.object(cli_main, "input", side_effect=command_list)

        # Execute
        inst.run_menu(menu=command_dispatch)

        # Assert
        assert command_dispatch["1"].call_count == 1
        assert command_dispatch["2"].call_count == queue_input.count("2")
        assert command_dispatch["0"].call_count == 1
        with pytest.raises(StopIteration):  # Assert command list was emptied
            mocked_input()

    def test_cli_main_cli_run_menu_key_error_main_menu(self, mocker):
        """Positive-Test-Cases, custom menu and prompt"""
        # Setup
        unrecognized_command = "spam"
        command_list = [unrecognized_command]
        inst = cli_main.Cli()

        # Mock
        mocked_input = mocker.patch.object(cli_main, "input", side_effect=command_list)
        inst.unrecognized_command = mocker.MagicMock(return_value="quit")
        inst._define_menus()  # redefine menu reference to mocked command pylint: disable=protected-access

        # Execute
        inst.run_menu()

        # Assert
        assert inst.unrecognized_command.call_count == 1
        assert inst.unrecognized_command.call_args[0][0] == unrecognized_command
        with pytest.raises(StopIteration):  # Assert command list was emptied
            mocked_input()

    def test_cli_main_cli_run_menu_key_error_quit(self, mocker, command_dispatch):
        """Positive-Test-Cases, custom menu and prompt"""
        # Setup
        unrecognized_command = "spam"
        command_list = [unrecognized_command]
        inst = cli_main.Cli()

        # Mock
        mocked_input = mocker.patch.object(cli_main, "input", side_effect=command_list)
        command_dispatch["_key_error"] = mocker.MagicMock(return_value="quit")

        # Execute
        inst.run_menu(menu=command_dispatch)

        # Assert
        assert command_dispatch["_key_error"].call_count == 1
        assert command_dispatch["_key_error"].call_args[0][0] == unrecognized_command
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
        mocked_input = mocker.patch.object(cli_main, "input", side_effect=command_list)
        command_dispatch["_key_error"] = mocker.MagicMock(return_value=queue_input)

        # Execute
        inst.run_menu(menu=command_dispatch)

        # Assert
        assert command_dispatch["1"].call_count == 1
        assert "2" not in command_list  # Assert test-case is setup properly
        assert command_dispatch["2"].call_count == queue_input.count("2")
        assert command_dispatch["0"].call_count == 1
        with pytest.raises(StopIteration):  # Assert command list was emptied
            mocked_input()

    @pytest.mark.parametrize(
        "queue_input",
        [
            pytest.param(["quit"], id="quit_queue_empty"),
            pytest.param(["quit", "spam"], id="quit_command"),
            pytest.param(["quit", "quit"], id="quit_quit"),
        ],
    )
    def test_cli_main_cli_run_menu_quit_queue(
        self, mocker, command_dispatch, queue_input
    ):
        """
        Positive-Test-Cases, menu can return a queue of callables after quit-command.

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

        mocked_input = mocker.patch.object(cli_main, "input", side_effect=command_list)

        # Execute
        returned_queue = inst.run_menu(menu=command_dispatch)

        # Assert
        assert command_dispatch["1"].call_count == 1
        assert returned_queue == queue_input[1:]
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
    def test_cli_main_cli_donor_list(self, mocker, mocked_print, donor_list):
        """Positive-Test-Cases"""
        # Setup
        inst = cli_main.Cli()

        # Mock
        inst.record = mocker.MagicMock()
        inst.record.donor_list = donor_list

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


class Test_Cli_Main_Cli_Thanks_Menu_Input:
    """Tests the cli_main.Cli.thanks_menu_input method."""

    # pylint: disable=protected-access

    @pytest.mark.parametrize(
        "result_goal",
        [pytest.param("quit", id="existing"), pytest.param("new_donor", id="new")],
    )
    def test_cli_main_cli_thanks_menu_input_name(self, mocker, result_goal):
        """Positive-Test-Cases, name entered"""
        # Setup
        command = "spam"
        inst = cli_main.Cli()

        # Mock
        inst.find_donor = mocker.MagicMock(return_value=(command, result_goal))

        # Execute
        first_value = inst._thank_you_donor
        result = inst.thanks_menu_input(command)
        second_value = inst._thank_you_donor

        # Assert
        assert first_value == ""
        assert second_value == command
        assert result == result_goal

    @pytest.mark.parametrize(
        "command", [pytest.param("D0", id="zero"), pytest.param("D1", id="positive"),],
    )
    def test_cli_main_cli_thanks_menu_input_valid_donor_id(self, mocker, command):
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
        result = inst.thanks_menu_input(command)
        second_value = inst._thank_you_donor

        # Assert
        assert result == "amount_menu"
        assert first_value == ""
        assert second_value == donor_list[donor_id]

    @pytest.mark.parametrize(
        "command, result_goal, name_goal",
        [
            pytest.param("D3", "", "", id="exceeds_donors"),
            pytest.param("D1.0", "new_donor", "D1.0", id="float"),
            pytest.param("D-1", "new_donor", "D-1", id="negative"),
        ],
    )
    def test_cli_main_cli_thanks_menu_input_invalid_donor_id(
        self, mocker, command, result_goal, name_goal
    ):
        """Positive-Test-Cases, invalid donor_id, things a new donor is being added"""
        # TODO should it recognize a donor_id was attempted?
        # Setup
        donor_list = ["spam", "eggs"]
        inst = cli_main.Cli()

        # Mock
        inst.record = mocker.MagicMock()
        inst.record.donor_list = donor_list
        inst.unrecognized_command = mocker.MagicMock()

        # Execute
        result = inst.thanks_menu_input(command)

        # Assert
        assert inst._thank_you_donor == name_goal
        assert result == result_goal


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
            assert result == "amount_menu"
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
        assert all(("quit" in result_item) for result_item in result_list)

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

    def test_cli_main_cli_save_emails(self, mocker, mocked_print):
        """Positive-Test-Cases"""
        # Setup
        inst = cli_main.Cli()

        # Mock
        inst.record = mocker.MagicMock()

        # Execute
        inst.save_emails()

        # Assert
        assert inst.record.save_all_donor_emails.call_count == 1
        assert mocked_print.call_count == 1
        assert "saved" in mocked_print.call_args[0][0]


class Test_Cli_Main_Cli_Print_Thanks:
    """
    Tests the cli_main.Cli.report method.

    __builtins__.print() is mocked to simulate user-interaction
    inst.record.compose_report() is mocked to provide an isolated state for each test
    """

    def test_cli_main_cli_print_thanks(self, mocker, mocked_print):
        """Positive-Test-Cases, print thank-you"""
        # Setup
        donor_name = "spam"
        message = "eggs"
        inst = cli_main.Cli()

        # Mock
        inst.record = mocker.MagicMock()
        mocked_donor = mocker.MagicMock()
        mocked_donor.thank_you_latest = mocker.MagicMock(return_value=message)
        inst.record.donors = {donor_name: mocked_donor}
        inst._thank_you_donor = donor_name

        # Execute
        inst.print_thanks()

        # Assert
        assert mocked_print.call_count == 1
        assert mocked_print.call_args[0][0] == message


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
