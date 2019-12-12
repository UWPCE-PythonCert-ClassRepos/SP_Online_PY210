#!/usr/bin/env python3

import os
import sys

"""
Steve Morehouse
Lesson 06
"""

donor_db = {"William Gates, III": [653772.32, 12.17],
            "Jeff Bezos": [877.33],
            "Paul Allen": [663.23, 43.87, 1.32],
            "Mark Zuckerberg": [1663.23, 4300.87, 10432.0]
            }

prompt = "\n".join(("Welcome to the Mailroom!",
          "Please choose from below options:",
          "1 - Send a Thank You",
          "2 - Create Report",
          "3 - Send letters to all",
          "4 - Exit",
          ">>> "))


"""
list all donors
return: list of names
"""
def list_donors (donor_db):
    list = []
    for i in donor_db.keys():
        list.append(i)
    return list

"""
add a new donor
return: none
"""
def add_donor (new_donor_name, donor_db):
    donor_db.update({new_donor_name: []})

"""
add a donation amount to a new donor
return: none
"""
def add_donation (donor_name, new_donation, donor_db):
    donor_db[donor_name].append (new_donation)

"""
If the user (you) selects “Send a Thank You” option, prompt for a Full Name.
If the user types list show them a list of the donor names and re-prompt.
If the user types a name not in the list, add that name to the data structure and use it.
If the user types a name in the list, use it.
Once a name has been selected, prompt for a donation amount.
Convert the amount into a number; it is OK at this point for the program to crash if
someone types a bogus amount.
Add that amount to the donation history of the selected user.
Finally, use string formatting to compose an email thanking the donor for their generous donation.
Print the email to the terminal and return to the original prompt.
It is fine (for now) for the program not to store the names of the new donors that had been added,
in other words, to forget new donors once the script quits running.
"""

def send_a_thank_you ():
    while True:
        name = input("Type 'list' to see a list of names or enter a name: ")
        # now redirect to feature functions based on the user selection
        if name == "list":
            donor_list = list_donors(donor_db)
            [print(donor) for donor in donor_list]

        elif donor_db.get(name) == None:
            add_donor (name)
            break

        else:
            break

    # enter donation amount
    donation = float(input("Enter a donation amount: "))
    add_donation (name, donation)

    # write email
    msg = f"\n{name},\n\nThank you for your donation of ${donation}.\n"
    print(msg)

"""
If the user (you) selected “Create a Report,” print a list of your donors, sorted by total
historical donation amount.  Include Donor Name, total donated, number of donations, and
average donation amount as values in each row. You do not need to print out all of each
donor’s donations, just the summary info.  Using string formatting, format the output
rows as nicely as possible. The end result should be tabular (values in each column
should align with those above and below).
After printing this report, return to the original prompt.
At any point, the user should be able to quit their current task and return to the original prompt.
From the original prompt, the user should be able to quit the script cleanly.
Your report should look something like this:
Donor Name               | Total Given | Num Gifts | Average Gift
"""

def get_donor_summary():
    donor_summary = []
    for donor in donor_db.items():
        name = donor[0]
        total_donations = sum(donor[1])
        count_donations = len(donor[1])
        average_donation = total_donations / count_donations
        donor_summary.append([name, total_donations, count_donations, average_donation])
    return donor_summary

"""
get_max_lengths
"""
def get_max_lengths(seq, header):

    name_len = len(header[0])
    total_len = len(header[1])
    count_len = len(header[2])
    avg_len = len(header[3])

    for item in seq:
        total = f"${item[1]:.02f}"
        count = str(item[2])
        avg = f"${item[3]:.02f}"

        name_len = len(item[0]) if len(item[0]) > name_len else name_len
        total_len = len(total) if len(total) > total_len else total_len
        count_len = len(count) if len(count) > count_len else count_len
        avg_len = len(avg) if len(avg) > avg_len else avg_len

    return [name_len, total_len, count_len, avg_len]

def sort_key(item):
    return item[1]


"""
Return a formatted string that will fit in the donor summary table.
"""
def format_line(item, lengths):
    total = f"{item[1]:.02f}"
    avg = f"{item[3]:.02f}"
    return f"{item[0]:<{lengths[0]}}  ${total:>{lengths[1]}}   {item[2]:>{lengths[2]}}  ${avg:>{lengths[3]}}"


def create_report ():
    pad = 2
    table = []
    donor_summary = get_donor_summary()
    header = ["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
    lengths = get_max_lengths(donor_summary, header)

    sep_strings = [("-" * (lengths[0] + pad)), ("-" * (lengths[1] + pad)), ("-" * (lengths[2] + pad)), ("-" * (lengths[3] + pad))]
    sep_line = "+".join(sep_strings)

    for item in sorted(donor_summary, key=sort_key, reverse=True):
        table.append(format_line(item, lengths))

    # Header
    table.insert(0, f"\n{header[0]:<{lengths[0]}} | {header[1]:>{lengths[1]}} | {header[2]:>{lengths[2]}}  | {header[3]:>{lengths[3]}} ")
    table.insert(1, "-" * (len(sep_line) ) )

    print("\n".join(table) + "\n")


"""
Compose the letter to the each donor and write to file
"""
def print_report ():
    cur_dir = os.getcwd()

    for donor in donor_db.items():

        name = donor[0]
        total_donations = sum(donor[1])
        count_donations = len(donor[1])

        letter = "Thank you {0:s} for your donations totaling ${1:.2f}.".format (name, total_donations)

        file_name = name.replace(" ","_") + ".txt"
        full_path = os.path.join (cur_dir,file_name)

        with open (full_path, "w") as file:
            file.write (letter)


def exit_program():
    print("Bye!")
    sys.exit()  # exit the interactive script


def main():
    prompt_action = {"1" : send_a_thank_you,
                     "2" : create_report,
                     "3" : print_report,
                     "4" : exit_program }

    while True:
        response = input(prompt)  # continuously collect user selection
        # now redirect to feature functions based on the user selection
        try:
            prompt_action[response]()
        except KeyError:
            print ("try again")


if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically if this module is imported
    main()
