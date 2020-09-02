"""Contains the Command Line Interface (CLI) for the mailroom package."""

from mailroom import donor_models  # pylint: disable=import-error


class Cli:
    """Command Line Interace to interact with donor_models"""

    def __init__(self):
        self.record = donor_models.Record()
        self._define_menus()  # Construct menu defaults

    def _define_menus(self):
        """
        Create the default menus of the CLI.

        Call using __init__(). Calling again resets attributes.
        """
        self.main_menu_model = {
            "1": "thank_you_cli",
            "2": self.report,
            "3": "save_all_donor_emails",
            "4": self.quit_menu,
            "q": self.quit_menu,
        }

        self.main_menu_prompt = (
            "\nChoose: “1”: Send a Thank You, “2”: Create a Report"
            " “3”: Send Letters to Everyone or “4”: Quit ->: "
        )

    def report(self):
        """Print a report of the donation history."""
        for line in self.record.compose_report():
            print(line)

    @staticmethod
    def quit_menu():
        """Return the string "quit" to exit a menu-level"""
        return "quit"

    def menu_key_error(self, command):
        """Default behavior when a menu receives an unrecognized command."""
        print(f"Unrecognized Command: “{command}”")

    def run_menu(self, menu_prompt="", menu_model=None, menu_key_error=None):
        """
        Runs a CLI menu selection code with a prompt, and target functions.

        Default for menu_prompt, menu_model, menu_key_error will use the instance attributes
        of self.main_menu_prompt and self.main_menu_model. Assumes it is being called as
        the main menu for the CLI.

        An unrecognized command creates a key_error which is dispatched to the
        menu_key_error argument or if None, then defaults to self.menu_key_error.

        Gets a command from the user or a command_queue that was the result of a prior
        command's execution.
        Processes the result from the command, if it is 'quit' it exits the current
        menu-level, if it is a list it will add them to the command_queue to be used
        automatically without prompting the user.

        Parameters
        ----------
        menu_prompt : str, optional
            Prompt that will be seen by user, by default ""
        menu_model : dict {str: callable}, optional
            Dictionary that selects target callable from user input str, by default None
        """
        if not menu_prompt:
            menu_prompt = self.main_menu_prompt
        if not menu_model:
            menu_model = self.main_menu_model
        if not menu_key_error:
            menu_key_error = self.menu_key_error

        command_queue = []
        while True:
            try:
                # Get Command
                if command_queue:
                    command = command_queue.pop(0)
                    result = command()
                else:
                    command = input(menu_prompt).lower()
                    result = menu_model[command]()

                # Process Result
                if result == "quit":  # checks if quit is returned
                    break
                if isinstance(result, list):
                    command_queue.extend(result)
            except KeyError:
                if menu_key_error(command) == "quit":
                    break


def main():
    """Generates a CLI instance and runs the main_menu."""
    cli_instance = Cli()
    cli_instance.run_menu()
