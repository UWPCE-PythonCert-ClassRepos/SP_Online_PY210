"""Unit Tests for mailroom.cli_main module

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
            "thank_you_menu_model",
            "thank_you_menu_prompt",
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


class Test_Cli_Main_cli_quit_Menu:
    """Tests the cli_main.Cli.quit_menu function."""

    def test_cli_main_cli_quit_menu(self):
        "The quite quiet quit test."
        # Setup
        inst = cli_main.Cli()

        # Assert
        assert inst.quit_menu() == "quit"


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

    @pytest.mark.parametrize(
        "command_list",
        [
            pytest.param(["", "0"], id="empty_quit"),
            pytest.param(["spam", "0"], id="unrecognized_quit"),
        ],
    )
    def test_cli_main_cli_run_menu_invalid_inputs(
        self, mocker, command_dispatch, mocked_print, command_list
    ):
        """Positive-Test-Cases, invalid inputs"""
        # Setup
        inst = cli_main.Cli()

        # Mock
        mocked_input = generate_mocked_input(command_list)
        mocked_input = mocker.patch.object(cli_main, "input", new=mocked_input)

        # Execute
        inst.run_menu(menu_prompt="spam", menu_model=command_dispatch)

        # Assert
        assert command_dispatch["0"].call_count == 1  # quit called once
        # Assert contents of error message printed
        for argument_string in ["Unrecognized", command_list[0]]:
            assert argument_string in mocked_print.call_args.args[0]
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
        "queue_len",
        [
            pytest.param(0, id="run_zero"),
            pytest.param(1, id="run_once"),
            pytest.param(2, id="run_twice"),
        ],
    )
    def test_cli_main_cli_run_menu_queue(self, mocker, command_dispatch, queue_len):
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

        command_2 = command_dispatch["2"]
        command_quit = command_dispatch["0"]
        queue_input = [command_2] * queue_len + [command_quit]
        command_dispatch["1"] = mocker.MagicMock(return_value=queue_input)

        # Mock
        mocked_input = generate_mocked_input(command_list)
        mocked_input = mocker.patch.object(cli_main, "input", new=mocked_input)

        # Execute
        inst.run_menu(menu_prompt="spam", menu_model=command_dispatch)

        # Assert
        assert command_dispatch["1"].call_count == 1
        assert command_dispatch["2"].call_count == queue_len
        assert command_dispatch["0"].call_count == 1
        with pytest.raises(StopIteration):  # Assert command list was emptied
            mocked_input()

    @pytest.mark.parametrize(
        "arg_default",
        [pytest.param("arg", id="argument"), pytest.param("default", id="default"),],
    )
    def test_cli_main_cli_run_menu_key_error(
        self, mocker, command_dispatch, arg_default
    ):
        """Positive-Test-Cases, custom menu and prompt"""
        # Setup
        unrecognized_command = "spam"
        command_list = [unrecognized_command]
        inst = cli_main.Cli()

        # Mock
        mocked_menu_key_error = mocker.MagicMock(return_value="quit")
        mocked_input = generate_mocked_input(command_list)
        mocked_input = mocker.patch.object(cli_main, "input", new=mocked_input)
        mocked_menu_key_error = mocker.MagicMock(return_value="quit")

        # Execute
        if arg_default == "arg":  # Run as argument
            inst.run_menu(
                menu_prompt="spam",
                menu_model=command_dispatch,
                menu_key_error=mocked_menu_key_error,
            )
        elif arg_default == "default":  # Run as default
            inst.menu_key_error = mocked_menu_key_error
            inst.run_menu(
                menu_prompt="spam", menu_model=command_dispatch,
            )

        # Assert
        assert mocked_menu_key_error.call_count == 1
        assert mocked_menu_key_error.call_args[0][0] == unrecognized_command
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


class Test_Cli_Main_Main:
    """
    Tests the cli_main.main function.

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
