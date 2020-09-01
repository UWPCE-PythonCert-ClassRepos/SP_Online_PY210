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


class Test_Cli_Main_Cli_Define_Main_Menu:
    """Tests the mailroom.cli_main.Cli.define_main_menu method."""

    def test_cli_main_cli_define_main_menu(self):
        """Positive-Test-Cases"""
        # Setup
        new_menu = {"spam": "eggs"}
        new_prompt = "spam"
        inst = cli_main.Cli()
        inst2 = cli_main.Cli()
        inst2.define_main_menu(new_menu_model=new_menu, new_menu_prompt=new_prompt)

        # Assert
        assert len(inst.main_menu_model) > 1  # Menu is defaulted to a standard model
        assert len(inst.main_menu_prompt) > 1  # Prompt is defaulted to a standard model
        assert inst2.main_menu_model == new_menu  # Menu is updated to new model
        assert inst2.main_menu_prompt == new_prompt  # Prompt updated to new model


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

    def test_cli_main_cli_run_menu(self, mocker):
        """Positive-Test-Cases"""
        # Setup
        command_list = ["spam", "1", "2", "2", "3"]
        input_list = (n for n in command_list)
        inst = cli_main.Cli()

        # Mock
        def mocked_input(*_):
            return next(input_list)

        called_once = mocker.MagicMock()
        called_twice = mocker.MagicMock()
        called_quit = mocker.MagicMock(return_value="quit")
        command_dispatch = {
            "1": called_once,
            "2": called_twice,
            "3": called_quit,
        }

        mocked_print = mocker.patch.object(cli_main, "print")
        mocker.patch.object(cli_main, "input", new=mocked_input)

        # Execute
        inst.run_menu(menu_model=command_dispatch)

        # Assert
        assert called_once.call_count == 1
        assert called_twice.call_count == 2
        assert called_quit.call_count == 1
        for argument_string in [
            "Unrecognized",
            command_list[0],
        ]:  # Assert contents of error message printed
            assert argument_string in mocked_print.call_args.args[0]
        with pytest.raises(StopIteration):  # Assert command list was emptied
            mocked_input()
