"""Contains the Command Line Interface (CLI) for the mailroom package."""
# pylint: disable=attribute-defined-outside-init

import regex
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
        self._thank_you_donor = ""

        self.main_menu_model = {
            "1": self.thank_you,
            "2": self.report,
            "3": self.save_all_donor_emails,
            "0": self.quit_menu,
            "quit": self.quit_menu,
        }

        self.main_menu_prompt = (
            "\nChoose: “1”: Send a Thank You, “2”: Create a Report"
            " “3”: Send Letters to Everyone, “0”: Quit ->: "
        )
        self.name_menu_model = {
            "1": self.donor_list,
            "new_donor": self.add_donor,
            "0": self.quit_menu,
            "quit": self.quit_menu,
        }

        self.name_menu_prompt = (
            "\nEnter donor's full name: (Or choose: “1”: List"
            " prior donors, “0”: Quit) ->: "
        )
        self.amount_menu_model = {
            "help": self.amount_menu_help,
            "0": self.quit_menu,
            "quit": self.quit_menu,
        }

        self.amount_menu_prompt = (
            "\nEnter how much was donated: (Or choose: “0”: Quit, “help”: Info) ->: "
        )

    def report(self):
        """Print a report of the donation history."""
        for line in self.record.compose_report():
            print(line)

    def save_all_donor_emails(self):
        """Save all donor thank-you-overall emails"""
        self.record.save_all_donor_emails()

    def thank_you(self):
        """
        Enters the thank_you sub-menu.

        Gets user input of donor name and donation amount.
        """
        self.run_menu(
            menu_prompt=self.name_menu_prompt,
            menu_model=self.name_menu_model,
            menu_key_error=self.name_menu_input,
        )
        self.run_menu(
            menu_prompt=self.amount_menu_prompt,
            menu_model=self.amount_menu_model,
            menu_key_error=self.amount_menu_input,
        )
        try:
            message = self.record.donors[self._thank_you_donor].thank_you_latest()
            print(message)
        except LookupError:  # Donation was not made
            pass

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
            Result message to send to menu dispatch
        """
        if name_entered in self.record.donor_list:
            name_found = name_entered
            result = "quit"
        else:
            name_found = name_entered
            result = "new_donor"
        return name_found, result

    def add_donor(self):
        """
        Adds a new donor to the donation record.

        Returns
        -------
        result : str
            Result message to send to menu dispatch
        """
        self.record.add_donor(self._thank_you_donor)
        print(f"Added donor “{self._thank_you_donor}”")
        result = "quit"
        return result

    @staticmethod
    def quit_menu():
        """Return the string "quit" to exit a menu-level"""
        return "quit"

    def name_menu_input(self, command):
        """
        Called when the thank-you-menu receives an unrecognized command.

        This happens when adding a new donor, using existing donor, donor id.

        Parameters
        ----------
        command : str
            The user-input command string to parse.

        Returns
        -------
        result : str
            Result message to send to menu dispatch
        """
        try:  # Check to see if input is a donor_id: "D#"
            donor_id = command.lower().replace("d", "", 1)
            donor_id = abs(int(donor_id))
            donor_name = self.record.donor_list[donor_id]
            print(f"Selected donor: “{donor_name}”")
            result = "quit"
        except IndexError:  # Unrecognized Donor ID
            self.unrecognized_command(command)
            donor_name = ""
            result = ""
        except ValueError:  # Not a donor_id, set as donor name
            donor_name, result = self.find_donor(command)
        self._thank_you_donor = donor_name
        return result

    def amount_menu_input(self, command):
        """
        Called when the new-donation-amount-menu receives an unrecognized command.

        This happens when adding an amount or other unrecognized command.

        Parameters
        ----------
        command : str
            The user-input command string to parse.
        """
        try:  # Try to add donation
            command = regex.sub("\\p{Currency_Symbol}", "", command)  # Strip symbols
            command = regex.sub(",", "", command)  # Strip commas
            amount = float(command)
            donor_data = self.record.donors[self._thank_you_donor]
            donor_data.add_donation(amount)
            print(f"Donor “{self._thank_you_donor}” donated: {amount:0.2f}")
            result = "quit"
        except ValueError:  # Unrecognized Command
            self.unrecognized_command(command)
            result = ""
        return result

    @staticmethod
    def amount_menu_help():
        """Display a message to the user to guide in entering in an amount."""
        print(
            "Help: Enter a number greater than 0. Commas and some currency symbols"
            " are ok to use."
        )

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

        If the user does not enter an input, they are reprompted.

        Processes the result from the command or menu_key_error method:
            If it is 'quit' it exits the current menu-level
            If it is a list it will add them to the command_queue to be used automatically
            without prompting the user. This list must be a list of strings.

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
                    command = command_queue.pop(0)  # Dequeue command
                else:
                    command = input(menu_prompt).lower()
                    if not command:  # Re-prompt if nothing entered
                        continue

                # Run Command
                result = menu_model[command]()

            except KeyError:  # Run command through menu_key_error
                result = menu_key_error(command)

            # Process Result
            if result == "quit":  # Exits the menu-level if 'quit' is result
                break
            if result:  # Any other non-empty response goes into the queue
                if isinstance(result, str):  # Turn strings into list to allow .extend()
                    result = [result]
                command_queue.extend(result)


def main():
    """Generates a CLI instance and runs the main_menu."""
    cli_instance = Cli()
    cli_instance.run_menu()
