"""Contains the Command Line Interface (CLI) for the mailroom package."""

from mailroom import donor_models  # pylint: disable=import-error


class Cli:
    """Command Line Interace to interact with donor_models"""

    def __init__(self):
        self.record = donor_models.Record()
        self._define_menus()  # Construct menu defaults
        self._thank_you_donor = ""

    def _define_menus(self):
        """
        Create the default menus of the CLI.

        Call using __init__(). Calling again resets attributes.
        """
        self.main_menu_model = {
            "1": self.thank_you,
            "2": self.report,
            "3": "save_all_donor_emails",
            "0": self.quit_menu,
        }

        self.main_menu_prompt = (
            "\nChoose: “1”: Send a Thank You, “2”: Create a Report"
            " “3”: Send Letters to Everyone or “0”: Quit ->: "
        )
        self.thank_you_menu_model = {
            "1": self.donor_list,
            "new_donor": "self.new_donor",
            "0": self.quit_menu,
        }

        self.thank_you_menu_prompt = (
            "\nChoose: “1”: Get list of prior donors, “0”: Quit, or "
            "enter a donor's full name ->: "
        )

    def report(self):
        """Print a report of the donation history."""
        for line in self.record.compose_report():
            print(line)

    def thank_you(self):
        """
        Enters the thank_you sub-menu.

        Gets user input of donor name and donation amount.
        """
        self.run_menu(
            menu_prompt=self.thank_you_menu_prompt,
            menu_model=self.thank_you_menu_model,
            menu_key_error=self.thank_you_input,
        )

    def donor_list(self):
        """
        Print list of all donors or No-Donor message.

        Prints the list of donors with D#, # is position in list of donor 1-indexed
        Prints a No-Donor message if there are no donors.
        """
        donors = self.record.donor_list
        if not donors:
            print("No donors, please create a new donor.")
            return
        for i, donor in enumerate(self.record.donor_list):
            print(f"    “D{i:d}”: {donor}")

    def find_donor(self, name_entered):
        """
        Attempts to find a donor based on the user input.

        Parameters
        ----------
        name_entered : str
            User input string to find a match of

        Returns
        -------
        name_found : str
            Donor name found
        result : str
            The string that helps the calling function dispatch the next behavior.
        """
        if name_entered in self.record.donor_list:
            name_found = name_entered
            result = "quit"
        else:
            name_found = name_entered
            result = "new_donor"
        return name_found, result

    @staticmethod
    def quit_menu():
        """Return the string "quit" to exit a menu-level"""
        return "quit"

    def thank_you_input(self, command):
        """
        Called when the thank-you-menu receives an unrecognized command.

        This happens when adding a new donor, using existing donor, donor id.
        Also happens when called with empty command

        Parameters
        ----------
        command : str
            The user-input command string to parse.
        """
        try:  # Check to see if input is a donor_id: "D#"
            donor_id = int(command[1:])
            donor_id -= 1  # Translate 1-index to 0-index
            self._thank_you_donor = self.record.donor_list[donor_id]
            return "quit"
        except IndexError:  # Unrecognized Donor ID
            self.unrecognized_command(command)
            self._thank_you_donor = ""
            return
        except ValueError:  # Not a donor_id, set as donor name
            self._thank_you_donor = command
            return "quit"

    @staticmethod
    def unrecognized_command(command):
        """Default behavior when a menu receives an unrecognized command."""
        print(f"Unrecognized Command: “{command}”")

    def run_menu(self, menu_prompt="", menu_model=None, menu_key_error=None):
        """
        Runs a CLI menu selection code with a prompt, and target functions.
        
        No args assumes it is being called as the main menu for the CLI:
        Default for menu_prompt, menu_model, menu_key_error will use the instance attributes
        of self.main_menu_prompt, self.main_menu_model, self.unrecognized_command.

        An unrecognized command creates a key_error which is dispatched to the
        menu_key_error argument or if None, then defaults to self.unrecognized_command.

        Gets a command from the user or a command_queue that was the result of a prior
        command's execution.

        Processes the result from the command or menu_key_error method:
            If it is 'quit' it exits the current menu-level
            If it is a list it will add them to the command_queue to be used automatically
            without prompting the user. This list must be a list of callables.

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
            menu_key_error = self.unrecognized_command

        command_queue = []
        while True:
            try:
                # Get Command
                if command_queue:
                    command = command_queue.pop(0)
                    result = command()
                else:
                    command = input(menu_prompt).lower()
                    # TODO check empty command here?
                    result = menu_model[command]()
            except KeyError:
                result = menu_key_error(command)
            # Process Result
            if result == "quit":  # checks if quit is returned
                break
            if isinstance(result, list):
                command_queue.extend(result)


def main():
    """Generates a CLI instance and runs the main_menu."""
    cli_instance = Cli()
    cli_instance.run_menu()
