#!/usr/bin/env python3
import sys

donors = [
    ['Carmelo Anthony', 1, 50],
    ['Damien Lillard', 100.50, 99, 10000],
    ['CJ McCollum', 24000, 70, 100, 5, 300],
    ['Hassan Whiteside', 10000],
    ['Terry Stotts', 500, 500, 100, 100, 100],
]

welcome_prompt = "\n".join(("Welcome to the Local Charity Mail Room System",
                  "Please choose from the following options:",
                  "1 - Send a Thank You",
                  "2 - Create a Report",
                  "3 - Quit",
                  ">>> "))


def main():
    while True:
        response = input(welcome_prompt)
        if response == "1":
            send_thank_you()
        elif response == "2":
            create_report()
        elif response == "3":
            exit_program()
        else:
            print("Not a valid option!")


def list_donors():
    newLine = '\n'
    print(f"{newLine.join(x[0] for x in donors)}")


def send_thank_you():
        response = input("Please enter a full name: ")
        if response.lower() == "list":
            list_donors()
            send_thank_you()
        else:
            amount = input("Please enter the donation amount: ")
            add_donation(find_donor(response), amount)


def find_donor(name):
    """
    Returns a list containing the name of the donor
    and a history of their donations.

    If the name cannot be found, crates a new list
    for the new donor
    """
    for d in donors:
        if name in d:
            return d
    new_donor = [name, ]
    donors.append(new_donor)
    return new_donor


def add_donation(donor, amt):
    """
    Records a donation and prints a thank you email.
    Expects a list which contains a donor and a list of amounts.
    """
    amt = float(amt)
    donor.append(amt)
    print(f"Thank you {donor[0]} for you generous donation of ${amt:.2f}")


def sort_key(donor_summary):
    return donor_summary[1]


def create_report():
    report = []
    for d in donors:
        total_amount = sum(d[1:])
        number_of_gifts = len(d) - 1
        average_gift = round(total_amount / number_of_gifts, 2)
        donor_summary = [d[0], total_amount, number_of_gifts, average_gift]
        report.append(donor_summary)
    print_report(sorted(report, key=sort_key, reverse=True))


def print_report(report):
    print("Donor Name" + (' ' * 16) + ("| Total Given | Num Gifts | Avergage Gift"))
    print("-" * 68)
    row = "{name:<26s} ${total:=12.2f}  {num:10d} ${avg:14.2f}".format
    for donor in report:
        print(row(name=donor[0], total=donor[1], num=donor[2], avg=donor[3]))


def exit_program():
    print("You made a difference today.  Have a good one!")
    sys.exit()


if __name__ == "__main__":
    main()
