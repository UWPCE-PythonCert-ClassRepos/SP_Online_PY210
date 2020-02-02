#!/usr/bin/env python3
from textwrap import dedent
from donor_models import DonorCollection


def main():
    """Prompt user for a choice of actions to take."""
    # donors collection
    donors = DonorCollection()

    # intro text to use for prompt
    intro = dedent("""\

    -----------------------
    Choose an action:
        1: Send a Thank You
        2: Send a Thank You (Bulk)
        3: Print Report
        q: Quit
    -----------------------""")

    # prompt for input
    # NOTE: no case here because only some of the functions called want
    # arguments
    while True:
        print(intro)
        inp = input("Select: ")
        if inp == "1":
            send_thanks(donors)
        elif inp == "2":
            send_thanks_bulk(donors)
        elif inp == "3":
            print_report(donors)
        elif inp == "q":
            print("Exiting.")
            exit(0)
        else:
            print(f"Unknown input: '{inp}'")


def send_thanks(donors):
    """Add a donation from a donor to the collection."""
    # prompt for name
    while True:
        name = input("Name: ")
        if name.lower() == "list":
            for dname in donors.names:
                print(dname)
            print("")
        else:
            break

    # prompt for gift amount
    while True:
        try:
            gift = float(input("Gift amount: "))
            break
        except ValueError:
            print("Input must be a number!")

    # add donor to collection (this is safe due to the method being idempotent)
    donors.add_donor(name)

    # get donor object from collection and add gift
    donor = donors.get_donor(name)
    donor.add_donation(gift)

    # print thank you letter
    print(_format_email(
        name,
        "Thank you for your donation!",
        f"Thank you for your donation of ${gift:,.2f}!"))


def send_thanks_bulk(donors):
    """Send a thank you letter to all donors."""
    for name in donors.names:
        # fetch donor info
        donor = donors.get_donor(name)

        # format email string
        emailstr = _format_email(
            name,
            "Thank you for your donations!",
            f"You've donated a total of ${donor.donations_total:,.2f}!" +
            " Thank you!")

        # convert donor name to a safe filename
        filename = "".join(c for c in name if c.isalnum()) + ".txt"

        # write message to file
        try:
            with open(filename, 'w') as f:
                f.write(emailstr)
        except OSError:
            print(f"ERROR: Unable to write to file '{filename}'!")


def print_report(donors):
    """Output a list of donors sorted by total donation amount."""
    # print header
    print(f"{'Name':^25} | {'Total Given':^15} | {'Num Gifts':^9} | " +
          f"{'Average Gift':^15}")
    print(f"{'':->73}")

    # loop through sorted donors and print
    for name in donors.names_sorted:
        donor = donors.get_donor(name)
        print(f"{donor.name:<25} | {donor.donations_total:>15.2f} | "
              f"{donor.donations_count:>9} | {donor.donations_avg:>15.2f}")


def _format_email(to, subj, body):
    """Format a thank you email string."""
    emailstr = dedent(f"""\
    From: "Nameless Charity" <sender@example.com>
    To: "{to}" <receiver@example.com>
    Subject: {subj}

    {body}
    """)
    return emailstr


if __name__ == "__main__":
    main()
