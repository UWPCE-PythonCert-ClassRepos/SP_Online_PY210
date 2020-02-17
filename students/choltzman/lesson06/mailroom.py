#!/usr/bin/env python3
from textwrap import dedent
from collections import defaultdict


donors = defaultdict(list, {
    'William Gates, III': [1234.56, 12345.67],
    'Mark Zuckerberg': [9506.31, 8288.91, 1357.02],
    'Jeff Bezos': [1234567.89],
    'Paul Allen': [1, 2, 3, 4, 5, 6, 7, 8, 9]
})


def main():
    """Prompt user for a choice of actions to take."""
    # intro text to use for prompt
    intro = dedent("""\

    -----------------------
    Choose an action:
        1: Send a Thank You
        2: Send a Thank You (Bulk)
        3: Create Report
        q: Quit
    -----------------------""")
    # dict for prompt choices
    inp_dict = {
                    '1': send_thanks,
                    '2': send_thanks_bulk,
                    '3': create_report,
                    'q': exit
               }

    # prompt for menu
    while True:
        print(intro)
        inp = input("Select: ")
        out = inp_dict.get(inp)
        if out:
            out()
        else:
            print(f"\nUnknown input: {inp}")
            input("Press Enter to continue...")


def send_thanks():
    """Add a donation and send a thank you letter."""
    while True:
        name = input("Name: ")
        if name.lower() == "list":
            for donor in donors.keys():
                print(donor)
            print("")
        else:
            # get gift amount and add to dict
            while True:
                try:
                    gift = float(input("Gift amount: "))
                    break
                except ValueError:
                    print("Input must be a number!")
            _add_donation(name, gift)
            # send a thank you letter
            print(_format_email(
                name,
                "Thank you for your donation!",
                f"Thank you for your donation of ${gift:,.2f} dollars!"))
            break


def send_thanks_bulk():
    """Send a thank you letter to all donors."""
    for name, gifts in donors.items():
        # format email string
        emailstr = _format_email(
            name,
            "Thank you for your donations!",
            f"You've donated a total of ${sum(gifts):,.2f} to our cause!" +
            " Thank you!")
        # write email string to file for later sending
        print(f"Creating file for {name}...")
        _write_file(name, emailstr)


def create_report():
    """Output a list of donors sorted by total donation amount."""
    # print header
    print(f"{'Name':^25} | {'Total Given':^15} | {'Num Gifts':^9} | " +
          f"{'Average Gift':^15}")
    print(f"{'':->73}")

    # sort list of donors by total donations
    donors_sorted = _sort_donors()

    # loop through list and print
    for name, gifts in donors_sorted:
        print(_format_report_row(name, gifts))


def _add_donation(name, num):
    """Add a donation to the donors dict."""
    donors[name].append(num)


def _format_email(to, subj, body):
    """Format a thank you email string."""
    emailstr = dedent(f"""\
    From: "Nameless Charity" <sender@example.com>
    To: "{to}" <receiver@example.com>
    Subject: {subj}

    {body}
    """)
    return emailstr


def _write_file(name, emailstr):
    """Write an email file to the current directory."""
    # convert donor name to a safe file name
    filename = "".join(c for c in name if c.isalnum()) + ".txt"

    # write message to file
    try:
        with open(filename, 'w') as f:
            f.write(emailstr)
    except OSError:
        print(f"ERROR: Unable to write to file '{filename}'!")


def _sort_donors():
    """Return a list of donors sorted by total donation amount."""
    return sorted(donors.items(),
                  key=lambda i: sum(i[1]), reverse=True)


def _format_report_row(name, gifts):
    """Format a row in the donation report."""
    return f"{name:<25} | {sum(gifts):>15.2f} | {len(gifts):>9} | " \
           f"{(sum(gifts) / len(gifts)):>15.2f}"


if __name__ == "__main__":
    main()
