"""Contains the Command Line Interface (CLI) for the mailroom package."""

from mailroom import donor_models


class Cli:
    """Command Line Interace to interact with donor_models"""

    def __init__(self):
        self.record = donor_models.Record()
        self.define_main_menu()

    def define_main_menu(self, new_menu_prompt="", new_menu_model=""):
        """
        Creates the main_dispatch model for the main menu of the CLI.

        Parameters
        ----------
        new_menu_prompt : str, optional
            New Prompt String, by default None creates standard prompt
        new_menu_model : dict, optional
            New Menu Model, by default Nonecreates standard menu

        """
        if not new_menu_model:
            new_menu_model = {
                "1": "thank_you_cli",
                "2": "report_cli",
                "3": "save_all_donor_emails",
                "4": "quit_menu",
                "quit": "quit_menu",
            }

        if not new_menu_prompt:
            new_menu_prompt = (
                "\nChoose: “1”: Send a Thank You, “2”: Create a Report"
                " “3”: Send Letters to Everyone or “4”: Quit ->: "
            )

        self.main_menu_model = new_menu_model
        self.main_menu_prompt = new_menu_prompt

    def report(self):
        """Print a report of the donation history."""
        for line in self.record.compose_report():
            print(line)

    @staticmethod
    def quit_menu():
        """Return the string "quit" to exit a menu-level"""
        return "quit"

    def run_menu(self, menu_prompt="", menu_model=None):
        # TODO DOCSTRING
        if not menu_prompt:
            menu_prompt = self.main_menu_prompt
        if not menu_model:
            menu_model = self.main_menu_model

        while True:
            command = input(menu_prompt).lower()
            try:
                if (
                    menu_model[command]() == "quit"
                ):  # Runs command and gets checks if quit is returned
                    break
            except KeyError:
                print(f"Unrecognized Command: {command}")
