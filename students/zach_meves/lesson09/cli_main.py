"""
Main command line interface for the Mailroom OO program.
"""

from donor_models import Donor, DonorCollection
import os

# For assignment purposes only, have an initial donor list so user doesn't have
# to manually add several donors
INITIAL_DONORS = (Donor("Hans Zimmer", [1200, 20, 340]),
                  Donor("Bill Boeing", [30, 75]),
                  Donor("Homer Simpson", 1),
                  Donor("Fred Flintstone", 100),
                  Donor("Will Smith", [50, 125]))

_quit_responses = ('q', 'quit')  # Responses to interpret as a "quit" command
_thankyou_responses = ('1', 'thank you', 'thankyou', 'send a thank you')
_report_responses = ('2', 'report', 'create a report')
_all_thank_responses = ('3', 'letters', 'send letters to all donors')


def _get_input(prompt, options, allow_new=False, reprompt_options=None):
    """For internal use only.

    Get user input and match the lowercase version to a list of options. Optionally restrict that
    input must be one of a few possible responses.

    Parameters
    ----------
    prompt : str
        Prompt to display
    options : sequence
        Sequence of valid response options
    allow_new : bool, optional
        If ``True``, allow responses that are not in the list of options
        If ``False``, re-prompt if a non-option given
    reprompt_options : sequence, optional
        Subset of given ``options`` that will be displayed to prompt user to enter a valid response,
        if not all entries of ``options`` should be shown.

    Returns
    -------
    str
        Input, matched to case of provided option if applicable"""

    _lwr_opts = [x.lower() for x in options]
    if reprompt_options is None:
        reprompt_options = options

    while True:
        _resp = input(prompt).strip()

        # Check that input is one of the options
        try:
            i = _lwr_opts.index(_resp.lower())
            return options[i]
        except ValueError:
            if not allow_new:
                print(f'Response must be one of the following: {", ".join(reprompt_options)}')

        if allow_new and _resp:  # If have a non-empty string
            return _resp


def _request_donation() -> float:
    """Requests a donation amount.

    Returns
    -------
    float or None
        Donation amount, or None if 'quit' requested
    """

    amt = _get_input("Enter a donation amount:\n> ", _quit_responses, allow_new=True)
    if amt in _quit_responses:
        return None
    else:
        try:
            return float(amt)
        except ValueError:
            print(f'{amt} is not a number!')
            return _request_donation()


def send_thank_you(donors: DonorCollection) -> None:
    """Send a thank you note to a Donor.

    Parameters
    ----------
    donors : DonorCollection
        DonorCollection to operate on
    """

    # Prompt user for a name
    while True:
        name = _get_input("Enter a full name (or 'list' to list the donors):\n> ",
                          tuple(donors.get_donor_names()) + ('list',) + _quit_responses,
                          allow_new=True)
        if name == 'list':
            print(donors.get_donor_names())
        else:  # Won't prompt again unless 'list' is entered
            # If quit, return to calling function
            if name in _quit_responses:
                return
            break  # Break out of while loop if a name entered

    # Request a donation amount
    amt = _request_donation()
    if amt is None:  # Return to calling function if quit
        return

    # Add donation to donor
    try:
        donors.add_donation(name, amt)
    except (ValueError, TypeError):
        print("Donations must be positive numbers\n")
    else:
        # Print thank you note
        print(f"\n{donors[name].get_thankyou()}\n")


def report_action(donors: DonorCollection) -> None:
    """Create and print a report of donations.

    Parameters
    ----------
    donors : DonorCollection
        DonorCollection to operate on
    """

    print('\n')
    print(donors.get_report())
    print('\n')


def all_thanks(donors: DonorCollection) -> None:
    """Write letters to all donors in this directory.

    Parameters
    ----------
    donors : DonorCollection
        DonorCollection to operate on
    """

    donors.write_thank_yous(directory='.')
    print('All letters written to current directory.\n')


def _exit_(*args, **kwargs):
    exit(0)


if __name__ == "__main__":
    """Main Mailroom Executable"""

    dc = DonorCollection(*INITIAL_DONORS)

    # Build up dispatch dictionary
    actions = {}
    for r in _thankyou_responses:
        actions[r] = send_thank_you
    for r in _report_responses:
        actions[r] = report_action
    for r in _all_thank_responses:
        actions[r] = all_thanks
    for r in _quit_responses:
        actions[r] = _exit_

    # Print intro
    print("\nWelcome to the Mailroom Program!\n")
    print("To quit the program, or return to the previous menu at any time, enter 'q' or 'quit'.\n")
    while True:
        response = _get_input("Select from the following options:\n"
                              " 1 - Send a Thank You\n"
                              " 2 - Create a Report\n"
                              " 3 - Send Letters to All Donors\n"
                              " q - Quit\n"
                              "> ",
                              _thankyou_responses + _report_responses + _all_thank_responses +
                              _quit_responses, allow_new=False,
                              reprompt_options=('1', '2', '3', 'q'))

        # Perform action based on response
        try:
            actions[response](dc)
        except KeyError:
            raise RuntimeError("Internal error occurred")
