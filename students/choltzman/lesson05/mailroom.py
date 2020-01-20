#!/usr/bin/env python3
from textwrap import dedent
from collections import defaultdict

# putting variables outside a function like this is ugly, but oh well
donors = defaultdict(list, {
    'William Gates, III': [1234.56, 12345.67],
    'Mark Zuckerberg': [9506.31, 8288.91, 1357.02],
    'Jeff Bezos': [1234567.89],
    'Paul Allen': [1, 2, 3, 4, 5, 6, 7, 8, 9]
})


def main():
    """Prompt user for a choice of actions."""
    # intro text to use for prompt
    intro = dedent("""\

    -----------------------
    Choose an action:
        1: Send a Thank You
        2: Send a Thank You (Bulk)
        3: Create a Report
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
    """Send a thank you to a given person."""
    print("Input a donor's full name, or enter 'list' to see all donors.")
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
            donors[name].append(gift)
            # print thank you email
            emailstr = dedent("""\
            From: "Nameless Charity" <sender@example.com>
            To: "{}" <receiver@example.com>
            Subject: Thank you for your donation!

            Thank you for your generous donation of ${:,.2f} dollars!
            """.format(name, gift))
            print("\n" + emailstr)
            input("Press Enter to continue...")
            break


def send_thanks_bulk():
    """Send a thank you to all donors."""
    for name, gifts in donors.items():
        # format nice email message
        emailstr = dedent("""\
        From: "Nameless Charity" <sender@example.com>
        To: "{}" <receiver@example.com>
        Subject: Thank you for your donations!

        You've donated a total of ${:,.2f} dollars to our cause! Thank you!
        """.format(name, sum(gifts)))
        # convert donor name to a safe file name
        filename = "".join(c for c in name if c.isalnum()) + ".txt"
        # write message to file
        print(f"Creating file for {name}...")
        try:
            with open(filename, 'w') as f:
                f.write(emailstr)
        except OSError:
            print(f"ERROR: Unable to open file '{filename}'!")


def create_report():
    """Output a list of donors sorted by total donation amount."""
    # print header
    print("{:^25} | {:^15} | {:^9} | {:^15}".format(
        "Name", "Total Given", "Num Gifts", "Average Gift"))
    print("{:->73}".format(""))

    # sort list of donors by total donations made
    donors_sorted = sorted(donors.items(),
                           key=lambda i: sum(i[1]), reverse=True)

    # loop through list and print
    for name, gifts in donors_sorted:
        total = sum(gifts)
        num = len(gifts)
        avg = sum(gifts) / len(gifts)
        print("{:<25} | {:>15.2f} | {:>9} | {:>15.2f}".format(
            name, total, num, avg))


if __name__ == "__main__":
    main()
