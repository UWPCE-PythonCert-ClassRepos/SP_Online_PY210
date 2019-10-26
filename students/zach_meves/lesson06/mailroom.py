#!/usr/bin/env python3

"""
mailroom.py

Zach Meves
Python 210
Lesson 06 Assignment

Mailroom Project Part 4 (Adding Tests)
"""

# Initialize donors
_donors = {"Hans Zimmer": [1200, 20, 340],
           "Bill Boeing": [30, 75],
           "Homer Simpson": [1],
           "Fred Flintstone": [100],
           "Will Smith": [50, 125]}
# Dictionary containing donor information. First element of each tuple is name, second is list
# of donation amounts

_quit_responses = ('q', 'quit')  # Responses to interpret as a "quit" command

_thank_string = "Dear {name},\n" + \
                "    Thank you very much for your recent donation of $ {last_donation:.2f}. We truly \n" + \
                "appreciate your contribution.\n\n    Your total tax-deductible donation amount is now " + \
                "$ {total_donation:.2f}.\n\n" + \
                "Sincerely,\n" + \
                "    Zach"


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


def _request_donation():
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


def _compose_thank_you(name):
    """Compose a thank you note to a donor with the given name.

    For use by :py:func:`add_donation`, which is in turn used by
    :py:func:`send_thank_you`.

    Parameters
    ----------
    name : str
        Full name of donor, must be one of the existing donors

    Returns
    -------
    str
        Thank you note
    """

    try:
        last_donation = _donors[name][-1]
        total_donation = sum(_donors[name])
        return _thank_string.format(name=name, last_donation=last_donation, total_donation=total_donation)

    except KeyError:
        raise NameError(f"No donor with name {name} is present in data")
        # print(f"No donor with name {name} is present in data")


def _print_donors():
    """Prints list of donors."""
    print('Current donors: ' + ', '.join(_get_donor_names()))


def _get_donor_names():
    """Returns list of donor names."""
    return list(_donors.keys())


def add_donation(name: str, amount: float) -> str:
    """Get a donation amount for a donor name and modify the stored donation data.
    Also return the donation letter for use by :py:func:`send_thank_you`.

    Parameters
    ----------
    name : str
        Name of donor to get donation for
    amount : float
        Donation amount

    Returns
    -------
    str
        Donor thank you letter based on this most recent donation."""

    _donors.setdefault(name, []).append(amount)
    return _compose_thank_you(name)


def send_thank_you():
    """Send a thank you note to a donor."""

    # Prompt user for a name
    name = ''
    while True:
        name = _get_input("Enter a full name (or 'list' to list the donors):\n> ",
                          tuple(_get_donor_names()) + ('list',) + _quit_responses, allow_new=True)
        if name == 'list':
            _print_donors()
        else:  # Won't prompt again unless 'list' is entered
            # If quit, return to calling function
            if name in _quit_responses:
                return
            break  # Break out of while loop if a name entered

    # Request a donation amount
    amt = _request_donation()
    if amt is None:  # Return to calling function if quit
        return

    # Find requested donor
    thank_you_note = add_donation(name, amt)

    # Print thank you note
    print('\n')
    print(thank_you_note)
    print('\n')


def create_report():
    """Create a report of donations. Prints report and returns the value.

    Returns
    -------
    str
        Report"""

    # Sort by total donation amount
    names = _get_donor_names()
    names.sort(key=lambda x: -sum(_donors[x]))

    # Generate the report
    _str_ = ["Donor Name                | Total Given | Num Gifts | Average Gift\n" +
             "------------------------------------------------------------------"]
    for donor in names:
        sm = sum(_donors[donor])
        l = len(_donors[donor])
        _str_.append(f"{donor:<25}   $ {sm:>9.2f}   {l:>9d}   $ {sm / l:>10.2f}")

    report = '\n'.join(_str_)
    print(report)
    return report


def all_thanks():
    """Write letters to all donors as individual files."""

    for name in _donors:
        fname = f"{name.replace(' ', '_')}_thanks.txt"
        with open(fname, 'w') as f:
            f.write(_compose_thank_you(name))
    print('All letters written to this directory\n')


def _report_action():
    """For internal use only. Prints report surrounded by new lines.

    Returns
    -------
    result of :py:func:`create_report`
    """

    print('')
    rep = create_report()
    print('')
    return rep


if __name__ == '__main__':
    """Main Mailroom Executable."""

    _thankyou_responses = ('1', 'thank you', 'thankyou', 'send a thank you')
    _report_responses = ('2', 'report', 'create a report')
    _all_thank_responses = ('3', 'letters', 'send letters to all donors')

    # Build up dispatch dictionary
    actions = {}
    for r in _thankyou_responses:
        actions[r] = send_thank_you
    for r in _report_responses:
        actions[r] = _report_action
    for r in _all_thank_responses:
        actions[r] = all_thanks
    for r in _quit_responses:
        actions[r] = exit

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
            actions[response]()
        except KeyError:
            raise RuntimeError("Internal error occurred")



