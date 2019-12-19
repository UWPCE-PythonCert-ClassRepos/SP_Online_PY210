#!/usr/bin/env python3
from textwrap import dedent

# putting variables outside a function like this is ugly, but oh well
donors = [
        {
            "name": "William Gates, III",
            "gifts": [1234.56, 12345.67]
        },
        {
            "name": "Mark Zuckerberg",
            "gifts": [9506.31, 8288.91, 1357.02]
        },
        {
            "name": "Jeff Bezos",
            "gifts": [1234567.89]
        },
        {
            "name": "Paul Allen",
            "gifts": [1, 2, 3, 4, 5, 6, 7, 8, 9]
        }
]


def main():
    """Prompt user for a choice of actions."""
    # intro text to use for prompt
    intro = dedent("""\

    -----------------------
    Choose an action:
        1: Send a Thank You
        2: Create a Report
        q: Quit
    -----------------------""")

    while True:
        print(intro)
        inp = input("Select: ")
        print("")
        if inp == "1":
            send_thanks()
        elif inp == "2":
            create_report()
        elif inp == "q":
            print("Exiting.")
            exit(0)
        else:
            print("Unknown input: '{}'".format(inp))
            input("Press Enter to continue...")


def send_thanks():
    """Send a thank you to a given person."""
    print("Input a donor's full name, or enter 'list' to see all donors.")
    while True:
        name = input("Name: ")
        if name == "list":
            for donor in donors:
                print(donor["name"])
            print("")
        else:
            gift = float(input("Gift amount: "))
            for donor in donors:
                if donor["name"] == name:
                    donor["gifts"].append(gift)
                    break
            else:
                donors.append({"name": name, "gifts": [gift]})
            emailstr = dedent("""\
            From: "Nameless Charity" <sender@example.com>
            To: "{}" <receiver@example.com>
            Subject: Thank you for your donation!

            Thank you for your generous donation of ${:,.2f} dollars!
            """.format(name, gift))
            print("\n" + emailstr)
            input("Press Enter to continue...")
            break


def create_report():
    """Output a list of donors sorted by total donation amount."""
    print("{:^25} | {:^15} | {:^9} | {:^15}".format(
        "Name", "Total Given", "Num Gifts", "Average Gift"))
    print("{:->73}".format(""))
    for donor in donors:
        # parse values
        total = sum(donor["gifts"])
        num = len(donor["gifts"])
        avg = sum(donor["gifts"]) / len(donor["gifts"])
        # print the thing
        print("{:<25} | {:>15.2f} | {:>9} | {:>15.2f}".format(
            donor["name"], total, num, avg))


if __name__ == "__main__":
    main()
